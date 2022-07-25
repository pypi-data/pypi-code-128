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


class IcuSkeletonParameters(object):
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
        'content': 'str',
        'locale_codes': 'list[str]',
        'keep_content': 'bool',
        'zero_form_enabled': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'locale_codes': 'locale_codes',
        'keep_content': 'keep_content',
        'zero_form_enabled': 'zero_form_enabled'
    }

    def __init__(self, content=None, locale_codes=None, keep_content=None, zero_form_enabled=None, local_vars_configuration=None):  # noqa: E501
        """IcuSkeletonParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._locale_codes = None
        self._keep_content = None
        self._zero_form_enabled = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if locale_codes is not None:
            self.locale_codes = locale_codes
        if keep_content is not None:
            self.keep_content = keep_content
        if zero_form_enabled is not None:
            self.zero_form_enabled = zero_form_enabled

    @property
    def content(self):
        """Gets the content of this IcuSkeletonParameters.  # noqa: E501

        Source content  # noqa: E501

        :return: The content of this IcuSkeletonParameters.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this IcuSkeletonParameters.

        Source content  # noqa: E501

        :param content: The content of this IcuSkeletonParameters.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def locale_codes(self):
        """Gets the locale_codes of this IcuSkeletonParameters.  # noqa: E501

        Locale codes  # noqa: E501

        :return: The locale_codes of this IcuSkeletonParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._locale_codes

    @locale_codes.setter
    def locale_codes(self, locale_codes):
        """Sets the locale_codes of this IcuSkeletonParameters.

        Locale codes  # noqa: E501

        :param locale_codes: The locale_codes of this IcuSkeletonParameters.  # noqa: E501
        :type: list[str]
        """

        self._locale_codes = locale_codes

    @property
    def keep_content(self):
        """Gets the keep_content of this IcuSkeletonParameters.  # noqa: E501

        Keep the content and add missing plural forms for each locale  # noqa: E501

        :return: The keep_content of this IcuSkeletonParameters.  # noqa: E501
        :rtype: bool
        """
        return self._keep_content

    @keep_content.setter
    def keep_content(self, keep_content):
        """Sets the keep_content of this IcuSkeletonParameters.

        Keep the content and add missing plural forms for each locale  # noqa: E501

        :param keep_content: The keep_content of this IcuSkeletonParameters.  # noqa: E501
        :type: bool
        """

        self._keep_content = keep_content

    @property
    def zero_form_enabled(self):
        """Gets the zero_form_enabled of this IcuSkeletonParameters.  # noqa: E501

        Indicates whether the zero form should be included or excluded in the returned skeletons  # noqa: E501

        :return: The zero_form_enabled of this IcuSkeletonParameters.  # noqa: E501
        :rtype: bool
        """
        return self._zero_form_enabled

    @zero_form_enabled.setter
    def zero_form_enabled(self, zero_form_enabled):
        """Sets the zero_form_enabled of this IcuSkeletonParameters.

        Indicates whether the zero form should be included or excluded in the returned skeletons  # noqa: E501

        :param zero_form_enabled: The zero_form_enabled of this IcuSkeletonParameters.  # noqa: E501
        :type: bool
        """

        self._zero_form_enabled = zero_form_enabled

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
        if not isinstance(other, IcuSkeletonParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IcuSkeletonParameters):
            return True

        return self.to_dict() != other.to_dict()
