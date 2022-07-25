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


class LocaleUpdateParameters(object):
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
        'branch': 'str',
        'name': 'str',
        'code': 'str',
        'default': 'bool',
        'main': 'bool',
        'rtl': 'bool',
        'source_locale_id': 'str',
        'fallback_locale_id': 'str',
        'unverify_new_translations': 'bool',
        'unverify_updated_translations': 'bool',
        'autotranslate': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'name': 'name',
        'code': 'code',
        'default': 'default',
        'main': 'main',
        'rtl': 'rtl',
        'source_locale_id': 'source_locale_id',
        'fallback_locale_id': 'fallback_locale_id',
        'unverify_new_translations': 'unverify_new_translations',
        'unverify_updated_translations': 'unverify_updated_translations',
        'autotranslate': 'autotranslate'
    }

    def __init__(self, branch=None, name=None, code=None, default=None, main=None, rtl=None, source_locale_id=None, fallback_locale_id=None, unverify_new_translations=None, unverify_updated_translations=None, autotranslate=None, local_vars_configuration=None):  # noqa: E501
        """LocaleUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._name = None
        self._code = None
        self._default = None
        self._main = None
        self._rtl = None
        self._source_locale_id = None
        self._fallback_locale_id = None
        self._unverify_new_translations = None
        self._unverify_updated_translations = None
        self._autotranslate = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
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
        if source_locale_id is not None:
            self.source_locale_id = source_locale_id
        if fallback_locale_id is not None:
            self.fallback_locale_id = fallback_locale_id
        if unverify_new_translations is not None:
            self.unverify_new_translations = unverify_new_translations
        if unverify_updated_translations is not None:
            self.unverify_updated_translations = unverify_updated_translations
        if autotranslate is not None:
            self.autotranslate = autotranslate

    @property
    def branch(self):
        """Gets the branch of this LocaleUpdateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this LocaleUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this LocaleUpdateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this LocaleUpdateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def name(self):
        """Gets the name of this LocaleUpdateParameters.  # noqa: E501

        Locale name  # noqa: E501

        :return: The name of this LocaleUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocaleUpdateParameters.

        Locale name  # noqa: E501

        :param name: The name of this LocaleUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this LocaleUpdateParameters.  # noqa: E501

        Locale ISO code  # noqa: E501

        :return: The code of this LocaleUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LocaleUpdateParameters.

        Locale ISO code  # noqa: E501

        :param code: The code of this LocaleUpdateParameters.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def default(self):
        """Gets the default of this LocaleUpdateParameters.  # noqa: E501

        Indicates whether locale is the default locale. If set to true, the previous default locale the project is no longer the default locale.  # noqa: E501

        :return: The default of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this LocaleUpdateParameters.

        Indicates whether locale is the default locale. If set to true, the previous default locale the project is no longer the default locale.  # noqa: E501

        :param default: The default of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def main(self):
        """Gets the main of this LocaleUpdateParameters.  # noqa: E501

        Indicates whether locale is a main locale. Main locales are part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Verification System</a> feature.  # noqa: E501

        :return: The main of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this LocaleUpdateParameters.

        Indicates whether locale is a main locale. Main locales are part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Verification System</a> feature.  # noqa: E501

        :param main: The main of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._main = main

    @property
    def rtl(self):
        """Gets the rtl of this LocaleUpdateParameters.  # noqa: E501

        Indicates whether locale is a RTL (Right-to-Left) locale.  # noqa: E501

        :return: The rtl of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._rtl

    @rtl.setter
    def rtl(self, rtl):
        """Sets the rtl of this LocaleUpdateParameters.

        Indicates whether locale is a RTL (Right-to-Left) locale.  # noqa: E501

        :param rtl: The rtl of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._rtl = rtl

    @property
    def source_locale_id(self):
        """Gets the source_locale_id of this LocaleUpdateParameters.  # noqa: E501

        Source locale. Can be the name or public id of the locale. Preferred is the public id.  # noqa: E501

        :return: The source_locale_id of this LocaleUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._source_locale_id

    @source_locale_id.setter
    def source_locale_id(self, source_locale_id):
        """Sets the source_locale_id of this LocaleUpdateParameters.

        Source locale. Can be the name or public id of the locale. Preferred is the public id.  # noqa: E501

        :param source_locale_id: The source_locale_id of this LocaleUpdateParameters.  # noqa: E501
        :type: str
        """

        self._source_locale_id = source_locale_id

    @property
    def fallback_locale_id(self):
        """Gets the fallback_locale_id of this LocaleUpdateParameters.  # noqa: E501

        Fallback locale for empty translations. Can be a locale name or id.  # noqa: E501

        :return: The fallback_locale_id of this LocaleUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._fallback_locale_id

    @fallback_locale_id.setter
    def fallback_locale_id(self, fallback_locale_id):
        """Sets the fallback_locale_id of this LocaleUpdateParameters.

        Fallback locale for empty translations. Can be a locale name or id.  # noqa: E501

        :param fallback_locale_id: The fallback_locale_id of this LocaleUpdateParameters.  # noqa: E501
        :type: str
        """

        self._fallback_locale_id = fallback_locale_id

    @property
    def unverify_new_translations(self):
        """Gets the unverify_new_translations of this LocaleUpdateParameters.  # noqa: E501

        Indicates that new translations for this locale should be marked as unverified. Part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Advanced Workflows</a> feature.  # noqa: E501

        :return: The unverify_new_translations of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._unverify_new_translations

    @unverify_new_translations.setter
    def unverify_new_translations(self, unverify_new_translations):
        """Sets the unverify_new_translations of this LocaleUpdateParameters.

        Indicates that new translations for this locale should be marked as unverified. Part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Advanced Workflows</a> feature.  # noqa: E501

        :param unverify_new_translations: The unverify_new_translations of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._unverify_new_translations = unverify_new_translations

    @property
    def unverify_updated_translations(self):
        """Gets the unverify_updated_translations of this LocaleUpdateParameters.  # noqa: E501

        Indicates that updated translations for this locale should be marked as unverified. Part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Advanced Workflows</a> feature.  # noqa: E501

        :return: The unverify_updated_translations of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._unverify_updated_translations

    @unverify_updated_translations.setter
    def unverify_updated_translations(self, unverify_updated_translations):
        """Sets the unverify_updated_translations of this LocaleUpdateParameters.

        Indicates that updated translations for this locale should be marked as unverified. Part of the <a href=\"https://help.phrase.com/help/verification-and-proofreading\" target=\"_blank\">Advanced Workflows</a> feature.  # noqa: E501

        :param unverify_updated_translations: The unverify_updated_translations of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._unverify_updated_translations = unverify_updated_translations

    @property
    def autotranslate(self):
        """Gets the autotranslate of this LocaleUpdateParameters.  # noqa: E501

        If set, translations for this locale will be fetched automatically, right after creation.  # noqa: E501

        :return: The autotranslate of this LocaleUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._autotranslate

    @autotranslate.setter
    def autotranslate(self, autotranslate):
        """Sets the autotranslate of this LocaleUpdateParameters.

        If set, translations for this locale will be fetched automatically, right after creation.  # noqa: E501

        :param autotranslate: The autotranslate of this LocaleUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._autotranslate = autotranslate

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
        if not isinstance(other, LocaleUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocaleUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()
