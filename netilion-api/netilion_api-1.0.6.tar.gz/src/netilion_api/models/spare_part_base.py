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


class SparePartBase(object):
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
        'order_code': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'order_code': 'order_code',
        'name': 'name',
        'description': 'description'
    }

    discriminator_value_class_map = {
        'SparePartRequest': 'SparePartRequest',
        'SparePartStatusResponse': 'SparePartStatusResponse',
        'SparePartResponse': 'SparePartResponse'
    }

    def __init__(self, order_code=None, name=None, description=None, _configuration=None):  # noqa: E501
        """SparePartBase - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._order_code = None
        self._name = None
        self._description = None
        self.discriminator = 'sparePartBaseType'

        if order_code is not None:
            self.order_code = order_code
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def order_code(self):
        """Gets the order_code of this SparePartBase.  # noqa: E501

        order code of the spare part, must be unique within the tenant scope. Whitespaces are trimmed.  # noqa: E501

        :return: The order_code of this SparePartBase.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this SparePartBase.

        order code of the spare part, must be unique within the tenant scope. Whitespaces are trimmed.  # noqa: E501

        :param order_code: The order_code of this SparePartBase.  # noqa: E501
        :type: str
        """

        self._order_code = order_code

    @property
    def name(self):
        """Gets the name of this SparePartBase.  # noqa: E501

        Supports translations.  # noqa: E501

        :return: The name of this SparePartBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SparePartBase.

        Supports translations.  # noqa: E501

        :param name: The name of this SparePartBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SparePartBase.  # noqa: E501

        Supports translations.  # noqa: E501

        :return: The description of this SparePartBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SparePartBase.

        Supports translations.  # noqa: E501

        :param description: The description of this SparePartBase.  # noqa: E501
        :type: str
        """

        self._description = description

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(SparePartBase, dict):
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
        if not isinstance(other, SparePartBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SparePartBase):
            return True

        return self.to_dict() != other.to_dict()
