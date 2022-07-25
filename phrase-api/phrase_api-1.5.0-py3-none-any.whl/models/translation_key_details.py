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


class TranslationKeyDetails(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'name_hash': 'str',
        'plural': 'bool',
        'tags': 'list[str]',
        'data_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
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
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'name_hash': 'name_hash',
        'plural': 'plural',
        'tags': 'tags',
        'data_type': 'data_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
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

    def __init__(self, id=None, name=None, description=None, name_hash=None, plural=None, tags=None, data_type=None, created_at=None, updated_at=None, name_plural=None, comments_count=None, max_characters_allowed=None, screenshot_url=None, unformatted=None, xml_space_preserve=None, original_file=None, format_value_type=None, creator=None, local_vars_configuration=None):  # noqa: E501
        """TranslationKeyDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._name_hash = None
        self._plural = None
        self._tags = None
        self._data_type = None
        self._created_at = None
        self._updated_at = None
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

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if name_hash is not None:
            self.name_hash = name_hash
        if plural is not None:
            self.plural = plural
        if tags is not None:
            self.tags = tags
        if data_type is not None:
            self.data_type = data_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
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
    def id(self):
        """Gets the id of this TranslationKeyDetails.  # noqa: E501


        :return: The id of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationKeyDetails.


        :param id: The id of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TranslationKeyDetails.  # noqa: E501


        :return: The name of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TranslationKeyDetails.


        :param name: The name of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TranslationKeyDetails.  # noqa: E501


        :return: The description of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TranslationKeyDetails.


        :param description: The description of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name_hash(self):
        """Gets the name_hash of this TranslationKeyDetails.  # noqa: E501


        :return: The name_hash of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._name_hash

    @name_hash.setter
    def name_hash(self, name_hash):
        """Sets the name_hash of this TranslationKeyDetails.


        :param name_hash: The name_hash of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._name_hash = name_hash

    @property
    def plural(self):
        """Gets the plural of this TranslationKeyDetails.  # noqa: E501


        :return: The plural of this TranslationKeyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._plural

    @plural.setter
    def plural(self, plural):
        """Sets the plural of this TranslationKeyDetails.


        :param plural: The plural of this TranslationKeyDetails.  # noqa: E501
        :type: bool
        """

        self._plural = plural

    @property
    def tags(self):
        """Gets the tags of this TranslationKeyDetails.  # noqa: E501


        :return: The tags of this TranslationKeyDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TranslationKeyDetails.


        :param tags: The tags of this TranslationKeyDetails.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def data_type(self):
        """Gets the data_type of this TranslationKeyDetails.  # noqa: E501


        :return: The data_type of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this TranslationKeyDetails.


        :param data_type: The data_type of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def created_at(self):
        """Gets the created_at of this TranslationKeyDetails.  # noqa: E501


        :return: The created_at of this TranslationKeyDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TranslationKeyDetails.


        :param created_at: The created_at of this TranslationKeyDetails.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TranslationKeyDetails.  # noqa: E501


        :return: The updated_at of this TranslationKeyDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TranslationKeyDetails.


        :param updated_at: The updated_at of this TranslationKeyDetails.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def name_plural(self):
        """Gets the name_plural of this TranslationKeyDetails.  # noqa: E501


        :return: The name_plural of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._name_plural

    @name_plural.setter
    def name_plural(self, name_plural):
        """Sets the name_plural of this TranslationKeyDetails.


        :param name_plural: The name_plural of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._name_plural = name_plural

    @property
    def comments_count(self):
        """Gets the comments_count of this TranslationKeyDetails.  # noqa: E501


        :return: The comments_count of this TranslationKeyDetails.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this TranslationKeyDetails.


        :param comments_count: The comments_count of this TranslationKeyDetails.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def max_characters_allowed(self):
        """Gets the max_characters_allowed of this TranslationKeyDetails.  # noqa: E501


        :return: The max_characters_allowed of this TranslationKeyDetails.  # noqa: E501
        :rtype: int
        """
        return self._max_characters_allowed

    @max_characters_allowed.setter
    def max_characters_allowed(self, max_characters_allowed):
        """Sets the max_characters_allowed of this TranslationKeyDetails.


        :param max_characters_allowed: The max_characters_allowed of this TranslationKeyDetails.  # noqa: E501
        :type: int
        """

        self._max_characters_allowed = max_characters_allowed

    @property
    def screenshot_url(self):
        """Gets the screenshot_url of this TranslationKeyDetails.  # noqa: E501


        :return: The screenshot_url of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._screenshot_url

    @screenshot_url.setter
    def screenshot_url(self, screenshot_url):
        """Sets the screenshot_url of this TranslationKeyDetails.


        :param screenshot_url: The screenshot_url of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._screenshot_url = screenshot_url

    @property
    def unformatted(self):
        """Gets the unformatted of this TranslationKeyDetails.  # noqa: E501


        :return: The unformatted of this TranslationKeyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._unformatted

    @unformatted.setter
    def unformatted(self, unformatted):
        """Sets the unformatted of this TranslationKeyDetails.


        :param unformatted: The unformatted of this TranslationKeyDetails.  # noqa: E501
        :type: bool
        """

        self._unformatted = unformatted

    @property
    def xml_space_preserve(self):
        """Gets the xml_space_preserve of this TranslationKeyDetails.  # noqa: E501


        :return: The xml_space_preserve of this TranslationKeyDetails.  # noqa: E501
        :rtype: bool
        """
        return self._xml_space_preserve

    @xml_space_preserve.setter
    def xml_space_preserve(self, xml_space_preserve):
        """Sets the xml_space_preserve of this TranslationKeyDetails.


        :param xml_space_preserve: The xml_space_preserve of this TranslationKeyDetails.  # noqa: E501
        :type: bool
        """

        self._xml_space_preserve = xml_space_preserve

    @property
    def original_file(self):
        """Gets the original_file of this TranslationKeyDetails.  # noqa: E501


        :return: The original_file of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._original_file

    @original_file.setter
    def original_file(self, original_file):
        """Sets the original_file of this TranslationKeyDetails.


        :param original_file: The original_file of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._original_file = original_file

    @property
    def format_value_type(self):
        """Gets the format_value_type of this TranslationKeyDetails.  # noqa: E501


        :return: The format_value_type of this TranslationKeyDetails.  # noqa: E501
        :rtype: str
        """
        return self._format_value_type

    @format_value_type.setter
    def format_value_type(self, format_value_type):
        """Sets the format_value_type of this TranslationKeyDetails.


        :param format_value_type: The format_value_type of this TranslationKeyDetails.  # noqa: E501
        :type: str
        """

        self._format_value_type = format_value_type

    @property
    def creator(self):
        """Gets the creator of this TranslationKeyDetails.  # noqa: E501


        :return: The creator of this TranslationKeyDetails.  # noqa: E501
        :rtype: UserPreview
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TranslationKeyDetails.


        :param creator: The creator of this TranslationKeyDetails.  # noqa: E501
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
        if not isinstance(other, TranslationKeyDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationKeyDetails):
            return True

        return self.to_dict() != other.to_dict()
