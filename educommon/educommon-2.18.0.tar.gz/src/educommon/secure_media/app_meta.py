# coding: utf-8
from __future__ import absolute_import

import os

from django import http
from django.conf import settings
from django.conf.urls import url
from m3 import M3JSONEncoder
from m3_django_compat import is_authenticated
from sendfile import sendfile


def check_autorization(request, path):

    # Если файл в media/public, то отдаем сразу без проверки
    # Вообще это делается соответствующим конфигурированием NGINX
    path_list = path.split(os.path.sep)
    if path_list and path_list[0] == "public":
        return sendfile(request, os.path.join(settings.MEDIA_ROOT, path))

    if not is_authenticated(request.user):
        result = M3JSONEncoder().encode(
            {'success': False,
             'message': u'Вы не авторизованы. Возможно, закончилось время '
                        u'пользовательской сессии. Для повторной '
                        u'аутентификации обновите страницу.'})
        return http.HttpResponse(result, content_type='application/json')

    return sendfile(request, os.path.join(settings.MEDIA_ROOT, path))


urlpatterns = [
    url(r'^media/(?P<path>.*)$', check_autorization)
]
