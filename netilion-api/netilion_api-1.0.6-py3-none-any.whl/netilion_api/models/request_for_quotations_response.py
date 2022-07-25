# coding: utf-8

"""
    Netilion API Documentation

    Welcome to the Netilion API Documentation, which provides interactive access and documentation to our REST API. Please visit our developer portal for further instructions and information: https://developer.netilion.endress.com/   # noqa: E501

    OpenAPI spec version: 01.00.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from netilion_api.configuration import Configuration


class RequestForQuotationsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_for_quotations': 'list[RequestForQuotationResponse]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'request_for_quotations': 'request_for_quotations',
        'pagination': 'pagination'
    }

    def __init__(self, request_for_quotations=None, pagination=None, _configuration=None):  # noqa: E501
        """RequestForQuotationsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_for_quotations = None
        self._pagination = None
        self.discriminator = None

        if request_for_quotations is not None:
            self.request_for_quotations = request_for_quotations
        if pagination is not None:
            self.pagination = pagination

    @property
    def request_for_quotations(self):
        """Gets the request_for_quotations of this RequestForQuotationsResponse.  # noqa: E501


        :return: The request_for_quotations of this RequestForQuotationsResponse.  # noqa: E501
        :rtype: list[RequestForQuotationResponse]
        """
        return self._request_for_quotations

    @request_for_quotations.setter
    def request_for_quotations(self, request_for_quotations):
        """Sets the request_for_quotations of this RequestForQuotationsResponse.


        :param request_for_quotations: The request_for_quotations of this RequestForQuotationsResponse.  # noqa: E501
        :type: list[RequestForQuotationResponse]
        """

        self._request_for_quotations = request_for_quotations

    @property
    def pagination(self):
        """Gets the pagination of this RequestForQuotationsResponse.  # noqa: E501


        :return: The pagination of this RequestForQuotationsResponse.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this RequestForQuotationsResponse.


        :param pagination: The pagination of this RequestForQuotationsResponse.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RequestForQuotationsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestForQuotationsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestForQuotationsResponse):
            return True

        return self.to_dict() != other.to_dict()
