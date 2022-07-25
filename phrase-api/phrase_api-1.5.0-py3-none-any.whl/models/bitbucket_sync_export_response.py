# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class BitbucketSyncExportResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status_path': 'str'
    }

    attribute_map = {
        'status_path': 'status_path'
    }

    def __init__(self, status_path=None, local_vars_configuration=None):  # noqa: E501
        """BitbucketSyncExportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_path = None
        self.discriminator = None

        if status_path is not None:
            self.status_path = status_path

    @property
    def status_path(self):
        """Gets the status_path of this BitbucketSyncExportResponse.  # noqa: E501


        :return: The status_path of this BitbucketSyncExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_path

    @status_path.setter
    def status_path(self, status_path):
        """Sets the status_path of this BitbucketSyncExportResponse.


        :param status_path: The status_path of this BitbucketSyncExportResponse.  # noqa: E501
        :type: str
        """

        self._status_path = status_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BitbucketSyncExportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BitbucketSyncExportResponse):
            return True

        return self.to_dict() != other.to_dict()
