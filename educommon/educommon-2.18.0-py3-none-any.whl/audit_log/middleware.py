# coding: utf-8
from __future__ import absolute_import

import six

from .utils import get_audit_log_context
from .utils import set_db_param


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object



class AuditLogMiddleware(MiddlewareMixin):

    u"""Устанавливает параметры из запроса в текущей сессии БД.

    Устанавливает в custom settings postgresql:
      - audit_log.user_id - id пользователя;
      - audit_log.user_type_id - id ContentType модели пользователя;
      - audit_log.ip - IP адрес, с которого пришел запрос.

    В дальнейшем эта информация используется в логирующем триггере.
    """

    def process_request(self, request):
        for name, value in six.iteritems(get_audit_log_context(request)):
            set_db_param('audit_log.' + name, value)

    def process_response(self, request, response):
        for name in ('user_id', 'user_type_id', 'ip'):
            set_db_param('audit_log.' + name, None)
        return response
