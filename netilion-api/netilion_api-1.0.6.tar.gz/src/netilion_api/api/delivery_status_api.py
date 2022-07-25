# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from netilion_api.api_client import ApiClient


class DeliveryStatusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_delivery_status(self, body, **kwargs):  # noqa: E501
        """Create a new delivery status  # noqa: E501

        Code must be unique. Parameters supporting translation: ```name, description```. POST sets values in default language: en.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_delivery_status(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryStatusRequest body: DeliveryStatus object to create. (required)
        :return: DeliveryStatusRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_delivery_status_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_delivery_status_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_delivery_status_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new delivery status  # noqa: E501

        Code must be unique. Parameters supporting translation: ```name, description```. POST sets values in default language: en.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_delivery_status_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryStatusRequest body: DeliveryStatus object to create. (required)
        :return: DeliveryStatusRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_delivery_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_delivery_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/delivery/statuses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeliveryStatusRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_delivery_status(self, id, **kwargs):  # noqa: E501
        """Delete a delivery status  # noqa: E501

        Delete a specific resource identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_delivery_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the delivery status to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_delivery_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_delivery_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_delivery_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a delivery status  # noqa: E501

        Delete a specific resource identified by the id in the URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_delivery_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the delivery status to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_delivery_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_delivery_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/delivery/statuses/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delivery_id_status(self, delivery_id, **kwargs):  # noqa: E501
        """Get the status of the specific delivery  # noqa: E501

        Returns the status of the delivery. You can apply the query parameters listed below to get a filtered list. Required Permissions: ```can_read``` Parameters supporting translation: ```name, description```. To add a translation set Content-Language. Possible include value: ```tenant```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_id_status(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int delivery_id: Id of the specified delivery (required)
        :param str include: Comma separated list of objects to include in response
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delivery_id_status_with_http_info(delivery_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_delivery_id_status_with_http_info(delivery_id, **kwargs)  # noqa: E501
            return data

    def get_delivery_id_status_with_http_info(self, delivery_id, **kwargs):  # noqa: E501
        """Get the status of the specific delivery  # noqa: E501

        Returns the status of the delivery. You can apply the query parameters listed below to get a filtered list. Required Permissions: ```can_read``` Parameters supporting translation: ```name, description```. To add a translation set Content-Language. Possible include value: ```tenant```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_id_status_with_http_info(delivery_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int delivery_id: Id of the specified delivery (required)
        :param str include: Comma separated list of objects to include in response
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_id', 'include', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_id_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_id' is set
        if self.api_client.client_side_validation and ('delivery_id' not in params or
                                                       params['delivery_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `delivery_id` when calling `get_delivery_id_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_id' in params:
            path_params['delivery_id'] = params['delivery_id']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/deliveries/{delivery_id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeliveryStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delivery_status_by_id(self, id, **kwargs):  # noqa: E501
        """Get a single delivery status  # noqa: E501

        Get a specific delivery status identified by the id in the URL. Parameters supporting translation: ```name, description```. To get a translation set Accept-Language.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_status_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of delivery status to fetch (required)
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delivery_status_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_delivery_status_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_delivery_status_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a single delivery status  # noqa: E501

        Get a specific delivery status identified by the id in the URL. Parameters supporting translation: ```name, description```. To get a translation set Accept-Language.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_status_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of delivery status to fetch (required)
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_status_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_delivery_status_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/delivery/statuses/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeliveryStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delivery_statuses(self, **kwargs):  # noqa: E501
        """Get a range of delivery statuses  # noqa: E501

        Returns a list of all delivery statuses that are available in your scope. You can apply the query parameters listed below to get a filtered list. Parameters supporting translation: ```name, description```. To get a translation set Accept-Language.  Possible include value: ```tenant```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_statuses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str code: Filter accepts `*` as wildcard
        :param str name: Filter accepts `*` as wildcard
        :param str tenant_id: One or multiple ids (comma list). Expected id format is integer
        :param str order_by: Order result by attribute value, accepts `id`, `created_at` or `updated_at`. Add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatuses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delivery_statuses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_delivery_statuses_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_delivery_statuses_with_http_info(self, **kwargs):  # noqa: E501
        """Get a range of delivery statuses  # noqa: E501

        Returns a list of all delivery statuses that are available in your scope. You can apply the query parameters listed below to get a filtered list. Parameters supporting translation: ```name, description```. To get a translation set Accept-Language.  Possible include value: ```tenant```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delivery_statuses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number to load
        :param int per_page: Number of items to load per page
        :param str code: Filter accepts `*` as wildcard
        :param str name: Filter accepts `*` as wildcard
        :param str tenant_id: One or multiple ids (comma list). Expected id format is integer
        :param str order_by: Order result by attribute value, accepts `id`, `created_at` or `updated_at`. Add `-` as a prefix for descending order. Default value is `id`
        :param str accept_language: The client's accepted languages. One or several (e.g. fr,de,en)
        :return: DeliveryStatuses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'code', 'name', 'tenant_id', 'order_by', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delivery_statuses" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('per_page' in params and params['per_page'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_delivery_statuses`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('per_page' in params and params['per_page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_delivery_statuses`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'tenant_id' in params:
            query_params.append(('tenant_id', params['tenant_id']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/delivery/statuses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeliveryStatuses',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_delivery_statuses(self, id, body, **kwargs):  # noqa: E501
        """Update an delivery status  # noqa: E501

        Update accessible parameters of the requested resource. Parameters supporting translation: ```name, description```. To add a translation set Content-Language.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_delivery_statuses(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the delivery to update (required)
        :param DeliveryStatusRequest body: Parameters that shall be updated. (required)
        :param str content_language: language of the content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_delivery_statuses_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_delivery_statuses_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def update_delivery_statuses_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update an delivery status  # noqa: E501

        Update accessible parameters of the requested resource. Parameters supporting translation: ```name, description```. To add a translation set Content-Language.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_delivery_statuses_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the delivery to update (required)
        :param DeliveryStatusRequest body: Parameters that shall be updated. (required)
        :param str content_language: language of the content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_delivery_statuses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `update_delivery_statuses`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_delivery_statuses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_language' in params:
            header_params['Content-Language'] = params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key', 'Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/delivery/statuses/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
