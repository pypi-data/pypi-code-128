# coding: utf-8
from __future__ import absolute_import

import hashlib

from six import text_type

from educommon import Undefined


class cached_property(property):

    u"""Кешируемое свойство.

    В отличие от :class:`django.utils.functional.cached_property`, наследуется
    от property и копирует строку документации, что актуально при генерации
    документации средствами Sphinx.
    """

    def __init__(self, method):
        super(cached_property, self).__init__(method)

        self.__doc__ = method.__doc__

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.fget.__name__ not in instance.__dict__:
            instance.__dict__[self.fget.__name__] = self.fget(instance)

        return instance.__dict__[self.fget.__name__]


def get_nested_attr(obj, attr, default=Undefined):
    u"""Возвращает значение вложенного атрибута объекта.

    .. code-block:: python

       obj = datetime(2015, 1, 1, 0, 0, 0)
       get_nested_attr(obj, 'date().year')  # 2015
       get_nested_attr(obj, 'date().year.__class__')  # int
    """
    attributes = attr.split('.')

    nested_attribute = ''
    nested_object = obj
    for name in attributes:
        if nested_attribute:
            nested_attribute += '.'
        nested_attribute += name

        if name.endswith('()'):
            callable_attribute = True
            name = name[:-2]
        else:
            callable_attribute = False

        try:
            nested_object = getattr(nested_object, name)
            if callable_attribute:
                assert callable(nested_object), (name, nested_object)
                nested_object = nested_object()
        except AttributeError:
            if default is not Undefined:
                return default
            else:
                raise AttributeError(
                    "'{}' object has no attribute '{}'".format(
                        type(obj), nested_attribute
                    )
                )

    return nested_object


def md5sum(filepath):
    u"""Возвращает контрольную сумму MD5 указанного файла.

    :param basestring filepath: Путь к файлу.

    :rtype: str
    """
    md5 = hashlib.md5()
    with open(filepath, 'r') as infile:
        while True:
            data = infile.read(1024)
            if not data:
                break
            if isinstance(data, text_type):
                data = data.encode('utf-8')
            md5.update(data)
    return md5.hexdigest()


class NoOperationCM(object):

    """Менеджер контекта, не выполняющий никаких действий."""

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_inst, traceback):
        pass


def get_mime_type_for_extension(extension):
    """Возвращает mimetype для расширения файла.

    :param extension: Расширение файла в вида '.название_расширения'
    :type extension: str
    :return: Название mimetype
    :rtype: str
    """
    import mimetypes
    mimetypes.init()
    if not extension.startswith('.'):
        extension = '.%s' % extension
    return mimetypes.types_map.get(extension.lower())
