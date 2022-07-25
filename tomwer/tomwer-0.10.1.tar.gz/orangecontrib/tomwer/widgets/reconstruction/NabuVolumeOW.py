# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

__authors__ = ["C. Nemoz", "H. Payno"]
__license__ = "MIT"
__date__ = "14/02/2020"


import logging
from tomwer.core.scan.hdf5scan import HDF5TomoScan
from tomwer.gui.reconstruction.nabu import check
from contextlib import AbstractContextManager
from silx.gui import qt
from tomwer.synctools.stacks.reconstruction.nabu import NabuVolumeProcessStack
from tomwer.core.process.reconstruction.nabu.nabuvolume import NabuVolume
from tomwer.gui.reconstruction.nabu.volume import NabuVolumeWindow
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.cluster import SlurmClusterConfiguration
from tomwer.core.scan.futurescan import FutureTomwerScan
from orangecontrib.tomwer.widgets.utils import WidgetLongProcessing
from orangewidget.settings import Setting
from orangewidget import gui
from orangewidget.widget import Input, Output
from ...orange.managedprocess import SuperviseOW
from tomwer.core.process.reconstruction.nabu import utils as nabu_utils
from tomwer.core.utils.char import BETA_CHAR, DELTA_CHAR
from collections.abc import Iterable
from tomwer.utils import docstring
from tomwer.core import settings
import tomwer.core.process.reconstruction.nabu.nabuvolume
import functools
import copy

_logger = logging.getLogger(__name__)


class NabuVolumeOW(WidgetLongProcessing, SuperviseOW):
    """
    A simple widget managing the copy of an incoming folder to an other one

    :param parent: the parent widget
    """

    # note of this widget should be the one registered on the documentation
    name = "nabu volume reconstruction"
    id = "orange.widgets.tomwer.reconstruction.NabuVolumeOW.NabuVolumeOW"
    description = (
        "This widget will call nabu for running a reconstruction " "on a volume"
    )
    icon = "icons/nabu_3d.svg"
    priority = 15
    keywords = ["tomography", "nabu", "reconstruction", "volume"]

    ewokstaskclass = tomwer.core.process.reconstruction.nabu.nabuvolume.NabuVolume

    want_main_area = True
    resizing_enabled = True
    compress_signal = False
    allows_cycle = True

    _rpSetting = Setting(dict())
    # kept for compatibility

    static_input = Setting(
        {"data": None, "nabu_volume_params": None, "nabu_params": None}
    )

    sigScanReady = qt.Signal(TomwerScanBase)
    "Signal emitted when a scan is ended"

    TIMEOUT = 30

    class Inputs:
        data = Input(
            name="data",
            type=TomwerScanBase,
            doc="one scan to be process",
            default=True,
            multiple=False,
        )
        cluster_in = Input(
            name="cluster_config",
            type=SlurmClusterConfiguration,
            doc="slurm cluster to be used",
            multiple=False,
        )

    class Outputs:
        data = Output(name="data", type=TomwerScanBase, doc="one scan to be process")

        future_out = Output(
            name="future_data",
            type=FutureTomwerScan,
            doc="data with some remote processing",
        )

    class DialogCM(AbstractContextManager):
        """Simple context manager to hida / show button dialogs"""

        def __init__(self, dialogButtonsBox):
            self._dialogButtonsBox = dialogButtonsBox

        def __enter__(self):
            self._dialogButtonsBox.show()

        def __exit__(self, exc_type, exc_val, exc_tb):
            self._dialogButtonsBox.hide()

    def __init__(self, parent=None):
        """
        Widget which read the .hdf5 generated by octave and modify it.
        Then run a subprocess to call octave and run ftseries

        :param bool _connect_handler: True if we want to store the modifications
                                      on the setting. Need for unit test since
                                      keep alive qt widgets.
        :param recons_params: reconsparameter to be used by the FTWidget.
                              If None, some will be created.
        :type: :class:`QReconsParams`
        """
        SuperviseOW.__init__(self, parent)
        WidgetLongProcessing.__init__(self)
        self._slurmCluster = None
        self.__exec_for_ci = False
        # processing tool
        self._processingStack = NabuVolumeProcessStack(self, process_id=self.process_id)

        _layout = gui.vBox(self.mainArea, self.name).layout()
        # main widget
        self._nabuWidget = NabuVolumeWindow(parent=self)
        _layout.addWidget(self._nabuWidget)
        # add button to validate when change reconstruction parameters is called
        types = qt.QDialogButtonBox.Ok
        self._buttons = qt.QDialogButtonBox(self)
        self._buttons.setStandardButtons(types)
        _layout.addWidget(self._buttons)

        # set up
        self._buttons.hide()

        # load settings
        nabu_volume_params = self.static_input.get("nabu_volume_params", None)
        if nabu_volume_params is None:
            nabu_volume_params = self._rpSetting
        if nabu_volume_params != dict():
            try:
                self._nabuWidget.setConfiguration(nabu_volume_params)
            except Exception:
                _logger.warning("fail to load reconstruction settings")

        # connect signal / slot
        self._processingStack.sigComputationStarted.connect(self._startProcessing)
        self._processingStack.sigComputationEnded.connect(self._endProcessing)
        self._buttons.button(qt.QDialogButtonBox.Ok).clicked.connect(self.accept)
        self._nabuWidget.sigConfigChanged.connect(self._updateSettingsVals)

    @Inputs.data
    def process(self, scan: TomwerScanBase):
        assert isinstance(scan, (TomwerScanBase, type(None)))
        if scan is None:
            return
        scan_ = copy.copy(scan)
        scan_.clear_latest_vol_reconstructions()

        if isinstance(scan, HDF5TomoScan):
            if not check.check_flat_series(
                scan_, logger=_logger, user_input=settings.isOnLbsram(scan=scan_)
            ):
                self.Outputs.data.send(scan_)
                return
            if not check.check_dark_series(
                scan_, logger=_logger, user_input=settings.isOnLbsram(scan=scan_)
            ):
                self.Outputs.data.send(scan_)
                return

        # insure we are able to reconstruct
        if scan.nabu_recons_params in ({}, None):
            _logger.error(
                "No reconstruction parameters found from nabu "
                "slices for {}. You should first run slice "
                "reconstruction prior to volume reconstruction"
                "".format(str(scan))
            )
            self.Outputs.data.send(scan)
            self.sigScanReady.emit(scan)
            return

        config = scan.nabu_recons_params
        if "phase" in config and "delta_beta" in config["phase"]:
            pag_dbs = config["phase"]["delta_beta"]
            if isinstance(pag_dbs, str):
                try:
                    pag_dbs = nabu_utils.retrieve_lst_of_value_from_str(
                        config["phase"]["delta_beta"], type_=float
                    )
                except Exception:
                    pass
            if len(pag_dbs) > 1:
                _logger.warning(
                    "Several value found for {} / {}. Volume"
                    "reconstruction take one at most."
                    "".format(DELTA_CHAR, BETA_CHAR)
                )
                timeout = NabuVolumeOW.TIMEOUT if settings.isOnLbsram(scan) else None
                self._dialogDB = _DeltaBetaSelectorDialog(
                    values=pag_dbs, parent=None, timeout=timeout
                )
                self._dialogDB.setModal(False)
                self._callbackDB = functools.partial(
                    self._updateDB, scan, self._dialogDB
                )
                self._dialogDB.accepted.connect(self._callbackDB)
                self._callbackTimeout = functools.partial(self._skipProcessing, scan)
                self._dialogDB.timeoutReached.connect(self._callbackTimeout)
                self._dialogDB.show()
                return

        self._processingStack.add(scan_, self.getConfiguration())

    @docstring(SuperviseOW)
    def reprocess(self, dataset):
        if (
            dataset.axis_params is None
            or dataset.axis_params.relative_cor_value is None
        ):
            # try to retrieve last computed cor value from nabu process
            r_cor = NabuVolume.retrieve_last_relative_cor(dataset)
            if dataset.axis_params is None:
                from tomwer.synctools.axis import QAxisRP

                dataset.axis_params = QAxisRP()
            try:
                dataset.axis_params.set_relative_value(
                    float(r_cor) - dataset.dim_1 / 2.0
                )
            except Exception:
                pass

        self.process(dataset)

    @Inputs.cluster_in
    def setCluster(self, cluster):
        self._slurmCluster = cluster

    def _updateDB(self, scan, dialog):
        db = dialog.getSelectedValue()
        if db is not None:
            try:
                scan.nabu_recons_params["phase"]["delta_beta"] = db
            except Exception as e:
                logging.error(e)
            else:
                self.process(scan=scan)

    def _endProcessing(self, scan, future_scan):
        WidgetLongProcessing._endProcessing(self, scan)
        if scan is not None:
            self.Outputs.data.send(scan)
            self.sigScanReady.emit(scan)
        if future_scan is not None:
            self.Outputs.future_out.send(future_scan)

    def setDryRun(self, dry_run):
        self._processingStack.setDryRun(dry_run)

    def _ciExec(self):
        self.activateWindow()
        self.raise_()
        self.show()

    def _replaceExec_(self):
        """used for CI, replace the exec_ call ny"""
        self.__exec_for_ci = True

    def _updateSettingsVals(self):
        self._rpSetting = self.getConfiguration()
        # kept for compatibility
        self.static_input = {
            "data": None,
            "nabu_volume_params": self.getConfiguration(),
            "nabu_params": None,
        }

    def _skipProcessing(self, scan):
        self.Outputs.data.send(scan)
        self.sigScanReady.emit(scan)

    def getConfiguration(self):
        config = self._nabuWidget.getConfiguration()
        config["cluster_config"] = self._slurmCluster
        return config

    def setConfiguration(self, config):
        # ignore slurm cluster. Defined by the upper widget
        config.pop("cluster_config", None)
        self._nabuWidget.setConfiguration(config=config)


class _DeltaBetaSelectorDialog(qt.QDialog):
    timeoutReached = qt.Signal()

    def __init__(self, values, parent=None, timeout=None):
        """

        :param values:
        :param parent:
        :param timeout: if a timeout is provided once reach this will
                        automatically reject the delta / beta selection.
                        This is needed when on lbsral to avoid 'locking'
                        a reconstruction. In sec.
        """
        qt.QDialog.__init__(self, parent)
        self.setLayout(qt.QVBoxLayout())

        self.mainWidget = _DeltaBetaSelector(parent=self, values=values)
        self.layout().addWidget(self.mainWidget)

        types = qt.QDialogButtonBox.Ok | qt.QDialogButtonBox.Cancel
        self._buttons = qt.QDialogButtonBox(parent=self)
        self._buttons.setStandardButtons(types)
        self.layout().addWidget(self._buttons)
        self._timeout = timeout
        if self._timeout is None:
            self.setWindowTitle(
                "Select one value for {} / {}".format(DELTA_CHAR, BETA_CHAR)
            )
        else:
            self.setWindowTitle(
                "Select one value for {} / {}. (close automatically in {} "
                "sec.)".format(DELTA_CHAR, BETA_CHAR, self._timeout)
            )

        # connect signal / slot
        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)

        # expose API
        self.getSelectedValue = self.mainWidget.getSelectedValue

        # add timers
        if timeout is not None:
            self._timer = qt.QTimer()
            self._timer.timeout.connect(self.reject)
            self._timer.start(timeout * 1000)
            self._displayTimer = qt.QTimer()
            self._displayTimer.timeout.connect(self._updateTitle)
            self._displayTimer.start(1000)
        else:
            self._timer = None

    def reject(self):
        if self._timer:
            self._timer.stop()
            self._timer.timeout.disconnect(self.reject)
            self._displayTimer.stop()
            self._displayTimer.timeout.disconnect(self._updateTitle)
            self._timer = None

        qt.QDialog.reject(self)

    def _updateTitle(self):
        self._timeout = self._timeout - 1
        if self._timeout <= 0:
            self.timeoutReached.emit()
            self.reject()
        else:
            self.setWindowTitle(
                "Select one value for {} / {}. (close automatically in {} "
                "sec.)".format(DELTA_CHAR, BETA_CHAR, self._timeout)
            )
            self._displayTimer.start(1000)


class _DeltaBetaSelector(qt.QTableWidget):
    """Widget used to select a value of delta beta if several provided"""

    def __init__(self, values, parent=None):
        qt.QTableWidget.__init__(self, parent)
        self.setSelectionMode(qt.QAbstractItemView.SingleSelection)
        self.setHorizontalHeaderLabels([DELTA_CHAR + " / " + BETA_CHAR])
        self.setRowCount(0)
        self.setColumnCount(1)
        self.verticalHeader().hide()
        if hasattr(self.horizontalHeader(), "setSectionResizeMode"):  # Qt5
            self.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Stretch)
        else:  # Qt4
            self.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)
        self.setAcceptDrops(False)

        # set up
        self.setValues(values=values)

    def setValues(self, values: Iterable):
        self.setHorizontalHeaderLabels([DELTA_CHAR + " / " + BETA_CHAR])
        self.setRowCount(len(values))
        self.setColumnCount(1)
        for i_value, value in enumerate(values):
            _item = qt.QTableWidgetItem()
            _item.setText(str(value))
            _item.setFlags(qt.Qt.ItemIsEnabled | qt.Qt.ItemIsSelectable)
            self.setItem(i_value, 0, _item)
            _item.setSelected(i_value == 0)

    def getSelectedValue(self):
        sel = None
        for item in self.selectedItems():
            sel = item.text()
        return sel
