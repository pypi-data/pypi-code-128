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


class CompanyBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** name                                **type:** string
**:param** summary                             **type:** string or None

**:param** public                              **type:** bool or None

**:param** meta                                **type:** dict or None

**:param** contact                             **type:** ContactBase or None
    """
    name = StrSchema
    summary = StrSchema
    public = BoolSchema
    meta = DictSchema

    @classmethod
    @property
    def contact(cls) -> typing.Type['ContactBase']:
        return ContactBase


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: typing.Union[name, Unset] = unset,
        summary: typing.Union[summary, Unset] = unset,
        public: typing.Union[public, Unset] = unset,
        meta: typing.Union[meta, Unset] = unset,
        contact: typing.Union['ContactBase', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CompanyBase':
        return super().__new__(
            cls,
            *args,
            name=name,
            summary=summary,
            public=public,
            meta=meta,
            contact=contact,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.contact_base import ContactBase
