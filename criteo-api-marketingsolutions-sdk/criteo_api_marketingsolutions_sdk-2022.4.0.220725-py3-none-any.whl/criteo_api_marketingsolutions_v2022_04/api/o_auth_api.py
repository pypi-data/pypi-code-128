"""
    Criteo API

    Criteo publicly exposed API  # noqa: E501

    The version of the OpenAPI document: 2022-04
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from criteo_api_marketingsolutions_v2022_04.api_client import ApiClient, Endpoint as _Endpoint
from criteo_api_marketingsolutions_v2022_04.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from criteo_api_marketingsolutions_v2022_04.model.access_token_model import AccessTokenModel
from criteo_api_marketingsolutions_v2022_04.model.o_auth_error_model import OAuthErrorModel


class OAuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_token(
            self,
            grant_type,
            client_id,
            client_secret,
            **kwargs
        ):
            """Creates a token based either on supplied client credentials or on single use authorization code  # noqa: E501

            Creates a token when the supplied client credentials are valid  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_token(grant_type, client_id, client_secret, async_req=True)
            >>> result = thread.get()

            Args:
                grant_type (str):
                client_id (str):
                client_secret (str):

            Keyword Args:
                redirect_uri (str): [optional]
                code (str): [optional]
                refresh_token (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AccessTokenModel
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['grant_type'] = \
                grant_type
            kwargs['client_id'] = \
                client_id
            kwargs['client_secret'] = \
                client_secret
            return self.call_with_http_info(**kwargs)

        self.get_token = _Endpoint(
            settings={
                'response_type': (AccessTokenModel,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/oauth2/token',
                'operation_id': 'get_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'grant_type',
                    'client_id',
                    'client_secret',
                    'redirect_uri',
                    'code',
                    'refresh_token',
                ],
                'required': [
                    'grant_type',
                    'client_id',
                    'client_secret',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'grant_type':
                        (str,),
                    'client_id':
                        (str,),
                    'client_secret':
                        (str,),
                    'redirect_uri':
                        (str,),
                    'code':
                        (str,),
                    'refresh_token':
                        (str,),
                },
                'attribute_map': {
                    'grant_type': 'grant_type',
                    'client_id': 'client_id',
                    'client_secret': 'client_secret',
                    'redirect_uri': 'redirect_uri',
                    'code': 'code',
                    'refresh_token': 'refresh_token',
                },
                'location_map': {
                    'grant_type': 'form',
                    'client_id': 'form',
                    'client_secret': 'form',
                    'redirect_uri': 'form',
                    'code': 'form',
                    'refresh_token': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client,
            callable=__get_token
        )
