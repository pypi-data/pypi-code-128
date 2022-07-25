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


class ProductOptionsResponse(object):
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
        'product_options': 'list[ProductOptionResponse]',
        'pagination': 'Pagination'
    }

    attribute_map = {
        'product_options': 'product_options',
        'pagination': 'pagination'
    }

    def __init__(self, product_options=None, pagination=None, _configuration=None):  # noqa: E501
        """ProductOptionsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_options = None
        self._pagination = None
        self.discriminator = None

        if product_options is not None:
            self.product_options = product_options
        if pagination is not None:
            self.pagination = pagination

    @property
    def product_options(self):
        """Gets the product_options of this ProductOptionsResponse.  # noqa: E501


        :return: The product_options of this ProductOptionsResponse.  # noqa: E501
        :rtype: list[ProductOptionResponse]
        """
        return self._product_options

    @product_options.setter
    def product_options(self, product_options):
        """Sets the product_options of this ProductOptionsResponse.


        :param product_options: The product_options of this ProductOptionsResponse.  # noqa: E501
        :type: list[ProductOptionResponse]
        """

        self._product_options = product_options

    @property
    def pagination(self):
        """Gets the pagination of this ProductOptionsResponse.  # noqa: E501


        :return: The pagination of this ProductOptionsResponse.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ProductOptionsResponse.


        :param pagination: The pagination of this ProductOptionsResponse.  # noqa: E501
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
        if issubclass(ProductOptionsResponse, dict):
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
        if not isinstance(other, ProductOptionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductOptionsResponse):
            return True

        return self.to_dict() != other.to_dict()
