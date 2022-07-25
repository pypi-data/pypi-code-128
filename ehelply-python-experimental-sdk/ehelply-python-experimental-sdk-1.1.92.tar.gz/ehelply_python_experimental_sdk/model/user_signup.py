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


class UserSignup(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    User information used for user signup
    """
    _required_property_names = set((
        'username',
        'password',
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'country',
    ))
    username = StrSchema
    password = StrSchema
    email = StrSchema
    first_name = StrSchema
    last_name = StrSchema
    phone_number = StrSchema
    country = StrSchema
    lat = StrSchema
    lng = StrSchema
    verified_legal_terms = BoolSchema
    picture = StrSchema
    newsletters = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        username: username,
        password: password,
        email: email,
        first_name: first_name,
        last_name: last_name,
        phone_number: phone_number,
        country: country,
        lat: typing.Union[lat, Unset] = unset,
        lng: typing.Union[lng, Unset] = unset,
        verified_legal_terms: typing.Union[verified_legal_terms, Unset] = unset,
        picture: typing.Union[picture, Unset] = unset,
        newsletters: typing.Union[newsletters, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'UserSignup':
        return super().__new__(
            cls,
            *args,
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            country=country,
            lat=lat,
            lng=lng,
            verified_legal_terms=verified_legal_terms,
            picture=picture,
            newsletters=newsletters,
            _configuration=_configuration,
            **kwargs,
        )
