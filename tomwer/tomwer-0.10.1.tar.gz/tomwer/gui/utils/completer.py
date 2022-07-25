# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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

"""module defining dedicated completer"""


__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "23/03/2022"


from typing import Optional
from silx.gui import qt


class _CodeCompleter(qt.QCompleter):
    ConcatenationRole = qt.Qt.UserRole + 1

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.create_model(data)

    def pathFromIndex(self, ix):
        return ix.data(_CodeCompleter.ConcatenationRole)

    def create_model(self, data):
        def addItems(parent, elements, t=""):
            for text in elements:
                item = qt.QStandardItem(text)
                data = t + "." + text if t else text
                item.setData(data, _CodeCompleter.ConcatenationRole)
                parent.appendRow(item)

        model = qt.QStandardItemModel(self)
        addItems(model, data)
        self.setModel(model)


class _LineEditWithCompleter(qt.QLineEdit):
    def __init__(self, completer, parent=None, data_type="url"):
        super().__init__(parent)
        self._completer = completer

    def keyPressEvent(self, key_event):
        # add Ctr + space for completion
        modifiers = key_event.modifiers()
        if qt.Qt.KeyboardModifier.ControlModifier == modifiers:
            if key_event.key() == qt.Qt.Key.Key_Space:
                self._completer.complete(self.rect())

        super().keyPressEvent(key_event)


class _TextCompleterWidget(qt.QWidget):
    """
    Simple widget to ease text research.
    """

    sigTextSelected = qt.Signal(str)

    def __init__(self, texts: tuple, parent=None) -> None:
        if not isinstance(texts, tuple):
            raise TypeError("texts is expected to be a tuple.")
        super().__init__(parent)
        layout = qt.QVBoxLayout()
        self.setLayout(layout)

        self._completer = _CodeCompleter(texts, self)

        self._lineEdit = _LineEditWithCompleter(parent=self, completer=self._completer)
        self._lineEdit.setCompleter(self._completer)
        layout.addWidget(self._lineEdit)

    def setText(self, text: str) -> None:
        self._lineEdit.setText(text)

    def text(self) -> str:
        return self._lineEdit.text()


class UrlCompleterDialog(qt.QDialog):
    def __init__(
        self, urls: tuple, parent=None, current_url: Optional[str] = None
    ) -> None:
        super().__init__(parent)
        self._urls = urls
        self.setWindowTitle("Url research")

        self.setLayout(qt.QVBoxLayout())
        self._completerWidget = _TextCompleterWidget(texts=urls, parent=self)
        self._completerWidget.setToolTip(
            "You can complete url. Use ctr + space to complete"
        )
        if current_url is not None:
            self._completerWidget.setText(current_url)
        self.layout().addWidget(self._completerWidget)

        types = qt.QDialogButtonBox.Cancel | qt.QDialogButtonBox.Ok
        self._buttons = qt.QDialogButtonBox(self)
        self._buttons.setStandardButtons(types)
        self.layout().addWidget(self._buttons)

        # connect signal / slot
        self._buttons.button(qt.QDialogButtonBox.Cancel).released.connect(self.reject)
        self._buttons.button(qt.QDialogButtonBox.Ok).released.connect(self.accept)
        self._completerWidget._lineEdit.textChanged.connect(
            self._updateOkButtonAvailability
        )

    def _updateOkButtonAvailability(self, *args, **kwargs):
        ok_enable = self._completerWidget.text() in self._urls
        self._buttons.button(qt.QDialogButtonBox.Ok).setEnabled(ok_enable)

    def selected_url(self):
        return self._completerWidget.text()

    def sizeHint(self):
        return qt.QSize(600, 100)
