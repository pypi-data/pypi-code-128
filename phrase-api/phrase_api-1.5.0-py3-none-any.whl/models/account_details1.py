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


class AccountDetails1(object):
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
        'subscription': 'Subscription',
        'slug': 'str'
    }

    attribute_map = {
        'subscription': 'subscription',
        'slug': 'slug'
    }

    def __init__(self, subscription=None, slug=None, local_vars_configuration=None):  # noqa: E501
        """AccountDetails1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subscription = None
        self._slug = None
        self.discriminator = None

        if subscription is not None:
            self.subscription = subscription
        if slug is not None:
            self.slug = slug

    @property
    def subscription(self):
        """Gets the subscription of this AccountDetails1.  # noqa: E501


        :return: The subscription of this AccountDetails1.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this AccountDetails1.


        :param subscription: The subscription of this AccountDetails1.  # noqa: E501
        :type: Subscription
        """

        self._subscription = subscription

    @property
    def slug(self):
        """Gets the slug of this AccountDetails1.  # noqa: E501


        :return: The slug of this AccountDetails1.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this AccountDetails1.


        :param slug: The slug of this AccountDetails1.  # noqa: E501
        :type: str
        """

        self._slug = slug

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
        if not isinstance(other, AccountDetails1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDetails1):
            return True

        return self.to_dict() != other.to_dict()
