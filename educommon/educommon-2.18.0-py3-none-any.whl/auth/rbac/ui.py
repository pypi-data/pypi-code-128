# coding: utf-8
# pylint: disable=attribute-defined-outside-init, no-member
from __future__ import absolute_import

import json

from django.utils.safestring import mark_safe
from m3.actions.context import ActionContext
from m3_ext.ui.containers.containers import ExtContainer
from m3_ext.ui.containers.containers import ExtToolbarMenu
from m3_ext.ui.containers.context_menu import ExtContextMenu
from m3_ext.ui.containers.forms import ExtPanel
from m3_ext.ui.containers.grids import ExtGridCheckBoxSelModel
from m3_ext.ui.containers.trees import ExtTree
from m3_ext.ui.fields import ExtMultiSelectField
from m3_ext.ui.icons import Icons
from m3_ext.ui.menus import ExtContextMenuItem
from m3_ext.ui.misc import ExtDataStore
from m3_ext.ui.misc.label import ExtLabel
from m3_ext.ui.panels.grids import ExtObjectGrid
from objectpack.tree_object_pack.ui import BaseObjectTree
from objectpack.tree_object_pack.ui import BaseTreeSelectWindow
from objectpack.ui import BaseListWindow
from objectpack.ui import ColumnsConstructor
from objectpack.ui import ObjectTab
from objectpack.ui import WindowTab

from educommon import ioc
from educommon.auth.rbac.constants import PERM_SOURCES
from educommon.objectpack.ui import ModelEditWindow
from educommon.objectpack.ui import TabbedEditWindow
from educommon.utils.ui import switch_window_in_read_only_mode

from .models import Role


class RolesTree(BaseObjectTree):

    u"""Грид для отображения иерархии ролей.

    Отличается от обычного грида для отображения деревьев тем, что помимо
    кнопок "Новый в корне" и "Новый дочерний" имеет кнопку "Добавить в роль".
    """

    def __init__(self, *args, **kwargs):
        super(RolesTree, self).__init__(*args, **kwargs)

        # Меню "Добавить"
        self.top_bar.button_add_to_role = ExtContextMenuItem(
            text=u'Добавить в роль',
            icon_cls='add_item',
            handler='topBarAddToRole',
        )
        self.top_bar.add_menu.menu.items.append(
            self.top_bar.button_add_to_role
        )

        # Меню "Удалить"
        self.top_bar.items.remove(self.top_bar.button_delete)
        self.top_bar.button_delete_from_role = ExtContextMenuItem(
            text=u'Удалить из роли',
            icon_cls='delete_item',
            handler='topBarDeleteFromRole',
        )
        self.top_bar.button_delete = ExtContextMenuItem(
            text=u'Удалить из системы',
            icon_cls='delete_item',
            handler='topBarDelete',
        )

        menu = ExtContextMenu()
        menu.items.extend((
            self.top_bar.button_delete_from_role,
            self.top_bar.button_delete,
        ))
        self.top_bar.delete_menu = ExtToolbarMenu(
            icon_cls="delete_item",
            menu=menu,
            text=u'Удалить'
        )
        self.top_bar.items.append(self.top_bar.delete_menu)

        # Передаем индексы, так как некорректно
        # формируется client_id для данных элементов.
        self.add_menu_index = self.top_bar.items.index(
            self.top_bar.add_menu
        )
        self.new_child_index = self.top_bar.add_menu.menu.items.index(
            self.top_bar.button_new_child
        )
        self.add_to_role_index = self.top_bar.add_menu.menu.items.index(
            self.top_bar.button_add_to_role
        )
        self.delete_menu_index = self.top_bar.items.index(
            self.top_bar.delete_menu
        )
        self.delete_from_role_index = menu.items.index(
            self.top_bar.button_delete_from_role
        )


class RolesListWindow(BaseListWindow):

    u"""Окно для отображения иерархии ролей."""

    def _init_components(self):
        super(RolesListWindow, self)._init_components()

        self.grid = RolesTree()

    def set_params(self, params):
        super(RolesListWindow, self).set_params(params)
        template = 'rbac/roles-list-window.js'
        self.pack = params['pack']
        # ---------------------------------------------------------------------
        # Включение/отключение элементов окна в зависимости от прав доступа
        if not params['can_edit']:
            template = 'rbac/roles-view-list-window.js'
            # Отключение контролов для добавления ролей
            self.grid.action_new = None

            # Отключение контролов для изменения ролей
            for control in (
                self.grid.top_bar.button_edit,
                self.grid.context_menu_row.menuitem_edit
            ):
                control.text = u'Просмотр'
                control.icon_cls = Icons.APPLICATION_VIEW_DETAIL

            # Изменение контролов для удаления ролей
            self.grid.action_delete = None
            self.grid.url_delete = None
            self.grid.top_bar.items.remove(self.grid.top_bar.delete_menu)
        # ---------------------------------------------------------------------
        self.template_globals = template


class RoleSelectWindow(BaseTreeSelectWindow):

    u"""Окно выбора роли, в которую будет добавлена указанная роль."""

    def _init_components(self):
        super(RoleSelectWindow, self)._init_components()

        self.label_message = ExtLabel(
            text=u'Выберите роль, в которую будет добавлена роль "{}":',
            style={'padding': '5px'},
            region='north',
        )

    def _do_layout(self):
        super(RoleSelectWindow, self)._do_layout()

        self.layout = 'border'

        self.items.insert(0, self.label_message)

    def set_params(self, params):
        super(RoleSelectWindow, self).set_params(params)

        self.title = u'Добавление одной роли в другую'

        self.grid.region = 'center'
        self.grid.action_new = None
        self.grid.action_edit = None
        self.grid.action_delete = None

        if self.grid.action_context is None:
            self.grid.action_context = ActionContext()
        self.grid.action_context.role_id = params['role'].id

        self.label_message.text = (
            mark_safe(self.label_message.text.format(params['role'].name))
        )
# -----------------------------------------------------------------------------


def _make_user_type_field(name='user_type_ids', **kwargs):
    field = ExtMultiSelectField(
        label=u'Может быть назначена',
        anchor='100%',
        hide_edit_trigger=False,
        hide_trigger=False,
        hide_dict_select_trigger=False,
        **kwargs
    )
    field.name = name

    return field


class PermissionsChangeTab(ObjectTab):

    u"""Вкладка "Разрешения роли" окна редактирования роли.

    Содержит элементы интерфейса для изменения параметров роли: названия,
    текстового описания, перечня разрешений и т.д.
    """

    title = u'Разрешения роли'

    model = Role

    field_fabric_params = dict(
        field_list=('name', 'description', 'can_be_assigned'),
    )

    def init_components(self, win):
        super(PermissionsChangeTab, self).init_components(win)

        self.field__user_types = _make_user_type_field()
        self.container__top = ExtPanel(
            body_cls='x-window-mc',
            border=False,
        )
        self.grid__partitions = ExtObjectGrid()
        self.grid__partitions.top_bar.hidden = True
        self.container__right = ExtContainer()

        self.grid__permissions = ExtObjectGrid()
        self.grid__permissions.top_bar.hidden = True
        self.grid__permissions.store.auto_load = False

        self.panel__description = ExtPanel(
            header=True,
            padding=5,
            title=u'Описание разрешения',
        )

    def do_layout(self, win, tab):
        super(PermissionsChangeTab, self).do_layout(win, tab)

        tab.border = False
        # ---------------------------------------------------------------------

        win.tab__permissions_change = tab
        win.field__name = self.field__name
        win.field__description = self.field__description
        win.field__can_be_assigned = self.field__can_be_assigned
        win.field__user_types = self.field__user_types
        win.grid__partitions = self.grid__partitions
        win.container__right = self.container__right
        win.grid__permissions = self.grid__permissions
        win.panel__description = self.panel__description
        # ---------------------------------------------------------------------

        self.container__top.items[:] = (
            self.field__name,
            self.field__description,
            self.field__can_be_assigned,
        )
        self.container__right.items[:] = (
            self.grid__permissions,
            self.panel__description,
        )
        tab.items[:] = (
            self.container__top,
            self.grid__partitions,
            self.container__right,
        )
        # ---------------------------------------------------------------------

        tab.layout = 'border'
        self.container__top.region = 'north'
        self.container__top.height = 130
        self.grid__partitions.region = 'west'
        self.grid__partitions.width = '20%'
        self.container__right.region = 'center'
        self.container__right.width = '80%'

        self.container__top.layout = 'form'
        self.container__top.label_width = 60
        self.container__top.padding = 5

        self.container__right.layout = 'vbox'
        self.container__right.layout_config = {
            'align': 'stretch',
        }
        self.panel__description.flex = 0
        self.panel__description.height = 100
        self.grid__permissions.flex = 1
        # ---------------------------------------------------------------------

    def set_params(self, win, params):
        super(PermissionsChangeTab, self).set_params(win, params)

        if params.get('show_user_types', False):
            self.container__top.height += 45
            self.container__top.label_width = 140
            self.container__top.items.append(self.field__user_types)

            self.field__user_types.set_store(
                ExtDataStore(data=params['user_types'])
            )
            self.field__user_types.value = params.get('user_type_ids', ())

        if params['can_edit']:
            self.grid__permissions.sm = ExtGridCheckBoxSelModel(
                check_only=True,
            )

        params['partitions_pack'].configure_grid(self.grid__partitions)
        params['permissions_pack'].configure_grid(self.grid__permissions)


class ResultPermissionsTree(ExtTree):

    u"""Панель для отображения итоговых разрешений в виде дерева.

    В дереве отображается три уровня: разделы, группы и сами разрешения.
    """

    def __init__(self, *args, **kwargs):
        super(ResultPermissionsTree, self).__init__()

        ColumnsConstructor.from_config((
            dict(
                data_index='title',
                header=u'Наименование',
            ),
            dict(
                data_index='description',
                hidden=True,
            ),
            dict(
                data_index=u'source',
                header=u'Источник',
            ),
        )).configure_grid(self)


class ResultPermissionsTab(WindowTab):

    u"""Вкладка "Итоговые разрешения" окна редактирования роли.

    Предназначена для отображения результирующего набора разрешений, которые
    предоставляет роль. В этот набор входят:

        - разрешения, добавленные в роль;
        - разрешения, зависящие тех, которые добавлены в роль;
        - разрешения вложенных ролей.

    Для каждого разрешения указывается источник: сама роль, зависимое
    разрешение или вложенная роль.
    """

    title = u'Итоговые разрешения'

    def init_components(self, win):
        super(ResultPermissionsTab, self).init_components(win)

        self.tree__result_permissions = ResultPermissionsTree()

        self.panel__description = ExtPanel(
            header=True,
            padding=5,
            title=u'Описание разрешения',
        )

    def do_layout(self, win, tab):
        super(ResultPermissionsTab, self).do_layout(win, tab)
        # ---------------------------------------------------------------------

        win.tab__result_permissions = tab
        tab.tree__result_permissions = self.tree__result_permissions
        tab.panel__description = self.panel__description

        tab.items.extend((
            self.tree__result_permissions,
            self.panel__description,
        ))
        # ---------------------------------------------------------------------

        tab.layout = 'vbox'
        tab.layout_config = dict(
            align='stretch',
        )
        self.tree__result_permissions.flex = 1
        self.panel__description.flex = 0
        self.panel__description.height = 100
        # ---------------------------------------------------------------------


class RoleAddWindow(ModelEditWindow):

    u"""Окно добавления роли."""

    model = Role

    field_fabric_params = dict(
        field_list=('name', 'description', 'can_be_assigned'),
        model_register=ioc.get('observer'),
    )

    def _init_components(self):
        super(RoleAddWindow, self)._init_components()
        self.field__user_types = _make_user_type_field()

    def _do_layout(self):
        super(RoleAddWindow, self)._do_layout()
        self.form.items.append(self.field__user_types)

    def set_params(self, params):
        super(RoleAddWindow, self).set_params(params)

        self.template_globals = 'rbac/role-add-window.js'

        if params.get('show_user_types', False):
            self.field__user_types.set_store(
                ExtDataStore(data=params['user_types'])
            )


class RoleEditWindow(TabbedEditWindow):

    u"""Окно редактирования роли."""

    model = Role

    tabs = (
        PermissionsChangeTab,
        ResultPermissionsTab,
    )

    def set_params(self, params):
        super(RoleEditWindow, self).set_params(params)

        self.width = 1100
        self.height = 700

        self.template_globals = 'rbac/role-edit-window.js'

        self.id_param_name = params['roles_pack']
        self.role = params['object']
        self.roles_pack = params['roles_pack']
        self.perm_sources = PERM_SOURCES
        self.permission_ids = params['permission_ids']
        self.can_edit = json.dumps(params['can_edit'])
        self.result_action_url = params['result_action_url']

        if not params['can_edit']:
            switch_window_in_read_only_mode(self)
# -----------------------------------------------------------------------------
