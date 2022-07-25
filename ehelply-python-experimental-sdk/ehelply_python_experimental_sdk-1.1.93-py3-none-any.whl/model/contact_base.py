# coding: utf-8

"""
    eHelply SDK - 1.1.93

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.93
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


class ContactBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** phones                              **type:** List[ContactKeys] or None

**:param** email                               **type:** string or None

**:param** website                             **type:** string or None

**:param** socials                             **type:** List[ContactKeys] or None
    """
    
    
    class phones(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ContactMethod']:
            return ContactMethod
    email = StrSchema
    website = StrSchema
    
    
    class socials(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ContactMethod']:
            return ContactMethod


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        phones: typing.Union[phones, Unset] = unset,
        email: typing.Union[email, Unset] = unset,
        website: typing.Union[website, Unset] = unset,
        socials: typing.Union[socials, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ContactBase':
        return super().__new__(
            cls,
            *args,
            phones=phones,
            email=email,
            website=website,
            socials=socials,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.contact_method import ContactMethod
