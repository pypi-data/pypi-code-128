# coding: utf-8
u"""Паки и экшены для окна реестра "Роли"."""
from __future__ import absolute_import

from collections import defaultdict
from functools import reduce
from itertools import chain
from operator import or_
import json

from django.contrib.contenttypes.models import ContentType
from django.db.models import Case
from django.db.models import F
from django.db.models import Q
from django.db.models import Value
from django.db.models import When
from django.db.models.fields import CharField
from django.db.models.functions import Concat
from django.utils.functional import cached_property
from m3.actions import ApplicationLogicException
from m3.actions import PreJsonResult
from m3.actions.results import OperationResult
from m3_django_compat import atomic
from m3_django_compat import get_request_params
from objectpack.actions import BaseAction
from objectpack.actions import BasePack
from objectpack.actions import ObjectPack
from objectpack.actions import ObjectRowsAction
from objectpack.actions import ObjectSelectWindowAction
from objectpack.exceptions import ValidationError
from objectpack.models import VirtualModel
from objectpack.tools import extract_int_list
from objectpack.tree_object_pack.actions import TreeObjectPack
import six

from educommon.auth.rbac.config import rbac_config
from educommon.auth.rbac.utils import get_permission_full_title
from educommon.m3 import convert_validation_error_to
from educommon.m3 import get_id_value
from educommon.m3 import get_pack
from educommon.m3 import get_pack_id

from . import ui
from .constants import PERM_SOURCE__DEPENDENCIES
from .constants import PERM_SOURCE__NESTED_ROLE
from .constants import PERM_SOURCE__ROLE
from .manager import rbac
from .models import Permission
from .models import Role
from .models import RoleParent
from .models import RolePermission
from .models import RoleUserType
from .models import UserRole
from .permissions import PERM_GROUP__ROLE


def _get_role(role_id):
    try:
        return Role.objects.get(pk=role_id)
    except Role.DoesNotExist:
        raise ApplicationLogicException(
            u'Роль ID:{} не существует'.format(role_id)
        )


class RolesTreeRowsAction(ObjectRowsAction):

    u"""Экшн, отдающий данные иерархии ролей.

    Т.к. одна и та же роль может быть включена в несколько ролей, то она также
    может отображаться вложенной в несколько ролей.
    """

    @cached_property
    def _parent_ids(self):
        u"""Id ролей, содержащих в себе другие роли.

        :rtype: set
        """
        result = RoleParent.objects.values_list('parent', flat=True).distinct()

        return set(result)

    def is_leaf(self, role):
        u"""Возвращает True, если данная роль не включает другие роли.

        :param role: Роль.
        :type role: Role

        :rtype: bool
        """
        if get_request_params(self.request).get('filter', False):
            result = True
        else:
            result = role.id not in self._parent_ids

        return result

    def prepare_object(self, obj):
        u"""Сохранение данных роли в словарь перед сериализацией в JSON."""
        data = super(RolesTreeRowsAction, self).prepare_object(obj)

        data['leaf'] = self.is_leaf(obj)

        return data

    def run(self, *args, **kwargs):
        result = super(RolesTreeRowsAction, self).run(*args, **kwargs)

        data = result.data.get('rows', [])

        return PreJsonResult(data)


class AddRoleToRoleWindowAction(ObjectSelectWindowAction):

    u"""Отображение окна добавления одной роли в другую."""

    def create_window(self):
        self.win = ui.RoleSelectWindow()

    def set_window_params(self):
        super(AddRoleToRoleWindowAction, self).set_window_params()

        self.win_params['pack'] = self.parent

        role_id = getattr(self.context, self.parent.id_param_name)
        role = _get_role(role_id)
        self.win_params['role'] = role


class AddRoleToRoleAction(BaseAction):

    u"""Добавление одной роли к другой."""

    @convert_validation_error_to(ApplicationLogicException)
    def run(self, request, context):
        role_parent = RoleParent(
            role=_get_role(getattr(context, self.parent.id_param_name)),
            parent=_get_role(context.parent_id),
        )
        role_parent.full_clean()
        role_parent.save()

        return OperationResult()


class DeleteRoleFromRoleAction(BaseAction):

    u"""Удаление одной роли из другой."""

    def run(self, request, context):
        try:
            role_parent = RoleParent.objects.get(
                role=_get_role(getattr(context, self.parent.id_param_name)),
                parent_id=context.parent_id
            )
        except RoleParent.DoesNotExist:
            raise ApplicationLogicException(
                u'Выбранная роль должна являться вложенной ролью.'
            )

        role_parent.delete()

        return OperationResult()


class Pack(TreeObjectPack):

    u"""Пак окна реестра "Роли"."""

    model = Role
    title = u'Роли'

    columns = [
        dict(
            data_index='name',
            header=u'Название',
            searchable=True,
        ),
    ]

    list_window = ui.RolesListWindow
    add_window = ui.RoleAddWindow
    edit_window = ui.RoleEditWindow

    column_name_on_select = 'name'

    def __init__(self):
        super(Pack, self).__init__()

        self.replace_action('rows_action', RolesTreeRowsAction())

        self.add_role_to_role_window_action = AddRoleToRoleWindowAction()
        self.add_role_to_role_action = AddRoleToRoleAction()
        self.delete_role_from_role_action = DeleteRoleFromRoleAction()

        self.actions.extend((
            self.add_role_to_role_window_action,
            self.add_role_to_role_action,
            self.delete_role_from_role_action,
        ))
        # ---------------------------------------------------------------------
        # Настройка разрешений для экшенов пака.
        self.need_check_permission = True
        self.perm_code = PERM_GROUP__ROLE

        for action in (self.autocomplete_action,
                       self.list_window_action,
                       self.multi_select_window_action,
                       self.rows_action,
                       self.select_window_action,
                       self.edit_window_action):
            action.perm_code = 'view'

        for action in (self.new_window_action,
                       self.save_action,
                       self.delete_action,
                       self.add_role_to_role_window_action,
                       self.add_role_to_role_action,
                       self.delete_role_from_role_action):
            action.perm_code = 'edit'
        # ---------------------------------------------------------------------

    def extend_menu(self, menu):
        u"""Размещает в меню Пуск ссылку Администрирование --> Роли."""
        return menu.administry(
            menu.Item(self.title, self.list_window_action),
        )

    def declare_context(self, action):
        result = super(Pack, self).declare_context(action)

        if action in (self.rows_action,
                      self.add_role_to_role_window_action,
                      self.add_role_to_role_action):
            result[self.id_param_name] = dict(type='int')

        if action is self.rows_action:
            result['select_mode'] = dict(type='boolean', default=False)
            result['role_id'] = dict(type='int_or_none', default=None)

        if action is self.add_role_to_role_action:
            result['parent_id'] = dict(type='int')

        if action is self.save_action:
            result.update(
                name=dict(type='unicode'),
                description=dict(type='unicode', default=u''),
                permissions=dict(type='int_list', default=[]),
                user_type_ids=dict(type='json_or_none', default=None),
            )
        if action is self.delete_role_from_role_action:
            result['parent_id'] = dict(type=int)

        return result

    def get_rows_query(self, request, context):
        request_params = get_request_params(request)
        if request_params.get('filter'):
            return super(Pack, self).get_rows_query(request, context)

        current_role_id = getattr(context, self.id_param_name)

        if request_params.get('filter', False):
            result = super(Pack, self).get_rows_query(
                request, context
            )
        elif current_role_id < 0:
            # Вывод корневых ролей
            result = self.model.objects.exclude(
                pk__in=RoleParent.objects.values('role').distinct()
            )
        else:
            # Вывод ролей, вложенных в указанную роль
            result = self.model.objects.filter(
                pk__in=RoleParent.objects.filter(
                    parent=current_role_id
                ).values('role').distinct()
            )

        if context.select_mode and context.role_id is not None:
            # Режим выбора роли, в которую будет добавлена указанная роль.
            # В этом режиме надо исключить возможность создания циклов в
            # иерархии ролей, поэтому из результатов запроса надо исключить
            # все подчиненные роли.
            try:
                role = Role.objects.get(pk=context.role_id)
            except Role.DoesNotExist:
                raise ApplicationLogicException(
                    u'Роль ID:{} не найдена'.format(context.role_id)
                )

            result = result.exclude(
                pk__in=set([role.id]) | set(r.id for r in role.subroles)
            )

        return result

    def get_list_window_params(self, params, request, context):
        params = super(Pack, self).get_list_window_params(
            params, request, context
        )

        if not params['is_select_mode']:
            params['width'] = 700
            params['height'] = 600

        params['can_edit'] = rbac.has_access(self.save_action, request)

        return params

    def get_edit_window_params(self, params, request, context):
        params = super(Pack, self).get_edit_window_params(
            params, request, context
        )

        params['roles_pack'] = self
        params['partitions_pack'] = get_pack(PartitionsPack)
        params['permissions_pack'] = get_pack(PermissionsPack)

        result_pack = get_pack(ResultPermissionsPack)
        result_action = result_pack.result_permissions_action
        params['result_action_url'] = result_action.get_absolute_url()

        if rbac_config.user_types:
            params['show_user_types'] = True
            params['user_types'] = tuple(
                (u_type.id, u_type.name)
                for u_type in six.itervalues(
                    ContentType.objects.get_for_models(
                        *rbac_config.user_types
                    )
                )
            )
            if not params['create_new']:
                params['user_type_ids'] = tuple(
                    params['object'].user_types.values_list('pk', flat=True)
                )

        if not params['create_new']:
            params['permission_ids'] = list(
                params['object'].permissions.values_list('pk', flat=True)
            )

        params['can_edit'] = rbac.has_access(self.save_action, request)
        if not params['can_edit']:
            params['title'] = self.format_window_title(u'Просмотр')

        return params

    @staticmethod
    def _bind_user_types_to_role(role, types):
        u"""Привязывает типы пользователей к роли.

        При необходимости удаления типов пользователей, происходит
        проверка на наличие уже существующих пользователей с
        удаляемыми типами.

        :param role: роль в системе
        :type role: educommon.auth.rbac.models.Role
        :param list of int types: список ID записей модели
            :class:`~django.contrib.contenttypes.models.ContentType`
        """
        new_user_types = set(types)
        old_user_types = set(role.user_types.values_list('pk', flat=True))

        types_to_delete = old_user_types - new_user_types
        user_roles_to_delete = UserRole.objects.filter(
            role=role,
            content_type_id__in=types_to_delete,
        )
        # Проверка, есть ли пользователи с удаляемыми типами
        if types_to_delete and user_roles_to_delete.exists():
            related_content_types = ContentType.objects.filter(
                pk__in=types_to_delete
            )
            raise ApplicationLogicException(
                u'Невозможно отменить назначение роли для пользователей '
                u'типа {}, т.к. данная роль уже назначена {} '
                u'пользователей.'.format(
                    u', '.join(
                        u'"{}"'.format(ct.name) for ct in related_content_types
                    ),
                    u'этому типу'
                    if len(types_to_delete) == 1 else u'этим типам',
                )
            )
        # Удаление лишних типов пользователей
        RoleUserType.objects.filter(
            role=role, user_type__in=types_to_delete
        ).delete()
        # Добавление новых типов пользователей
        for user_type_id in new_user_types - old_user_types:
            RoleUserType.objects.create(
                role=role, user_type_id=user_type_id
            )

    @convert_validation_error_to(ValidationError)
    @atomic
    def save_row(self, obj, create_new, request, context):
        # При отключении флага удаляются все связи с типами пользователей
        if not (create_new or obj.can_be_assigned):
            RoleUserType.objects.filter(role=obj).delete()
        # Сохранение роли
        obj.full_clean()
        obj.save()

        if obj.can_be_assigned:
            self._bind_user_types_to_role(obj, context.user_type_ids or ())
        # Сохранение связи с родительской ролью
        if create_new and context.parent_id is not None:
            try:
                parent = Role.objects.get(pk=context.parent_id)
            except Role.DoesNotExist:
                raise ApplicationLogicException(
                    u'Роль ID:{} не существует.'.format(context.parent_id)
                )

            RoleParent.objects.create(role=obj, parent=parent)
        else:
            new_permissions = set(extract_int_list(request, 'permissions'))
            old_permissions = set(obj.permissions.values_list('pk', flat=True))

            # Удаление прав у роли
            for link in RolePermission.objects.filter(
                role=obj,
                permission__in=old_permissions - new_permissions,
            ):
                link.delete()

            # Добавление новых прав в роль
            for permission_id in new_permissions - old_permissions:
                RolePermission.objects.get_or_create(
                    role=obj, permission_id=permission_id
                )


@six.python_2_unicode_compatible
class Partition(VirtualModel):

    u"""Виртуальная модель "Раздел системы".

    Используется в связи с тем, что сведения о разделах не сохраняются в БД.
    """

    def __init__(self, data):
        self.__dict__.update(data)

    @classmethod
    def _get_ids(cls):
        if not hasattr(cls, 'data'):
            cls.data = []
            for i, title in enumerate(sorted(rbac.partitions)):
                cls.data.append(dict(id=i, title=title))

        return cls.data

    def __str__(self):
        return self.title


class PartitionsPack(ObjectPack):

    u"""Пак для грида "Разделы системы" окна редактирования роли."""

    model = Partition

    columns = [
        dict(
            data_index='__str__',
            header=u'Модуль',
        ),
    ]

    allow_paging = False

    def __init__(self):
        super(PartitionsPack, self).__init__()
        # ---------------------------------------------------------------------

        self.need_check_permission = True
        self.perm_code = PERM_GROUP__ROLE

        for action in self.actions:
            action.perm_code = 'view'
        # ---------------------------------------------------------------------


class PermissionsPack(ObjectPack):

    u"""Пак для грида "Права доступа" окна редактирования роли."""

    model = Permission

    columns = (
        dict(
            data_index='title_with_group',
            header=u'Разрешение',
            column_renderer='columnRenderer',
            width=4,
        ),
        dict(
            data_index='description',
            hidden=True,
        ),
        dict(
            data_index='dependencies',
            header=u'Включает разрешения',
            width=5,
        ),
    )
    list_sort_order = ('title_with_group',)

    allow_paging = False

    def __init__(self):
        super(PermissionsPack, self).__init__()
        # ---------------------------------------------------------------------

        self.need_check_permission = True
        self.perm_code = PERM_GROUP__ROLE

        for action in self.actions:
            action.perm_code = 'view'
        # ---------------------------------------------------------------------

    def declare_context(self, action):
        result = super(PermissionsPack, self).declare_context(action)

        if action is self.rows_action:
            result['partition_id'] = dict(type='int')

        return result

    def prepare_row(self, obj, request, context):
        result = super(PermissionsPack, self).prepare_row(
            obj, request, context
        )

        permission_names = (
            rbac.get_dependent_permissions(obj.name) - rbac.hidden_permissions
        )
        result.dependencies = json.dumps(sorted(
            get_permission_full_title(dependency)
            for dependency in permission_names
        ))

        return result

    def get_rows_query(self, request, context):
        # Определение название раздела по его id.
        try:
            partition = PartitionsPack.model.objects.get(
                id=context.partition_id
            ).title
        except PartitionsPack.model.DoesNotExists:
            raise ApplicationLogicException(
                u'Раздел {} не существует'.format(context.partition_id)
            )

        query = super(PermissionsPack, self).get_rows_query(
            request, context
        ).filter(
            # Условия для выборки разрешений только из раздела partition.
            reduce(or_, (
                Q(name__startswith=code + '/')
                for code in rbac.partitions[partition]
            )),
            hidden=False,
        ).annotate(title_with_group=Case(
            # Добавление названия группы к названию разрешения.
            output_field=CharField(),
            *(
                When(
                    name__startswith=group + '/',
                    then=Concat(
                        Value(title + u' - ' if title else u''),
                        F('title'),
                    )
                )
                for group, title in six.iteritems(rbac.groups)
            )
        ))

        return query
# -----------------------------------------------------------------------------

def _get_group_name(perm_name):
    """Возвращает имя группы разрешения."""
    return perm_name.split('/')[0]

def _get_group_title(perm_name):
    u"""Возвращает название группы разрешений."""
    group_name = _get_group_name(perm_name)
    group_title = rbac.groups[group_name]
    return group_title


def _get_partition_title(perm_name):
    group_name = perm_name.split('/')[0]

    for title, names in six.iteritems(rbac.partitions):
        if group_name in names:
            return title

    return u''


class ResultPermissionsAction(BaseAction):

    u"""Возвращает данные для грида "Итоговые разрешения"."""

    def _get_nested_roles(self, role_id):
        role_children = defaultdict(set)
        query = RoleParent.objects.values_list('parent', 'role')

        for parent_id, child_id in query:
            role_children[parent_id].add(child_id)

        def get_nested_roles(rid):
            result = set()

            if rid in role_children:
                for child_id in role_children[rid]:
                    result.add(child_id)
                    result.update(get_nested_roles(child_id))

            return result

        return get_nested_roles(role_id)

    def _get_nested_roles_permissions(self, role_id):
        query = Permission.objects.filter(
            pk__in=RolePermission.objects.filter(
                role_id__in=self._get_nested_roles(role_id)
            ).values('permission'),
            hidden=False,
        ).values_list('name', 'title', 'description')

        for name, title, description in query:
            yield dict(
                name=name,
                group=_get_group_title(name),
                partition=_get_partition_title(name),
                title=title,
                description=description,
                source=PERM_SOURCE__NESTED_ROLE,
            )

    def _get_dependent_permissions(self, permission_ids):
        permissions_by_id = {
            pk: (name, title, description)
            for pk, name, title, description in Permission.objects.filter(
                hidden=False,
            ).values_list(
                'pk', 'name', 'title', 'description'
            )
        }
        permissions_by_name = {
            name: (pk, title, description)
            for pk, (name, title, description) in six.iteritems(permissions_by_id)
        }

        for perm_id in permission_ids:
            # Может случиться так, что к роли будут привязаны скрытые
            # разрешения, но в permissions_by_id скрытых разрешений нет.
            if perm_id not in permissions_by_id:
                # Пропускаем скрытые разрешения.
                continue
            perm_name, _, _ = permissions_by_id[perm_id]
            dependent_perm_names = rbac.get_dependent_permissions(perm_name)
            dependent_perm_names -= rbac.hidden_permissions
            for name in dependent_perm_names:
                _, title, description = permissions_by_name[name]
                yield dict(
                    name=name,
                    group=_get_group_title(name),
                    partition=_get_partition_title(name),
                    title=title,
                    description=description,
                    source=PERM_SOURCE__DEPENDENCIES,
                )

    def _get_role_permissions(self, permission_ids):
        query = Permission.objects.filter(
            pk__in=permission_ids,
            hidden=False,
        ).values_list('name', 'title', 'description', 'hidden')

        for name, title, description, hidden in query:
            if not hidden and _get_group_name(name) in rbac.groups:
                yield dict(
                    name=name,
                    group=_get_group_title(name),
                    partition=_get_partition_title(name),
                    title=title,
                    description=description,
                    source=PERM_SOURCE__ROLE,
                )

    def run(self, request, context):
        perm_names = set()

        data = defaultdict(lambda: defaultdict(list))

        for perm_data in chain(
            self._get_role_permissions(context.role_permissions),
            self._get_dependent_permissions(context.role_permissions),
            self._get_nested_roles_permissions(get_id_value(context, Pack)),
        ):
            if perm_data['name'] not in perm_names:
                perm_names.add(perm_data['name'])

                partition_title = perm_data['partition']
                group_title = perm_data['group']

                data[partition_title][group_title].append(dict(
                    title=perm_data['title'],
                    description=perm_data['description'],
                    source=perm_data['source'],
                ))

        return PreJsonResult(data)


class ResultPermissionsPack(BasePack):

    u"""Набор действий для грида "Итоговые разрешения" окна редактирования."""

    def __init__(self):
        super(ResultPermissionsPack, self).__init__()
        # ---------------------------------------------------------------------

        self.result_permissions_action = ResultPermissionsAction()

        self.actions.extend((
            self.result_permissions_action,
        ))
        # ---------------------------------------------------------------------

        self.need_check_permission = True
        self.perm_code = PERM_GROUP__ROLE

        for action in self.actions:
            action.perm_code = 'view'
        # ---------------------------------------------------------------------

    def declare_context(self, action):
        result = super(ResultPermissionsPack, self).declare_context(action)

        if action is self.result_permissions_action:
            result[get_pack_id(Pack)] = dict(type='int_or_none', default=None)
            result['role_permissions'] = dict(type='int_list', default=())

        return result
# -----------------------------------------------------------------------------
