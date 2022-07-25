import copy
import inspect
from functools import (
    lru_cache,
)
from itertools import (
    chain,
)
from typing import (
    Any,
    Dict,
    List,
)

from django.apps import (
    apps,
)
from django.core.exceptions import (
    FieldError,
    MultipleObjectsReturned,
    ObjectDoesNotExist,
)
from django.db.models import (
    NOT_PROVIDED,
    CharField,
    Model,
    PositiveIntegerField,
)
from django.db.models.base import (
    ModelBase,
    subclass_exception,
)
from django.db.models.deletion import (
    CASCADE,
)
from django.db.models.fields.related import (
    OneToOneField,
    resolve_relation,
)
from django.db.models.utils import (
    make_model_tuple,
)
from django.utils.functional import (
    cached_property,
)

from m3_db_utils.consts import (
    DEFAULT_ORDER_NUMBER,
    KEY_FIELD_NAME,
    ORDER_NUMBER_FIELD_NAME,
)
from m3_db_utils.exceptions import (
    RequiredFieldEmptyModelEnumValueError,
)
from m3_db_utils.mixins import (
    CharValueMixin,
    IntegerValueMixin,
    TitleFieldMixin,
)
from m3_db_utils.options import (
    ModelEnumOptions,
)
from m3_db_utils.strings import (
    EXTEND_NON_EXTENSIBLE_MODEL_ENUMERATION_ERROR,
)


# TODO EDUSCHL-14355  Функция перенесена из Django 2.2 в угоду совместимости с Django 1.11 используемой на текущий
#  момент в ОБР. Стоит выпилить после повышения версии Django в ОБР
def _has_contribute_to_class(value):
    # Only call contribute_to_class() if it's bound.
    return not inspect.isclass(value) and hasattr(value, 'contribute_to_class')


class ModelEnumValue:
    """
    Значение модели-перечисления.

    Универсальная сущность, которая используется в качестве значений параметров класса модели-перечисления наследника
    m3_db_utils.models.ModelEnum. Должны быть заполнены поля, обозначенные в моделе, как обязательные. Иначе не будет
    возможности записать значения в базу данных. Часть полей значения модели-перечисления может не иметь необходимости
    записи в БД. Для этого в моделе не нужно создавать одноименных полей.

    Ключ записи заполняется при инициализации класса модели именем параметра класса модели-перечисления. Это позволяет
    избежать дублирования имен и использования в коде и базе одинакового идентификатора, что упростит задачу при
    рефакторинге, т.к. ссылка на модель-перечисление - это внешний ключ и изменение значений будет означать создание
    миграции с прохождением всех моделей, ссылающихся на модель-перечисление и замену старого значения на новое.
    """

    def __init__(self, key=None, order_number=None, **kwargs):
        """
        Args:
            key: ключ, выступает значением первичного ключа. Заполняется при инициализации класса модели-перечисления
                именем переменной класса модели-перечисления
            order_number: порядковый номер значения модели-перечисления используемый в сортировке значений
                модели-перечисления
            kwargs: в именованных параметрах передаются параметры значения перечисления. В моделе должны быть поля, с
                соответствующими названиями и типами. Если будут переданы значения, выходящие за рамки полей модели,
                они будут сохранены в значении модели-перечисления, но в базу данных не будут записаны. При сохранении
                значений в базу данных будут браться значения полей
        """
        self._required_fields = [KEY_FIELD_NAME, ORDER_NUMBER_FIELD_NAME]
        self._fields = [*kwargs.keys(), *self._required_fields]

        self._key = key

        kwargs[ORDER_NUMBER_FIELD_NAME] = order_number

        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)

    @property
    def key(self) -> str:
        """
        Возвращает ключ.
        """
        return self._key

    @key.setter
    def key(self, v):
        """
        Устанавливает ключ.
        """
        self._key = v

    @property
    def fields(self) -> List[str]:
        """
        Возвращает список полей значения модели-перечисления.
        """
        return self._fields

    def set_field_value(self, field_name: str, field_value: Any, force: bool = False):
        """
        Установка значения поля.

        Args:
            field_name: имя поля
            field_value: значение поля
            force: установить значение, даже если оно уже было установлено ранее
        """
        if hasattr(self, field_name) and (getattr(self, field_name) is None or force):
            setattr(self, field_name, field_value)

    def set_required_field(self, field_name):
        """
        Установка обязательности поля в значении модели-перечисления.
        """
        if getattr(self, field_name, None) is None:
            raise RequiredFieldEmptyModelEnumValueError

        self._required_fields.append(field_name)

    @cached_property
    def required_fields(self):
        """
        Возвращает список обязательных для заполнения полей значения модели-перечисления.
        """
        return self._required_fields

    @cached_property
    def required_fields_without_key(self):
        """
        Возвращает список обязательных для заполнения полей значения модели-перечисления без поля key.
        """
        required_fields = copy.deepcopy(self.required_fields)
        required_fields.remove(KEY_FIELD_NAME)

        return required_fields


class ModelEnumMetaclass(ModelBase):
    """
    Метакласс для моделей-перечислений с переопределенным набором параметров в Meta. Поведение достигается путем замены
    стандартного Options на кастомный.
    """

    # TODO BOBUH-19054
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super(ModelBase, cls).__new__

        # Also ensure initialization is only performed for subclasses of Model
        # (excluding Model class itself).
        parents = [b for b in bases if isinstance(b, ModelBase)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        # Create the class.
        module = attrs.pop('__module__')
        new_attrs = {'__module__': module}
        classcell = attrs.pop('__classcell__', None)
        if classcell is not None:
            new_attrs['__classcell__'] = classcell
        attr_meta = attrs.pop('Meta', None)

        cls._patch_model_enum_values(attrs=attrs)

        # Pass all attrs without a (Django-specific) contribute_to_class()
        # method to type.__new__() so that they're properly initialized
        # (i.e. __set_name__()).
        contributable_attrs = {}
        for obj_name, obj in list(attrs.items()):
            if _has_contribute_to_class(obj):
                contributable_attrs[obj_name] = obj
            else:
                new_attrs[obj_name] = obj
        new_class = super_new(cls, name, bases, new_attrs, **kwargs)

        abstract = getattr(attr_meta, 'abstract', False)
        meta = attr_meta or getattr(new_class, 'Meta', None)
        base_meta = getattr(new_class, '_meta', None)

        app_label = None

        # Look for an application configuration to attach the model to.
        app_config = apps.get_containing_app_config(module)

        if getattr(meta, 'app_label', None) is None:
            if app_config is None:
                if not abstract:
                    raise RuntimeError(
                        "Model class %s.%s doesn't declare an explicit "
                        "app_label and isn't in an application in "
                        "INSTALLED_APPS." % (module, name)
                    )

            else:
                app_label = app_config.label

        # Options был заменен на ModelEnumOptions для добавления дополнительных параметров в Meta
        new_class.add_to_class('_meta', ModelEnumOptions(meta, app_label))

        if not abstract:
            new_class.add_to_class(
                'DoesNotExist',
                subclass_exception(
                    'DoesNotExist',
                    tuple(
                        x.DoesNotExist for x in parents if hasattr(x, '_meta') and not x._meta.abstract
                    ) or (ObjectDoesNotExist,),
                    module,
                    attached_to=new_class))
            new_class.add_to_class(
                'MultipleObjectsReturned',
                subclass_exception(
                    'MultipleObjectsReturned',
                    tuple(
                        x.MultipleObjectsReturned for x in parents if hasattr(x, '_meta') and not x._meta.abstract
                    ) or (MultipleObjectsReturned,),
                    module,
                    attached_to=new_class))
            if base_meta and not base_meta.abstract:
                # Non-abstract child classes inherit some attributes from their
                # non-abstract parent (unless an ABC comes before it in the
                # method resolution order).
                if not hasattr(meta, 'ordering'):
                    new_class._meta.ordering = base_meta.ordering
                if not hasattr(meta, 'get_latest_by'):
                    new_class._meta.get_latest_by = base_meta.get_latest_by

        is_proxy = new_class._meta.proxy

        # If the model is a proxy, ensure that the base class
        # hasn't been swapped out.
        if is_proxy and base_meta and base_meta.swapped:
            raise TypeError("%s cannot proxy the swapped model '%s'." % (name, base_meta.swapped))

        # Add remaining attributes (those with a contribute_to_class() method)
        # to the class.
        for obj_name, obj in contributable_attrs.items():
            new_class.add_to_class(obj_name, obj)

        # All the fields of any type declared on this model
        new_fields = chain(
            new_class._meta.local_fields,
            new_class._meta.local_many_to_many,
            new_class._meta.private_fields
        )
        field_names = {f.name for f in new_fields}

        # Basic setup for proxy models.
        if is_proxy:
            base = None
            for parent in [kls for kls in parents if hasattr(kls, '_meta')]:
                if parent._meta.abstract:
                    if parent._meta.fields:
                        raise TypeError(
                            "Abstract base class containing model fields not "
                            "permitted for proxy model '%s'." % name
                        )
                    else:
                        continue
                if base is None:
                    base = parent
                elif parent._meta.concrete_model is not base._meta.concrete_model:
                    raise TypeError("Proxy model '%s' has more than one non-abstract model base class." % name)
            if base is None:
                raise TypeError("Proxy model '%s' has no non-abstract model base class." % name)
            new_class._meta.setup_proxy(base)
            new_class._meta.concrete_model = base._meta.concrete_model
        else:
            new_class._meta.concrete_model = new_class

        # Collect the parent links for multi-table inheritance.
        parent_links = {}
        for base in reversed([new_class] + parents):
            # Conceptually equivalent to `if base is Model`.
            if not hasattr(base, '_meta'):
                continue
            # Skip concrete parent classes.
            if base != new_class and not base._meta.abstract:
                continue
            # Locate OneToOneField instances.
            for field in base._meta.local_fields:
                if isinstance(field, OneToOneField):
                    related = resolve_relation(new_class, field.remote_field.model)
                    parent_links[make_model_tuple(related)] = field

        # Track fields inherited from base models.
        inherited_attributes = set()
        # Do the appropriate setup for any model parents.
        for base in new_class.mro():
            if base not in parents or not hasattr(base, '_meta'):
                # Things without _meta aren't functional models, so they're
                # uninteresting parents.
                inherited_attributes.update(base.__dict__)
                continue

            parent_fields = base._meta.local_fields + base._meta.local_many_to_many
            if not base._meta.abstract:
                # Check for clashes between locally declared fields and those
                # on the base classes.
                for field in parent_fields:
                    if field.name in field_names:
                        raise FieldError(
                            'Local field %r in class %r clashes with field of '
                            'the same name from base class %r.' % (
                                field.name,
                                name,
                                base.__name__,
                            )
                        )
                    else:
                        inherited_attributes.add(field.name)

                # Concrete classes...
                base = base._meta.concrete_model
                base_key = make_model_tuple(base)
                if base_key in parent_links:
                    field = parent_links[base_key]
                elif not is_proxy:
                    attr_name = '%s_ptr' % base._meta.model_name
                    field = OneToOneField(
                        base,
                        on_delete=CASCADE,
                        name=attr_name,
                        auto_created=True,
                        parent_link=True,
                    )

                    if attr_name in field_names:
                        raise FieldError(
                            "Auto-generated field '%s' in class %r for "
                            "parent_link to base class %r clashes with "
                            "declared field of the same name." % (
                                attr_name,
                                name,
                                base.__name__,
                            )
                        )

                    # Only add the ptr field if it's not already present;
                    # e.g. migrations will already have it specified
                    if not hasattr(new_class, attr_name):
                        new_class.add_to_class(attr_name, field)
                else:
                    field = None
                new_class._meta.parents[base] = field
            else:
                base_parents = base._meta.parents.copy()

                # Add fields from abstract base class if it wasn't overridden.
                for field in parent_fields:
                    if (field.name not in field_names and
                        field.name not in new_class.__dict__ and
                        field.name not in inherited_attributes):
                        new_field = copy.deepcopy(field)
                        new_class.add_to_class(field.name, new_field)
                        # Replace parent links defined on this base by the new
                        # field. It will be appropriately resolved if required.
                        if field.one_to_one:
                            for parent, parent_link in base_parents.items():
                                if field == parent_link:
                                    base_parents[parent] = new_field

                # Pass any non-abstract parent classes onto child.
                new_class._meta.parents.update(base_parents)

            # Inherit private fields (like GenericForeignKey) from the parent
            # class
            for field in base._meta.private_fields:
                if field.name in field_names:
                    if not base._meta.abstract:
                        raise FieldError(
                            'Local field %r in class %r clashes with field of '
                            'the same name from base class %r.' % (
                                field.name,
                                name,
                                base.__name__,
                            )
                        )
                else:
                    field = copy.deepcopy(field)
                    if not base._meta.abstract:
                        field.mti_inherited = True
                    new_class.add_to_class(field.name, field)

        # Copy indexes so that index names are unique when models extend an
        # abstract model.
        new_class._meta.indexes = [copy.deepcopy(idx) for idx in new_class._meta.indexes]

        if abstract:
            # Abstract base models can't be instantiated and don't appear in
            # the list of models for an app. We do the final setup for them a
            # little differently from normal models.
            attr_meta.abstract = False
            new_class.Meta = attr_meta
            return new_class

        new_class._prepare()
        new_class._meta.apps.register_model(new_class._meta.app_label, new_class)

        cls._patch_new_class_after_init(new_class, attrs)

        return new_class

    def __setattr__(cls, name, value):
        if isinstance(value, ModelEnumValue) and not cls._meta.extensible:
            raise RuntimeError(EXTEND_NON_EXTENSIBLE_MODEL_ENUMERATION_ERROR)

        super(ModelBase, cls).__setattr__(name, value)

    @classmethod
    def _patch_model_enum_values(cls, attrs: Dict[str, Any]):
        """
        Патчинг параметров моделей-перечислений с добавлением ключей.
        """
        for key, value in attrs.items():
            if isinstance(value, ModelEnumValue):
                value.key = key

    @staticmethod
    def _set_default_model_enum_values(new_class, attrs: Dict[str, Any]):
        """
        Установка дефолтных значений из полей модели в поля значения модели-перечисления, если значения еще не были
        заполнены.
        """
        fields_with_default_values = [
            field
            for field in new_class._meta.fields
            if getattr(field, 'default', None) is not None and getattr(field, 'default', None) != NOT_PROVIDED
        ]

        model_attrs = {}
        for class_ in new_class.__mro__:
            model_attrs.update(vars(class_))

        model_enum_values = [
            value
            for value in model_attrs.values()
            if isinstance(value, ModelEnumValue)
        ]

        for model_enum_value in model_enum_values:
            for model_field in fields_with_default_values:
                model_enum_value.set_field_value(
                    field_name=model_field.name,
                    field_value=model_field.default,
                )

    @staticmethod
    def _set_model_enum_value_required_fields(new_class, attrs: Dict[str, Any]):
        """
        Добавление обязательных для заполнения полей в значении модели-перечисления.
        """
        required_fields = []

        for field in new_class._meta.fields:
            is_blank = getattr(field, 'blank', None)
            has_default = getattr(field, 'default', None)

            if is_blank is not None and (not is_blank and (has_default is None or has_default == NOT_PROVIDED)):
                required_fields.append(field.name)

        model_attrs = {}
        for class_ in new_class.__mro__:
            model_attrs.update(vars(class_))

        for key, value in model_attrs.items():
            if isinstance(value, ModelEnumValue):
                for field_name in required_fields:
                    try:
                        value.set_required_field(field_name=field_name)
                    except RequiredFieldEmptyModelEnumValueError:
                        raise RequiredFieldEmptyModelEnumValueError(
                            f'У модели-перечисления поле "{field_name}" является обязательным. В значении свойства '
                            f'класса "{new_class.__name__}" модели-перечисления "{key}" необходимо установить значение '
                            f'для поля "{field_name}"!'
                        )

    @classmethod
    def _patch_new_class_after_init(cls, new_class, attrs: Dict[str, Any]):
        """
        Патчинг сформированного класса модели после его инициализации.
        """
        cls._set_default_model_enum_values(new_class=new_class, attrs=attrs)
        cls._set_model_enum_value_required_fields(new_class=new_class, attrs=attrs)


class ModelEnum(Model, metaclass=ModelEnumMetaclass):
    """
    Модель-перечисление.

    Предназначен для создания перечислений, которые будут храниться в базе данных. На значения перечислений можно
    ссылаться через внешний ключ. Данный подход является более удобным с точки зрения работы на уровне SQL -
    организации сортировки, фильтрации и пр. На стороне Python, работа производится как с обычным перечислением.

    При ссылке на перечисление через внешний ключ, лучше указывать on_delete=PROTECTED, т.к. при удалении значений
    перечисления явно будут возникать ошибки на уровне БД, что позволит сохранить целостность данных.

    В перечислении значения указываются в свойствах класса именуемых заглавными буквами с разделителем нижнее
    подчеркивание. Значением перечисления является именованный кортеж ModelEnumValue.

    Добавление записей в перечисление производится путем указания нового свойства и присваиванием ему значения
    m3_db_utils.models.ModelEnumValue.

    Модель-перечисление поддерживает сортировку значений для вывода пользователю в заданном порядке. Для указания
    порядка следования значений используется поле order_number. Поле будет добавлено в таблицу модели перечисления,
    т.к. логика вывода значений модели-перечисления может быть реализована и на уровне SQL. По умолчанию проставляется
    значение 1000, чтобы все значения модели-перечисления, без явно проставленного порядкового номера находились в
    конце.

    Перечисление поддерживает добавление, обновление и удаление значений перечислений.
    Актуализатор :class:`m3_db_utils.helpers.ModelEnumDBValueUpdater` по добавлению, обновлению и удалению значений
    перечисления. Запускается на сигнал post_migrate. В актуализаторе производится поиск всех моделей перечислений. Для
    каждой модели выбираются все значения из БД и собираются все значения из класса модели-перечисления.

    Далее производится сравнение значений:

    - Если key уже есть в БД, то необходимо проверить, требуется ли обновление. Если требуется, то значения обновляются
        и помещаются в список объектов на обновление;
    - Если key есть в БД, но нет в перечислении, то он был удален;
    - Если key нет в БД, но есть в значениях перечисления, то было добавлено новое значение перечисления.

    В Meta опциях появился параметр extensible. Он отвечает за возможность расширения (патчинга) класса
    модели-перечисления из плагинов. Если True, то можно, False - запрещается. Данный параметр напрямую влияет на
    отключение плагина. Если модель-перечисление расширяемая, то при отключении плагина, значения элементов перечисления
    не будут удаляться из БД при актуализации значений. Т.к. ссылка на перечисление представлена в виде внешнего ключа,
    то при попытке удаления значения из модели-перечисления, в случае использования, будет получена ошибка о
    невозможности удаления значения. В этом случае необходимо реализовать миграцию данных, которая будет заменять
    старое значение, на новое или удалять зависимые записи.
    """

    key = CharField(verbose_name='ключ', null=False, primary_key=True, db_index=True, max_length=512)

    order_number = PositiveIntegerField(verbose_name='Порядковый номер', default=DEFAULT_ORDER_NUMBER)

    class Meta:
        abstract = True

    @classmethod
    @lru_cache()
    def get_enum_data(cls) -> Dict[str, ModelEnumValue]:
        """
        Возвращает данные перечисления в виде словаря.

        Args:

        Returns:
            {
                key: ModelEnumValue,
                ...
            }
        """
        enum_data = {}

        model_dict = {}
        for class_ in cls.__mro__:
            model_dict.update(vars(class_))

        for key in filter(lambda k: k.isupper(), model_dict.keys()):
            enum_value = getattr(cls, key)

            if isinstance(enum_value, ModelEnumValue):
                enum_data[key] = enum_value

        enum_data = dict(sorted(enum_data.items(), key=lambda edi: edi[1].order_number))

        return enum_data

    @classmethod
    @lru_cache()
    def get_model_enum_values(cls) -> List[ModelEnumValue]:
        """
        Получение значений модели перечисления.
        """
        return list(cls.get_enum_data().values())

    @classmethod
    @lru_cache()
    def get_model_enum_keys(cls) -> List[str]:
        """
        Получение значений модели перечисления.
        """
        return list(cls.get_enum_data().keys())

    @classmethod
    def get_model_enum_value(cls, key: str) -> ModelEnumValue:
        """
        Возвращает значение элемента перечисления.

        Args:

        Returns:
            ModelEnumValue - значение элемента перечисления
        """
        enum_data = cls.get_enum_data()

        return enum_data[key]

    @classmethod
    def extend(cls, key, order_number=DEFAULT_ORDER_NUMBER, **kwargs):
        """
        Метод расширения модели-перечисления, например из плагина. Необходимо, чтобы сама модель-перечисление была
        расширяемой. Для этого необходимо, чтобы был установлен extensible = True в Meta.

        Args:
            key: ключ элемента перечисления, указывается заглавными буквами с разделителем нижнее подчеркивание
            order_number: порядковый номер значения модели перечисления используемый при сортировке
        """
        setattr(cls, key, ModelEnumValue(key=key, order_number=order_number, **kwargs))

    @property
    def model_enum_value(self) -> ModelEnumValue:
        """
        Получение значения модели-перечисления у экземпляра модели.
        """
        return getattr(self, self.key)


class IntegerModelEnum(ModelEnum, IntegerValueMixin):
    """
    Модель-перечисление c обязательным для заполнения целочисленным положительным полем value.
    """

    class Meta:
        abstract = True


class CharModelEnum(ModelEnum, CharValueMixin):
    """
    Модель-перечисление c обязательным для заполнения символьным полем value.
    """

    class Meta:
        abstract = True


class TitledModelEnum(ModelEnum, TitleFieldMixin):
    """
    Модель-перечисление c обязательным для заполнения текстовым полем title.
    """

    class Meta:
        abstract = True


class TitledIntegerModelEnum(IntegerModelEnum, TitleFieldMixin):
    """
    Модель-перечисление c обязательными для заполнения целочисленным положительным полем value и текстовым полем title.
    """

    class Meta:
        abstract = True


class TitledCharModelEnum(CharModelEnum, TitleFieldMixin):
    """
    Модель-перечисление c символьным полем value и текстовым полем title.
    """

    class Meta:
        abstract = True
