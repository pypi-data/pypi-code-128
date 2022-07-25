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


class ProjectsUsageTypeUpdate(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Used for update endpoint
    """
    name = StrSchema
    summary = StrSchema
    category = StrSchema
    service = StrSchema
    
    
    class unit_prices(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['ProjectsUsageTypeUnitPrice']:
            return ProjectsUsageTypeUnitPrice


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: typing.Union[name, Unset] = unset,
        summary: typing.Union[summary, Unset] = unset,
        category: typing.Union[category, Unset] = unset,
        service: typing.Union[service, Unset] = unset,
        unit_prices: typing.Union[unit_prices, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ProjectsUsageTypeUpdate':
        return super().__new__(
            cls,
            *args,
            name=name,
            summary=summary,
            category=category,
            service=service,
            unit_prices=unit_prices,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_experimental_sdk.model.projects_usage_type_unit_price import ProjectsUsageTypeUnitPrice
