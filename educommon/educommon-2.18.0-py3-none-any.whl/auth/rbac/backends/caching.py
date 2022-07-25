# coding: utf-8
from __future__ import absolute_import

from collections import defaultdict
from datetime import date
from itertools import chain
from logging import getLogger
from time import time

from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db.models.query_utils import Q
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
import six

from educommon.utils.misc import cached_property

from ..models import Permission
from ..models import Role
from ..models import RoleParent
from ..models import RolePermission
from ..models import UserRole
from .base import BackendBase


class CachingBackend(BackendBase):

    u"""Бэкенд, кеширующий объекты подсистемы RBAC.

    Перезагружает данные из БД в следующих случаях:

        - при инициализации подсистемы RBAC;
        - при изменении или удалении ролей;
        - при изменении прав в ролях;
        - при назначении или отзыве ролей у пользователей.
    """

    CACHE_KEY = 'RBAC_DATA_CHANGE_TIME'
    u"""Ключ кеша, в котором сохраняется время изменения объектов в БД."""

    # Модели, данные которых кэшируются.
    _cached_models = {
        Permission,
        Role,
        RoleParent,
        UserRole,
        RolePermission
    }

    @cached_property
    def _logger(self):
        return getLogger(__name__.rpartition('.')[0])

    def __init__(self, *args, **kwargs):
        super(CachingBackend, self).__init__(*args, **kwargs)

        # Максимальная продолжительность кеширования объектов до их
        # перезагрузки (в секундах).
        self.CACHE_TIMEOUT = kwargs.get('CACHE_KEY', 1 * 60 * 60)

        self._loaded_at = 0  # время последней загрузки данных

        self._permissions_by_id = {}
        self._permissions_by_name = {}
        self._role_permissions = defaultdict(set)
        self._role_children = defaultdict(set)
        self._user_roles = defaultdict(set)
        # ---------------------------------------------------------------------
        # настройка сигналов

        def get_dispatch_uid(name):
            return '.'.join((self.__class__.__name__, name))

        self._manager.post_init.connect(
            self._signal_handler,
            dispatch_uid=get_dispatch_uid('post_init'),
        )
        post_save.connect(
            self._signal_handler,
            dispatch_uid=get_dispatch_uid('post_save'),
        )
        post_delete.connect(
            self._signal_handler,
            dispatch_uid=get_dispatch_uid('post_delete'),
        )

    def _signal_handler(self, sender, **kwargs):
        u"""Обработчик сигналов об изменениях в моделях."""
        if (
            # changed приходит только от post_init
            kwargs.get('changed', False) or
            # а port_save и post_delete нужно обрабатывать только для
            # кэшируемых моделей
            sender in self._cached_models
        ):
            self._set_data_change_time()

    def _get_data_change_time(self):
        u"""Возвращает время последнего изменения объектов RBAC в БД."""
        t = cache.get(self.CACHE_KEY)
        return float(t) if t else None

    def _set_data_change_time(self):
        u"""Сохраняет время последнего изменения объектов RBAC в БД."""
        t = time()
        cache.set(self.CACHE_KEY, six.text_type(t), self.CACHE_TIMEOUT)
        return t

    def _is_out_of_date(self):
        u"""Возвращает True, если кешированные данные устарели."""
        data_change_time = self._get_data_change_time()
        if data_change_time is None:
            # Либо, объекты еще не кэшировались, либо истекло время хранения
            # ключа, поэтому пора перезагрузить объекты RBAC.
            data_change_time = self._set_data_change_time()

        return self._loaded_at < data_change_time

    def _clear(self):
        u"""Очистка кеша объектов RBAC."""
        self._permissions_by_id.clear()
        self._permissions_by_name.clear()
        self._role_permissions.clear()
        self._role_children.clear()
        self._user_roles.clear()

    def _load_permissions(self):
        u"""Загрузка данных о разрешениях RBAC."""
        for pk, name in Permission.objects.values_list('pk', 'name'):
            self._permissions_by_id[pk] = name
            self._permissions_by_name[name] = pk

    def _load_role_hierarchy(self):
        u"""Загрузка данных о подчиненности ролей RBAC."""
        query = RoleParent.objects.values_list('parent', 'role')

        for parent_id, role_id in query:
            self._role_children[parent_id].add(role_id)

    def _load_role_permissions(self):
        u"""Загрузка данных о разрешениях ролей RBAC."""
        for role_id, permission_id in RolePermission.objects.values_list(
            'role', 'permission'
        ):
            self._role_permissions[role_id].add(permission_id)

    def _load_user_roles(self):
        u"""Загрузка данных о ролях пользователей."""
        query = UserRole.objects.filter(
            Q(date_to__isnull=True) | Q(date_to__gte=date.today()),
        ).values_list(
            'content_type', 'object_id', 'date_from', 'date_to', 'role'
        )

        for ct_id, obj_id, date_from, date_to, role_id in query:
            self._user_roles[ct_id, obj_id].add(
                (date_from, date_to, role_id)
            )

    def _get_role_descendants(self, role_id, include_self=False):
        u"""Возвращает вложенные роли."""
        result = set()

        if include_self:
            result.add(role_id)

        for child_role_id in self._role_children[role_id]:
            result.update(
                self._get_role_descendants(child_role_id, include_self=True)
            )

        return result

    def _get_user_roles(self, user):
        u"""Возвращает все роли пользователя, в т.ч. и вложенные.

        :rtype: set
        """
        content_type_id = ContentType.objects.get_for_model(user).id
        roles_data = self._user_roles[content_type_id, user.id]
        today = date.today()

        return set(chain(*(
            self._get_role_descendants(role_id, include_self=True)
            for date_from, date_to, role_id in roles_data
            if (date_from or today) <= today <= (date_to or today)
        )))

    def _get_user_permissions(self, user):
        u"""Возврвщает все доступные пользователю разрешения.

        :rtype: itertools.chain
        """
        def get_role_permissions(role_id):
            # pylint: disable=protected-access
            for permission_id in self._role_permissions[role_id]:
                yield permission_id
                for name in self._manager.get_dependent_permissions(
                    self._permissions_by_id[permission_id]
                ):
                    yield self._permissions_by_name[name]

        return chain(*(
            get_role_permissions(role_id)
            for role_id in self._get_user_roles(user)
        ))

    def _reload(self, force=False):
        u"""Перезагрузка кешируемых объектов при необходимости.

        :param bool force: Указывает на необходимость принудительной
            перезагрузки.
        """
        if force or self._is_out_of_date():
            self._clear()

            self._load_permissions()
            self._load_role_permissions()
            self._load_role_hierarchy()
            self._load_user_roles()

            self._loaded_at = time()

    def has_perm(self, user, perm_name):
        u"""Проверяет наличие у пользователя разрешения.

        :param user: Пользователь, возвращаемый функцией
            ioc.get('get_current_user').
        :param basestring perm_name: Имя разрешения.

        :rtype: bool
        """
        self._reload()

        assert perm_name in self._permissions_by_name, perm_name

        permission_id = self._permissions_by_name[perm_name]
        return permission_id in self._get_user_permissions(user)

    def has_access(self, action, request):
        u"""Проверяет наличие у текущего пользователя разрешения.

        :param action: Экшн, к которому проверяется наличие доступа.
        :type action: m3.actions.Action

        :param request: HTTP-запрос.
        :type request: django.http.HttpRequest

        :rtype: bool
        """
        if not self._need_check_access(action):
            return True

        user = self._get_current_user(request)
        if user is None:
            return False

        self._reload()

        # Id разрешений экшена, доступность которых будем проверять
        action_permissions = set(
            self._permissions_by_name[perm_name]
            for perm_name in self._get_action_permissions(action)
        )

        for permission_id in self._get_user_permissions(user):
            if permission_id in action_permissions:
                permission_name = self._permissions_by_id[permission_id]
                if self._check_permission(permission_name, action, request,
                                          user):
                    return True

        return False
