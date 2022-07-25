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

from ehelply_python_experimental_sdk.model.page import Page
from ehelply_python_experimental_sdk.model.http_validation_error import HTTPValidationError

# query params
ProjectUuidSchema = StrSchema
NameSchema = StrSchema
AddressLine1Schema = StrSchema
AddressLine2Schema = StrSchema
CitySchema = StrSchema
ProvinceStateSchema = StrSchema
CountrySchema = StrSchema
PostalZipCodeSchema = StrSchema
LatSchema = StrSchema
LngSchema = StrSchema
EmailSchema = StrSchema
IsPublicSchema = BoolSchema
IsDeletedSchema = BoolSchema
WithCompanySchema = BoolSchema
WithMetaSchema = BoolSchema
WithCatalogSchema = BoolSchema
WithReviewsSchema = BoolSchema
WithScheduleSchema = BoolSchema
WithCollectionSchema = BoolSchema
WithBlogSchema = BoolSchema
WithTagsSchema = BoolSchema
WithCategoriesSchema = BoolSchema
PageSchema = IntSchema
PageSizeSchema = IntSchema
SortOnSchema = StrSchema
SortDescSchema = BoolSchema
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'project_uuid': ProjectUuidSchema,
        'name': NameSchema,
        'address_line_1': AddressLine1Schema,
        'address_line_2': AddressLine2Schema,
        'city': CitySchema,
        'province_state': ProvinceStateSchema,
        'country': CountrySchema,
        'postal_zip_code': PostalZipCodeSchema,
        'lat': LatSchema,
        'lng': LngSchema,
        'email': EmailSchema,
        'is_public': IsPublicSchema,
        'is_deleted': IsDeletedSchema,
        'with_company': WithCompanySchema,
        'with_meta': WithMetaSchema,
        'with_catalog': WithCatalogSchema,
        'with_reviews': WithReviewsSchema,
        'with_schedule': WithScheduleSchema,
        'with_collection': WithCollectionSchema,
        'with_blog': WithBlogSchema,
        'with_tags': WithTagsSchema,
        'with_categories': WithCategoriesSchema,
        'page': PageSchema,
        'page_size': PageSizeSchema,
        'sort_on': SortOnSchema,
        'sort_desc': SortDescSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_project_uuid = api_client.QueryParameter(
    name="project_uuid",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectUuidSchema,
    explode=True,
)
request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_address_line_1 = api_client.QueryParameter(
    name="address_line_1",
    style=api_client.ParameterStyle.FORM,
    schema=AddressLine1Schema,
    explode=True,
)
request_query_address_line_2 = api_client.QueryParameter(
    name="address_line_2",
    style=api_client.ParameterStyle.FORM,
    schema=AddressLine2Schema,
    explode=True,
)
request_query_city = api_client.QueryParameter(
    name="city",
    style=api_client.ParameterStyle.FORM,
    schema=CitySchema,
    explode=True,
)
request_query_province_state = api_client.QueryParameter(
    name="province_state",
    style=api_client.ParameterStyle.FORM,
    schema=ProvinceStateSchema,
    explode=True,
)
request_query_country = api_client.QueryParameter(
    name="country",
    style=api_client.ParameterStyle.FORM,
    schema=CountrySchema,
    explode=True,
)
request_query_postal_zip_code = api_client.QueryParameter(
    name="postal_zip_code",
    style=api_client.ParameterStyle.FORM,
    schema=PostalZipCodeSchema,
    explode=True,
)
request_query_lat = api_client.QueryParameter(
    name="lat",
    style=api_client.ParameterStyle.FORM,
    schema=LatSchema,
    explode=True,
)
request_query_lng = api_client.QueryParameter(
    name="lng",
    style=api_client.ParameterStyle.FORM,
    schema=LngSchema,
    explode=True,
)
request_query_email = api_client.QueryParameter(
    name="email",
    style=api_client.ParameterStyle.FORM,
    schema=EmailSchema,
    explode=True,
)
request_query_is_public = api_client.QueryParameter(
    name="is_public",
    style=api_client.ParameterStyle.FORM,
    schema=IsPublicSchema,
    explode=True,
)
request_query_is_deleted = api_client.QueryParameter(
    name="is_deleted",
    style=api_client.ParameterStyle.FORM,
    schema=IsDeletedSchema,
    explode=True,
)
request_query_with_company = api_client.QueryParameter(
    name="with_company",
    style=api_client.ParameterStyle.FORM,
    schema=WithCompanySchema,
    explode=True,
)
request_query_with_meta = api_client.QueryParameter(
    name="with_meta",
    style=api_client.ParameterStyle.FORM,
    schema=WithMetaSchema,
    explode=True,
)
request_query_with_catalog = api_client.QueryParameter(
    name="with_catalog",
    style=api_client.ParameterStyle.FORM,
    schema=WithCatalogSchema,
    explode=True,
)
request_query_with_reviews = api_client.QueryParameter(
    name="with_reviews",
    style=api_client.ParameterStyle.FORM,
    schema=WithReviewsSchema,
    explode=True,
)
request_query_with_schedule = api_client.QueryParameter(
    name="with_schedule",
    style=api_client.ParameterStyle.FORM,
    schema=WithScheduleSchema,
    explode=True,
)
request_query_with_collection = api_client.QueryParameter(
    name="with_collection",
    style=api_client.ParameterStyle.FORM,
    schema=WithCollectionSchema,
    explode=True,
)
request_query_with_blog = api_client.QueryParameter(
    name="with_blog",
    style=api_client.ParameterStyle.FORM,
    schema=WithBlogSchema,
    explode=True,
)
request_query_with_tags = api_client.QueryParameter(
    name="with_tags",
    style=api_client.ParameterStyle.FORM,
    schema=WithTagsSchema,
    explode=True,
)
request_query_with_categories = api_client.QueryParameter(
    name="with_categories",
    style=api_client.ParameterStyle.FORM,
    schema=WithCategoriesSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_sort_on = api_client.QueryParameter(
    name="sort_on",
    style=api_client.ParameterStyle.FORM,
    schema=SortOnSchema,
    explode=True,
)
request_query_sort_desc = api_client.QueryParameter(
    name="sort_desc",
    style=api_client.ParameterStyle.FORM,
    schema=SortDescSchema,
    explode=True,
)
# header params
XAccessTokenSchema = StrSchema
XSecretTokenSchema = StrSchema
AuthorizationSchema = StrSchema
EhelplyActiveParticipantSchema = StrSchema
EhelplyProjectSchema = StrSchema
EhelplyDataSchema = StrSchema
RequestRequiredHeaderParams = typing.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-access-token': XAccessTokenSchema,
        'x-secret-token': XSecretTokenSchema,
        'authorization': AuthorizationSchema,
        'ehelply-active-participant': EhelplyActiveParticipantSchema,
        'ehelply-project': EhelplyProjectSchema,
        'ehelply-data': EhelplyDataSchema,
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_access_token = api_client.HeaderParameter(
    name="x-access-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAccessTokenSchema,
)
request_header_x_secret_token = api_client.HeaderParameter(
    name="x-secret-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XSecretTokenSchema,
)
request_header_authorization = api_client.HeaderParameter(
    name="authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
request_header_ehelply_active_participant = api_client.HeaderParameter(
    name="ehelply-active-participant",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyActiveParticipantSchema,
)
request_header_ehelply_project = api_client.HeaderParameter(
    name="ehelply-project",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyProjectSchema,
)
request_header_ehelply_data = api_client.HeaderParameter(
    name="ehelply-data",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyDataSchema,
)
_path = '/places/places'
_method = 'GET'
SchemaFor200ResponseBodyApplicationJson = Page


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


class SearchPlacesPlacesPlacesGet(api_client.Api):

    def search_places_places_places_get(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        header_params: RequestHeaderParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Search Places
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestHeaderParams, header_params)
        used_path = _path

        prefix_separator_iterator = None
        for parameter in (
            request_query_project_uuid,
            request_query_name,
            request_query_address_line_1,
            request_query_address_line_2,
            request_query_city,
            request_query_province_state,
            request_query_country,
            request_query_postal_zip_code,
            request_query_lat,
            request_query_lng,
            request_query_email,
            request_query_is_public,
            request_query_is_deleted,
            request_query_with_company,
            request_query_with_meta,
            request_query_with_catalog,
            request_query_with_reviews,
            request_query_with_schedule,
            request_query_with_collection,
            request_query_with_blog,
            request_query_with_tags,
            request_query_with_categories,
            request_query_page,
            request_query_page_size,
            request_query_sort_on,
            request_query_sort_desc,
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
        for parameter in (
            request_header_x_access_token,
            request_header_x_secret_token,
            request_header_authorization,
            request_header_ehelply_active_participant,
            request_header_ehelply_project,
            request_header_ehelply_data,
        ):
            parameter_data = header_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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
