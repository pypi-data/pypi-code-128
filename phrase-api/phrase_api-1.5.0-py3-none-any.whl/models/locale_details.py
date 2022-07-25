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


class LocaleDetails(object):
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
        'code': 'str',
        'default': 'bool',
        'main': 'bool',
        'rtl': 'bool',
        'plural_forms': 'list[str]',
        'source_locale': 'LocalePreview',
        'fallback_locale': 'LocalePreview',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'statistics': 'LocaleStatistics'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'default': 'default',
        'main': 'main',
        'rtl': 'rtl',
        'plural_forms': 'plural_forms',
        'source_locale': 'source_locale',
        'fallback_locale': 'fallback_locale',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'statistics': 'statistics'
    }

    def __init__(self, id=None, name=None, code=None, default=None, main=None, rtl=None, plural_forms=None, source_locale=None, fallback_locale=None, created_at=None, updated_at=None, statistics=None, local_vars_configuration=None):  # noqa: E501
        """LocaleDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._code = None
        self._default = None
        self._main = None
        self._rtl = None
        self._plural_forms = None
        self._source_locale = None
        self._fallback_locale = None
        self._created_at = None
        self._updated_at = None
        self._statistics = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if default is not None:
            self.default = default
        if main is not None:
            self.main = main
        if rtl is not None:
            self.rtl = rtl
        if plural_forms is not None:
            self.plural_forms = plural_forms
        if source_locale is not None:
            self.source_locale = source_locale
        if fallback_locale is not None:
            self.fallback_locale = fallback_locale
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if statistics is not None:
            self.statistics = statistics

    @property
    def id(self):
        """Gets the id of this LocaleDetails.  # noqa: E501


        :return: The id of this LocaleDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocaleDetails.


        :param id: The id of this LocaleDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LocaleDetails.  # noqa: E501


        :return: The name of this LocaleDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocaleDetails.


        :param name: The name of this LocaleDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this LocaleDetails.  # noqa: E501


        :return: The code of this LocaleDetails.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LocaleDetails.


        :param code: The code of this LocaleDetails.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def default(self):
        """Gets the default of this LocaleDetails.  # noqa: E501


        :return: The default of this LocaleDetails.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this LocaleDetails.


        :param default: The default of this LocaleDetails.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def main(self):
        """Gets the main of this LocaleDetails.  # noqa: E501


        :return: The main of this LocaleDetails.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this LocaleDetails.


        :param main: The main of this LocaleDetails.  # noqa: E501
        :type: bool
        """

        self._main = main

    @property
    def rtl(self):
        """Gets the rtl of this LocaleDetails.  # noqa: E501


        :return: The rtl of this LocaleDetails.  # noqa: E501
        :rtype: bool
        """
        return self._rtl

    @rtl.setter
    def rtl(self, rtl):
        """Sets the rtl of this LocaleDetails.


        :param rtl: The rtl of this LocaleDetails.  # noqa: E501
        :type: bool
        """

        self._rtl = rtl

    @property
    def plural_forms(self):
        """Gets the plural_forms of this LocaleDetails.  # noqa: E501


        :return: The plural_forms of this LocaleDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._plural_forms

    @plural_forms.setter
    def plural_forms(self, plural_forms):
        """Sets the plural_forms of this LocaleDetails.


        :param plural_forms: The plural_forms of this LocaleDetails.  # noqa: E501
        :type: list[str]
        """

        self._plural_forms = plural_forms

    @property
    def source_locale(self):
        """Gets the source_locale of this LocaleDetails.  # noqa: E501


        :return: The source_locale of this LocaleDetails.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._source_locale

    @source_locale.setter
    def source_locale(self, source_locale):
        """Sets the source_locale of this LocaleDetails.


        :param source_locale: The source_locale of this LocaleDetails.  # noqa: E501
        :type: LocalePreview
        """

        self._source_locale = source_locale

    @property
    def fallback_locale(self):
        """Gets the fallback_locale of this LocaleDetails.  # noqa: E501


        :return: The fallback_locale of this LocaleDetails.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._fallback_locale

    @fallback_locale.setter
    def fallback_locale(self, fallback_locale):
        """Sets the fallback_locale of this LocaleDetails.


        :param fallback_locale: The fallback_locale of this LocaleDetails.  # noqa: E501
        :type: LocalePreview
        """

        self._fallback_locale = fallback_locale

    @property
    def created_at(self):
        """Gets the created_at of this LocaleDetails.  # noqa: E501


        :return: The created_at of this LocaleDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LocaleDetails.


        :param created_at: The created_at of this LocaleDetails.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LocaleDetails.  # noqa: E501


        :return: The updated_at of this LocaleDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LocaleDetails.


        :param updated_at: The updated_at of this LocaleDetails.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def statistics(self):
        """Gets the statistics of this LocaleDetails.  # noqa: E501


        :return: The statistics of this LocaleDetails.  # noqa: E501
        :rtype: LocaleStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this LocaleDetails.


        :param statistics: The statistics of this LocaleDetails.  # noqa: E501
        :type: LocaleStatistics
        """

        self._statistics = statistics

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
        if not isinstance(other, LocaleDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocaleDetails):
            return True

        return self.to_dict() != other.to_dict()
