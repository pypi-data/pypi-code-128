# coding: utf-8

"""
    eHelply SDK - 1.1.92

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.92
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from ehelply_python_experimental_sdk.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class Field(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Field
    """
    uuid = StrSchema
    type = IntSchema
    placeholder = StrSchema

    @classmethod
    @property
    def validations(cls) -> typing.Type['Validations']:
        return Validations
    hint = StrSchema
    icon = StrSchema
    label = StrSchema

    @classmethod
    @property
    def options(cls) -> typing.Type['Options']:
        return Options


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: typing.Union[uuid, Unset] = unset,
        type: typing.Union[type, Unset] = unset,
        placeholder: typing.Union[placeholder, Unset] = unset,
        validations: typing.Union['Validations', Unset] = unset,
        hint: typing.Union[hint, Unset] = unset,
        icon: typing.Union[icon, Unset] = unset,
        label: typing.Union[label, Unset] = unset,
        options: typing.Union['Options', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Field':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            type=type,
            placeholder=placeholder,
            validations=validations,
            hint=hint,
            icon=icon,
            label=label,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.options import Options
from ehelply_python_experimental_sdk.model.validations import Validations
