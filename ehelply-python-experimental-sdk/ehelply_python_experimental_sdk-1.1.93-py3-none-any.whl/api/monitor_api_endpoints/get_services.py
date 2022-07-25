# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from ehelply_python_experimental_sdk import api_client, exceptions
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

from ehelply_python_experimental_sdk.model.service_response import ServiceResponse
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError

# query params
HeartbeatsSchema = BoolSchema
HeartbeatLimitSchema = IntSchema
AlarmsSchema = BoolSchema
AlarmLimitSchema = IntSchema
IncludeHiddenSchema = BoolSchema
StageSchema = StrSchema
KeySchema = StrSchema
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'heartbeats': HeartbeatsSchema,
        'heartbeat_limit': HeartbeatLimitSchema,
        'alarms': AlarmsSchema,
        'alarm_limit': AlarmLimitSchema,
        'include_hidden': IncludeHiddenSchema,
        'stage': StageSchema,
        'key': KeySchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_heartbeats = api_client.QueryParameter(
    name="heartbeats",
    style=api_client.ParameterStyle.FORM,
    schema=HeartbeatsSchema,
    explode=True,
)
request_query_heartbeat_limit = api_client.QueryParameter(
    name="heartbeat_limit",
    style=api_client.ParameterStyle.FORM,
    schema=HeartbeatLimitSchema,
    explode=True,
)
request_query_alarms = api_client.QueryParameter(
    name="alarms",
    style=api_client.ParameterStyle.FORM,
    schema=AlarmsSchema,
    explode=True,
)
request_query_alarm_limit = api_client.QueryParameter(
    name="alarm_limit",
    style=api_client.ParameterStyle.FORM,
    schema=AlarmLimitSchema,
    explode=True,
)
request_query_include_hidden = api_client.QueryParameter(
    name="include_hidden",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeHiddenSchema,
    explode=True,
)
request_query_stage = api_client.QueryParameter(
    name="stage",
    style=api_client.ParameterStyle.FORM,
    schema=StageSchema,
    explode=True,
)
request_query_key = api_client.QueryParameter(
    name="key",
    style=api_client.ParameterStyle.FORM,
    schema=KeySchema,
    explode=True,
)
_path = '/sam/monitor/services'
_method = 'GET'


class SchemaFor200ResponseBodyApplicationJson(
    ListSchema
):

    @classmethod
    @property
    def _items(cls) -> typing.Type['ServiceResponse']:
        return ServiceResponse


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: Unset = unset
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '404': _response_for_404,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class GetServices(api_client.Api):

    def get_services(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Getservices
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        used_path = _path

        prefix_separator_iterator = None
        for parameter in (
            request_query_heartbeats,
            request_query_heartbeat_limit,
            request_query_alarms,
            request_query_alarm_limit,
            request_query_include_hidden,
            request_query_stage,
            request_query_key,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
