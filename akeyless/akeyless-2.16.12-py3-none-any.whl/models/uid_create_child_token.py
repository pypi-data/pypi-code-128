# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class UidCreateChildToken(object):
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
        'auth_method_name': 'str',
        'child_deny_inheritance': 'bool',
        'child_deny_rotate': 'bool',
        'child_ttl': 'int',
        'comment': 'str',
        'token': 'str',
        'uid_token': 'str',
        'uid_token_id': 'str'
    }

    attribute_map = {
        'auth_method_name': 'auth-method-name',
        'child_deny_inheritance': 'child-deny-inheritance',
        'child_deny_rotate': 'child-deny-rotate',
        'child_ttl': 'child-ttl',
        'comment': 'comment',
        'token': 'token',
        'uid_token': 'uid-token',
        'uid_token_id': 'uid-token-id'
    }

    def __init__(self, auth_method_name=None, child_deny_inheritance=None, child_deny_rotate=None, child_ttl=None, comment=None, token=None, uid_token=None, uid_token_id=None, local_vars_configuration=None):  # noqa: E501
        """UidCreateChildToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth_method_name = None
        self._child_deny_inheritance = None
        self._child_deny_rotate = None
        self._child_ttl = None
        self._comment = None
        self._token = None
        self._uid_token = None
        self._uid_token_id = None
        self.discriminator = None

        if auth_method_name is not None:
            self.auth_method_name = auth_method_name
        if child_deny_inheritance is not None:
            self.child_deny_inheritance = child_deny_inheritance
        if child_deny_rotate is not None:
            self.child_deny_rotate = child_deny_rotate
        if child_ttl is not None:
            self.child_ttl = child_ttl
        if comment is not None:
            self.comment = comment
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        if uid_token_id is not None:
            self.uid_token_id = uid_token_id

    @property
    def auth_method_name(self):
        """Gets the auth_method_name of this UidCreateChildToken.  # noqa: E501

        The universal identity auth method name, required only when uid-token is not provided  # noqa: E501

        :return: The auth_method_name of this UidCreateChildToken.  # noqa: E501
        :rtype: str
        """
        return self._auth_method_name

    @auth_method_name.setter
    def auth_method_name(self, auth_method_name):
        """Sets the auth_method_name of this UidCreateChildToken.

        The universal identity auth method name, required only when uid-token is not provided  # noqa: E501

        :param auth_method_name: The auth_method_name of this UidCreateChildToken.  # noqa: E501
        :type: str
        """

        self._auth_method_name = auth_method_name

    @property
    def child_deny_inheritance(self):
        """Gets the child_deny_inheritance of this UidCreateChildToken.  # noqa: E501

        Deny from new child to create their own children  # noqa: E501

        :return: The child_deny_inheritance of this UidCreateChildToken.  # noqa: E501
        :rtype: bool
        """
        return self._child_deny_inheritance

    @child_deny_inheritance.setter
    def child_deny_inheritance(self, child_deny_inheritance):
        """Sets the child_deny_inheritance of this UidCreateChildToken.

        Deny from new child to create their own children  # noqa: E501

        :param child_deny_inheritance: The child_deny_inheritance of this UidCreateChildToken.  # noqa: E501
        :type: bool
        """

        self._child_deny_inheritance = child_deny_inheritance

    @property
    def child_deny_rotate(self):
        """Gets the child_deny_rotate of this UidCreateChildToken.  # noqa: E501

        Deny from new child to rotate  # noqa: E501

        :return: The child_deny_rotate of this UidCreateChildToken.  # noqa: E501
        :rtype: bool
        """
        return self._child_deny_rotate

    @child_deny_rotate.setter
    def child_deny_rotate(self, child_deny_rotate):
        """Sets the child_deny_rotate of this UidCreateChildToken.

        Deny from new child to rotate  # noqa: E501

        :param child_deny_rotate: The child_deny_rotate of this UidCreateChildToken.  # noqa: E501
        :type: bool
        """

        self._child_deny_rotate = child_deny_rotate

    @property
    def child_ttl(self):
        """Gets the child_ttl of this UidCreateChildToken.  # noqa: E501

        New child token ttl  # noqa: E501

        :return: The child_ttl of this UidCreateChildToken.  # noqa: E501
        :rtype: int
        """
        return self._child_ttl

    @child_ttl.setter
    def child_ttl(self, child_ttl):
        """Sets the child_ttl of this UidCreateChildToken.

        New child token ttl  # noqa: E501

        :param child_ttl: The child_ttl of this UidCreateChildToken.  # noqa: E501
        :type: int
        """

        self._child_ttl = child_ttl

    @property
    def comment(self):
        """Gets the comment of this UidCreateChildToken.  # noqa: E501

        New Token comment  # noqa: E501

        :return: The comment of this UidCreateChildToken.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UidCreateChildToken.

        New Token comment  # noqa: E501

        :param comment: The comment of this UidCreateChildToken.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def token(self):
        """Gets the token of this UidCreateChildToken.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UidCreateChildToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UidCreateChildToken.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UidCreateChildToken.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UidCreateChildToken.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UidCreateChildToken.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UidCreateChildToken.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UidCreateChildToken.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def uid_token_id(self):
        """Gets the uid_token_id of this UidCreateChildToken.  # noqa: E501

        The ID of the uid-token, required only when uid-token is not provided  # noqa: E501

        :return: The uid_token_id of this UidCreateChildToken.  # noqa: E501
        :rtype: str
        """
        return self._uid_token_id

    @uid_token_id.setter
    def uid_token_id(self, uid_token_id):
        """Sets the uid_token_id of this UidCreateChildToken.

        The ID of the uid-token, required only when uid-token is not provided  # noqa: E501

        :param uid_token_id: The uid_token_id of this UidCreateChildToken.  # noqa: E501
        :type: str
        """

        self._uid_token_id = uid_token_id

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
        if not isinstance(other, UidCreateChildToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UidCreateChildToken):
            return True

        return self.to_dict() != other.to_dict()
