# coding: utf-8
from __future__ import absolute_import

from importlib import import_module
from uuid import uuid4
import os

from django.conf import settings
from django.utils.text import slugify
import six

from educommon.report.constructor.models import ReportTemplate


_BUILDERS_PACKAGE = 'educommon.report.constructor.builders'


class BuildReportTaskMixin(object):

    _builders = {
        ReportTemplate.EXCEL_SIMPLE:
            _BUILDERS_PACKAGE + '.excel.product.ReportBuilder',
        ReportTemplate.EXCEL_MERGED:
            _BUILDERS_PACKAGE + '.excel.with_merged_cells.ReportBuilder',
    }

    def _get_builder(self, report_template, fmt):
        if report_template.format == ReportTemplate.USER_DEFINED:
            report_format = fmt
        else:
            report_format = report_template.format

        builder_name = self._builders[report_format]
        module_name, _, class_name = builder_name.rpartition('.')
        module = import_module(module_name)
        return getattr(module, class_name)

    def make_report(self, *args, **kwargs):
        u"""Совершает сборку отчета."""
        result = dict()
        report_template_id = kwargs['report_template_id']
        report_template = ReportTemplate.objects.get(pk=report_template_id)
        reports_dir = os.path.join(settings.MEDIA_ROOT, 'report_constructor')
        if not os.path.exists(reports_dir):
            os.mkdir(reports_dir)
        while True:
            report_id = six.text_type(uuid4().hex)
            report_dir = os.path.join(reports_dir, report_id)
            if not os.path.exists(report_dir):
                os.mkdir(report_dir)
                break
        file_name = (
            slugify(report_template.title, allow_unicode=True) + u'.xlsx'
        )
        file_path = os.path.join(report_dir, file_name)
        builder_class = self._get_builder(report_template, kwargs['format'])
        user = kwargs['content_type'].get_object_for_this_type(
            id=kwargs['object_id']
        )
        builder = builder_class(report_template, file_path, user)
        builder.build()
        link = os.path.join(
            settings.MEDIA_URL, u'report_constructor', report_id, file_name
        )
        download_link = u'<a href="{}" target="_blank" download>{}</a>'.format(
            link, file_name)
        result['download_link'] = download_link
        return result
