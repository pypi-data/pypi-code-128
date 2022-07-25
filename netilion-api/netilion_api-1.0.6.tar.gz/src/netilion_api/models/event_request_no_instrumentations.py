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


class EventRequestNoInstrumentations(object):
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
        'status': 'NestedID',
        'type': 'NestedID',
        'tenant': 'NestedID'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'tenant': 'tenant'
    }

    def __init__(self, status=None, type=None, tenant=None, _configuration=None):  # noqa: E501
        """EventRequestNoInstrumentations - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._type = None
        self._tenant = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if tenant is not None:
            self.tenant = tenant

    @property
    def status(self):
        """Gets the status of this EventRequestNoInstrumentations.  # noqa: E501


        :return: The status of this EventRequestNoInstrumentations.  # noqa: E501
        :rtype: NestedID
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventRequestNoInstrumentations.


        :param status: The status of this EventRequestNoInstrumentations.  # noqa: E501
        :type: NestedID
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this EventRequestNoInstrumentations.  # noqa: E501


        :return: The type of this EventRequestNoInstrumentations.  # noqa: E501
        :rtype: NestedID
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventRequestNoInstrumentations.


        :param type: The type of this EventRequestNoInstrumentations.  # noqa: E501
        :type: NestedID
        """

        self._type = type

    @property
    def tenant(self):
        """Gets the tenant of this EventRequestNoInstrumentations.  # noqa: E501


        :return: The tenant of this EventRequestNoInstrumentations.  # noqa: E501
        :rtype: NestedID
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this EventRequestNoInstrumentations.


        :param tenant: The tenant of this EventRequestNoInstrumentations.  # noqa: E501
        :type: NestedID
        """

        self._tenant = tenant

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
        if issubclass(EventRequestNoInstrumentations, dict):
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
        if not isinstance(other, EventRequestNoInstrumentations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventRequestNoInstrumentations):
            return True

        return self.to_dict() != other.to_dict()
