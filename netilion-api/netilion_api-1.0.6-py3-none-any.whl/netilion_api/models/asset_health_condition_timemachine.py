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


class AssetHealthConditionTimemachine(object):
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
        'health_condition': 'AssetHealthConditionNested',
        'created_datetime': 'datetime',
        'deleted_datetime': 'datetime'
    }

    attribute_map = {
        'health_condition': 'health_condition',
        'created_datetime': 'created_datetime',
        'deleted_datetime': 'deleted_datetime'
    }

    def __init__(self, health_condition=None, created_datetime=None, deleted_datetime=None, _configuration=None):  # noqa: E501
        """AssetHealthConditionTimemachine - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._health_condition = None
        self._created_datetime = None
        self._deleted_datetime = None
        self.discriminator = None

        self.health_condition = health_condition
        self.created_datetime = created_datetime
        self.deleted_datetime = deleted_datetime

    @property
    def health_condition(self):
        """Gets the health_condition of this AssetHealthConditionTimemachine.  # noqa: E501


        :return: The health_condition of this AssetHealthConditionTimemachine.  # noqa: E501
        :rtype: AssetHealthConditionNested
        """
        return self._health_condition

    @health_condition.setter
    def health_condition(self, health_condition):
        """Sets the health_condition of this AssetHealthConditionTimemachine.


        :param health_condition: The health_condition of this AssetHealthConditionTimemachine.  # noqa: E501
        :type: AssetHealthConditionNested
        """
        if self._configuration.client_side_validation and health_condition is None:
            raise ValueError("Invalid value for `health_condition`, must not be `None`")  # noqa: E501

        self._health_condition = health_condition

    @property
    def created_datetime(self):
        """Gets the created_datetime of this AssetHealthConditionTimemachine.  # noqa: E501

        Date of the Create Event  # noqa: E501

        :return: The created_datetime of this AssetHealthConditionTimemachine.  # noqa: E501
        :rtype: datetime
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this AssetHealthConditionTimemachine.

        Date of the Create Event  # noqa: E501

        :param created_datetime: The created_datetime of this AssetHealthConditionTimemachine.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and created_datetime is None:
            raise ValueError("Invalid value for `created_datetime`, must not be `None`")  # noqa: E501

        self._created_datetime = created_datetime

    @property
    def deleted_datetime(self):
        """Gets the deleted_datetime of this AssetHealthConditionTimemachine.  # noqa: E501

        Date of the Destroy Event  # noqa: E501

        :return: The deleted_datetime of this AssetHealthConditionTimemachine.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_datetime

    @deleted_datetime.setter
    def deleted_datetime(self, deleted_datetime):
        """Sets the deleted_datetime of this AssetHealthConditionTimemachine.

        Date of the Destroy Event  # noqa: E501

        :param deleted_datetime: The deleted_datetime of this AssetHealthConditionTimemachine.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and deleted_datetime is None:
            raise ValueError("Invalid value for `deleted_datetime`, must not be `None`")  # noqa: E501

        self._deleted_datetime = deleted_datetime

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
        if issubclass(AssetHealthConditionTimemachine, dict):
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
        if not isinstance(other, AssetHealthConditionTimemachine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetHealthConditionTimemachine):
            return True

        return self.to_dict() != other.to_dict()
