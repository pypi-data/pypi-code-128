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


class ProductBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'price',
        'quantity_for_public',
    ))
    meta_data = DictSchema
    collection_uuid = StrSchema
    review_group_uuid = StrSchema
    
    
    class addons(
        ListSchema
    ):
        _items = StrSchema
    name = StrSchema
    price = IntSchema
    quantity_for_public = IntSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        price: price,
        quantity_for_public: quantity_for_public,
        meta_data: typing.Union[meta_data, Unset] = unset,
        collection_uuid: typing.Union[collection_uuid, Unset] = unset,
        review_group_uuid: typing.Union[review_group_uuid, Unset] = unset,
        addons: typing.Union[addons, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ProductBase':
        return super().__new__(
            cls,
            *args,
            price=price,
            quantity_for_public=quantity_for_public,
            meta_data=meta_data,
            collection_uuid=collection_uuid,
            review_group_uuid=review_group_uuid,
            addons=addons,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
