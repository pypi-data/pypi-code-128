# coding: utf-8
u"""Описания пользовательского интерфейса приложения логирования СМЭВ."""
from __future__ import absolute_import

from m3_ext.ui import all_components as ext
from m3_ext.ui.icons import Icons
from objectpack.ui import BaseEditWindow
from objectpack.ui import BaseListWindow
from objectpack.ui import ModelEditWindow

from educommon.ws_log.models import SmevLog
from educommon.ws_log.models import SmevProvider


class SmevLogEditWindow(
    ModelEditWindow.fabricate(
        SmevLog, field_list=['request', 'response', 'result'])
):
    u"""Окно редактирования логов СМЭВ."""

    def set_params(self, params):
        u"""Настройка окна."""
        super(SmevLogEditWindow, self).set_params(params)
        self.height, self.width = 800, 800

        self.make_read_only()

        for field in self.form.items:
            if isinstance(field, ext.ExtTextArea):
                field.height = 240


class SmevLogListWindow(BaseListWindow):
    u"""Окно списка логов СМЭВ."""

    def _init_components(self):
        u"""Создание компонентов окна."""
        super(SmevLogListWindow, self)._init_components()
        self.print_button = ext.ExtButton(
            text=u'Печать', handler='printSmevLogsReport', icon_cls='printer')

    def _do_layout(self):
        u"""Расположение компонентов окна."""
        super(SmevLogListWindow, self)._do_layout()
        self.grid.top_bar.items.append(self.print_button)
        self.grid.top_bar.button_edit.icon_cls = Icons.APPLICATION_VIEW_DETAIL

    def set_params(self, params):
        u"""Настройка окна."""
        super(SmevLogListWindow, self).set_params(params)
        self.maximized = True
        self.settings_report_window_url = params['settings_report_window_url']
        self.template_globals = 'ui-js/smev-logs-list-window.js'

class SmevProviderListWindow(BaseListWindow):

    u"""Окно списка поставщиков СМЭВ."""

    def set_params(self, params):
        super(SmevProviderListWindow, self).set_params(params)
        self.width = 1000


class SmevProviderEditWindow(ModelEditWindow):

    u"""Окно добавления/редактирования поставщиков СМЭВ."""

    model = SmevProvider

    def set_params(self, params):
        super(SmevProviderEditWindow, self).set_params(params)
        self.form.label_width = 200
        self.width = 500


class SmevLogReportWindow(BaseEditWindow):

    def _init_components(self):
        u"""Создание компонентов окна."""
        super(SmevLogReportWindow, self)._init_components()
        self.field_date_begin = ext.ExtDateField(
            name='date_begin',
            label=u'Дата с',
            allow_blank=False,
            anchor='100%')

        self.field_date_end = ext.ExtDateField(
            name='date_end',
            label=u'Дата по',
            allow_blank=False,
            anchor='100%')

        self.field_institute = ext.ExtDictSelectField(
            label=u'Организация',
            name='institute_id',
            display_field='code',
            anchor='100%',
            hide_trigger=False,
            hide_edit_trigger=True,
            allow_blank=False)

    def _do_layout(self):
        u"""Расположение компонентов окна."""
        super(SmevLogReportWindow, self)._do_layout()
        self.form.items.extend([
            self.field_institute,
            self.field_date_begin,
            self.field_date_end,
        ])

    def set_params(self, params):
        u"""Настройка окна."""
        super(SmevLogReportWindow, self).set_params(params)
        self.height, self.width = 200, 400

        self.field_institute.pack = params['institute_pack']

        if params.get('institute'):
            self.field_institute.set_value_from_model(params['institute'])

        self.template_globals = 'ui-js/smev-logs-report-setting-window.js'
