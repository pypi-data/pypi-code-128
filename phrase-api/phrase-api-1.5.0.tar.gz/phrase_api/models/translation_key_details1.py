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


class TranslationKeyDetails1(object):
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
        'name_plural': 'str',
        'comments_count': 'int',
        'max_characters_allowed': 'int',
        'screenshot_url': 'str',
        'unformatted': 'bool',
        'xml_space_preserve': 'bool',
        'original_file': 'str',
        'format_value_type': 'str',
        'creator': 'UserPreview'
    }

    attribute_map = {
        'name_plural': 'name_plural',
        'comments_count': 'comments_count',
        'max_characters_allowed': 'max_characters_allowed',
        'screenshot_url': 'screenshot_url',
        'unformatted': 'unformatted',
        'xml_space_preserve': 'xml_space_preserve',
        'original_file': 'original_file',
        'format_value_type': 'format_value_type',
        'creator': 'creator'
    }

    def __init__(self, name_plural=None, comments_count=None, max_characters_allowed=None, screenshot_url=None, unformatted=None, xml_space_preserve=None, original_file=None, format_value_type=None, creator=None, local_vars_configuration=None):  # noqa: E501
        """TranslationKeyDetails1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name_plural = None
        self._comments_count = None
        self._max_characters_allowed = None
        self._screenshot_url = None
        self._unformatted = None
        self._xml_space_preserve = None
        self._original_file = None
        self._format_value_type = None
        self._creator = None
        self.discriminator = None

        if name_plural is not None:
            self.name_plural = name_plural
        if comments_count is not None:
            self.comments_count = comments_count
        if max_characters_allowed is not None:
            self.max_characters_allowed = max_characters_allowed
        if screenshot_url is not None:
            self.screenshot_url = screenshot_url
        if unformatted is not None:
            self.unformatted = unformatted
        if xml_space_preserve is not None:
            self.xml_space_preserve = xml_space_preserve
        if original_file is not None:
            self.original_file = original_file
        if format_value_type is not None:
            self.format_value_type = format_value_type
        if creator is not None:
            self.creator = creator

    @property
    def name_plural(self):
        """Gets the name_plural of this TranslationKeyDetails1.  # noqa: E501


        :return: The name_plural of this TranslationKeyDetails1.  # noqa: E501
        :rtype: str
        """
        return self._name_plural

    @name_plural.setter
    def name_plural(self, name_plural):
        """Sets the name_plural of this TranslationKeyDetails1.


        :param name_plural: The name_plural of this TranslationKeyDetails1.  # noqa: E501
        :type: str
        """

        self._name_plural = name_plural

    @property
    def comments_count(self):
        """Gets the comments_count of this TranslationKeyDetails1.  # noqa: E501


        :return: The comments_count of this TranslationKeyDetails1.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this TranslationKeyDetails1.


        :param comments_count: The comments_count of this TranslationKeyDetails1.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def max_characters_allowed(self):
        """Gets the max_characters_allowed of this TranslationKeyDetails1.  # noqa: E501


        :return: The max_characters_allowed of this TranslationKeyDetails1.  # noqa: E501
        :rtype: int
        """
        return self._max_characters_allowed

    @max_characters_allowed.setter
    def max_characters_allowed(self, max_characters_allowed):
        """Sets the max_characters_allowed of this TranslationKeyDetails1.


        :param max_characters_allowed: The max_characters_allowed of this TranslationKeyDetails1.  # noqa: E501
        :type: int
        """

        self._max_characters_allowed = max_characters_allowed

    @property
    def screenshot_url(self):
        """Gets the screenshot_url of this TranslationKeyDetails1.  # noqa: E501


        :return: The screenshot_url of this TranslationKeyDetails1.  # noqa: E501
        :rtype: str
        """
        return self._screenshot_url

    @screenshot_url.setter
    def screenshot_url(self, screenshot_url):
        """Sets the screenshot_url of this TranslationKeyDetails1.


        :param screenshot_url: The screenshot_url of this TranslationKeyDetails1.  # noqa: E501
        :type: str
        """

        self._screenshot_url = screenshot_url

    @property
    def unformatted(self):
        """Gets the unformatted of this TranslationKeyDetails1.  # noqa: E501


        :return: The unformatted of this TranslationKeyDetails1.  # noqa: E501
        :rtype: bool
        """
        return self._unformatted

    @unformatted.setter
    def unformatted(self, unformatted):
        """Sets the unformatted of this TranslationKeyDetails1.


        :param unformatted: The unformatted of this TranslationKeyDetails1.  # noqa: E501
        :type: bool
        """

        self._unformatted = unformatted

    @property
    def xml_space_preserve(self):
        """Gets the xml_space_preserve of this TranslationKeyDetails1.  # noqa: E501


        :return: The xml_space_preserve of this TranslationKeyDetails1.  # noqa: E501
        :rtype: bool
        """
        return self._xml_space_preserve

    @xml_space_preserve.setter
    def xml_space_preserve(self, xml_space_preserve):
        """Sets the xml_space_preserve of this TranslationKeyDetails1.


        :param xml_space_preserve: The xml_space_preserve of this TranslationKeyDetails1.  # noqa: E501
        :type: bool
        """

        self._xml_space_preserve = xml_space_preserve

    @property
    def original_file(self):
        """Gets the original_file of this TranslationKeyDetails1.  # noqa: E501


        :return: The original_file of this TranslationKeyDetails1.  # noqa: E501
        :rtype: str
        """
        return self._original_file

    @original_file.setter
    def original_file(self, original_file):
        """Sets the original_file of this TranslationKeyDetails1.


        :param original_file: The original_file of this TranslationKeyDetails1.  # noqa: E501
        :type: str
        """

        self._original_file = original_file

    @property
    def format_value_type(self):
        """Gets the format_value_type of this TranslationKeyDetails1.  # noqa: E501


        :return: The format_value_type of this TranslationKeyDetails1.  # noqa: E501
        :rtype: str
        """
        return self._format_value_type

    @format_value_type.setter
    def format_value_type(self, format_value_type):
        """Sets the format_value_type of this TranslationKeyDetails1.


        :param format_value_type: The format_value_type of this TranslationKeyDetails1.  # noqa: E501
        :type: str
        """

        self._format_value_type = format_value_type

    @property
    def creator(self):
        """Gets the creator of this TranslationKeyDetails1.  # noqa: E501


        :return: The creator of this TranslationKeyDetails1.  # noqa: E501
        :rtype: UserPreview
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TranslationKeyDetails1.


        :param creator: The creator of this TranslationKeyDetails1.  # noqa: E501
        :type: UserPreview
        """

        self._creator = creator

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
        if not isinstance(other, TranslationKeyDetails1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationKeyDetails1):
            return True

        return self.to_dict() != other.to_dict()
