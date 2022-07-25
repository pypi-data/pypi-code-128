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


class UpdateAuthMethodOAuth2(object):
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
        'access_expires': 'int',
        'audience': 'str',
        'bound_client_ids': 'list[str]',
        'bound_ips': 'list[str]',
        'force_sub_claims': 'bool',
        'gw_bound_ips': 'list[str]',
        'issuer': 'str',
        'jwks_uri': 'str',
        'jwt_ttl': 'int',
        'name': 'str',
        'new_name': 'str',
        'token': 'str',
        'uid_token': 'str',
        'unique_identifier': 'str'
    }

    attribute_map = {
        'access_expires': 'access-expires',
        'audience': 'audience',
        'bound_client_ids': 'bound-client-ids',
        'bound_ips': 'bound-ips',
        'force_sub_claims': 'force-sub-claims',
        'gw_bound_ips': 'gw-bound-ips',
        'issuer': 'issuer',
        'jwks_uri': 'jwks-uri',
        'jwt_ttl': 'jwt-ttl',
        'name': 'name',
        'new_name': 'new-name',
        'token': 'token',
        'uid_token': 'uid-token',
        'unique_identifier': 'unique-identifier'
    }

    def __init__(self, access_expires=0, audience=None, bound_client_ids=None, bound_ips=None, force_sub_claims=None, gw_bound_ips=None, issuer=None, jwks_uri=None, jwt_ttl=None, name=None, new_name=None, token=None, uid_token=None, unique_identifier=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAuthMethodOAuth2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_expires = None
        self._audience = None
        self._bound_client_ids = None
        self._bound_ips = None
        self._force_sub_claims = None
        self._gw_bound_ips = None
        self._issuer = None
        self._jwks_uri = None
        self._jwt_ttl = None
        self._name = None
        self._new_name = None
        self._token = None
        self._uid_token = None
        self._unique_identifier = None
        self.discriminator = None

        if access_expires is not None:
            self.access_expires = access_expires
        if audience is not None:
            self.audience = audience
        if bound_client_ids is not None:
            self.bound_client_ids = bound_client_ids
        if bound_ips is not None:
            self.bound_ips = bound_ips
        if force_sub_claims is not None:
            self.force_sub_claims = force_sub_claims
        if gw_bound_ips is not None:
            self.gw_bound_ips = gw_bound_ips
        if issuer is not None:
            self.issuer = issuer
        self.jwks_uri = jwks_uri
        if jwt_ttl is not None:
            self.jwt_ttl = jwt_ttl
        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if token is not None:
            self.token = token
        if uid_token is not None:
            self.uid_token = uid_token
        self.unique_identifier = unique_identifier

    @property
    def access_expires(self):
        """Gets the access_expires of this UpdateAuthMethodOAuth2.  # noqa: E501

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :return: The access_expires of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this UpdateAuthMethodOAuth2.

        Access expiration date in Unix timestamp (select 0 for access without expiry date)  # noqa: E501

        :param access_expires: The access_expires of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: int
        """

        self._access_expires = access_expires

    @property
    def audience(self):
        """Gets the audience of this UpdateAuthMethodOAuth2.  # noqa: E501

        The audience in the JWT  # noqa: E501

        :return: The audience of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this UpdateAuthMethodOAuth2.

        The audience in the JWT  # noqa: E501

        :param audience: The audience of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def bound_client_ids(self):
        """Gets the bound_client_ids of this UpdateAuthMethodOAuth2.  # noqa: E501

        The clients ids that the access is restricted to  # noqa: E501

        :return: The bound_client_ids of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_client_ids

    @bound_client_ids.setter
    def bound_client_ids(self, bound_client_ids):
        """Sets the bound_client_ids of this UpdateAuthMethodOAuth2.

        The clients ids that the access is restricted to  # noqa: E501

        :param bound_client_ids: The bound_client_ids of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: list[str]
        """

        self._bound_client_ids = bound_client_ids

    @property
    def bound_ips(self):
        """Gets the bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :return: The bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: list[str]
        """
        return self._bound_ips

    @bound_ips.setter
    def bound_ips(self, bound_ips):
        """Sets the bound_ips of this UpdateAuthMethodOAuth2.

        A CIDR whitelist with the IPs that the access is restricted to  # noqa: E501

        :param bound_ips: The bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: list[str]
        """

        self._bound_ips = bound_ips

    @property
    def force_sub_claims(self):
        """Gets the force_sub_claims of this UpdateAuthMethodOAuth2.  # noqa: E501

        if true: enforce role-association must include sub claims  # noqa: E501

        :return: The force_sub_claims of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: bool
        """
        return self._force_sub_claims

    @force_sub_claims.setter
    def force_sub_claims(self, force_sub_claims):
        """Sets the force_sub_claims of this UpdateAuthMethodOAuth2.

        if true: enforce role-association must include sub claims  # noqa: E501

        :param force_sub_claims: The force_sub_claims of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: bool
        """

        self._force_sub_claims = force_sub_claims

    @property
    def gw_bound_ips(self):
        """Gets the gw_bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501

        A CIDR whitelist with the GW IPs that the access is restricted to  # noqa: E501

        :return: The gw_bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: list[str]
        """
        return self._gw_bound_ips

    @gw_bound_ips.setter
    def gw_bound_ips(self, gw_bound_ips):
        """Sets the gw_bound_ips of this UpdateAuthMethodOAuth2.

        A CIDR whitelist with the GW IPs that the access is restricted to  # noqa: E501

        :param gw_bound_ips: The gw_bound_ips of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: list[str]
        """

        self._gw_bound_ips = gw_bound_ips

    @property
    def issuer(self):
        """Gets the issuer of this UpdateAuthMethodOAuth2.  # noqa: E501

        Issuer URL  # noqa: E501

        :return: The issuer of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this UpdateAuthMethodOAuth2.

        Issuer URL  # noqa: E501

        :param issuer: The issuer of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this UpdateAuthMethodOAuth2.  # noqa: E501

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :return: The jwks_uri of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this UpdateAuthMethodOAuth2.

        The URL to the JSON Web Key Set (JWKS) that containing the public keys that should be used to verify any JSON Web Token (JWT) issued by the authorization server.  # noqa: E501

        :param jwks_uri: The jwks_uri of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jwks_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `jwks_uri`, must not be `None`")  # noqa: E501

        self._jwks_uri = jwks_uri

    @property
    def jwt_ttl(self):
        """Gets the jwt_ttl of this UpdateAuthMethodOAuth2.  # noqa: E501

        Jwt TTL  # noqa: E501

        :return: The jwt_ttl of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: int
        """
        return self._jwt_ttl

    @jwt_ttl.setter
    def jwt_ttl(self, jwt_ttl):
        """Sets the jwt_ttl of this UpdateAuthMethodOAuth2.

        Jwt TTL  # noqa: E501

        :param jwt_ttl: The jwt_ttl of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: int
        """

        self._jwt_ttl = jwt_ttl

    @property
    def name(self):
        """Gets the name of this UpdateAuthMethodOAuth2.  # noqa: E501

        Auth Method name  # noqa: E501

        :return: The name of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAuthMethodOAuth2.

        Auth Method name  # noqa: E501

        :param name: The name of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def new_name(self):
        """Gets the new_name of this UpdateAuthMethodOAuth2.  # noqa: E501

        Auth Method new name  # noqa: E501

        :return: The new_name of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this UpdateAuthMethodOAuth2.

        Auth Method new name  # noqa: E501

        :param new_name: The new_name of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def token(self):
        """Gets the token of this UpdateAuthMethodOAuth2.  # noqa: E501

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :return: The token of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateAuthMethodOAuth2.

        Authentication token (see `/auth` and `/configure`)  # noqa: E501

        :param token: The token of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid_token(self):
        """Gets the uid_token of this UpdateAuthMethodOAuth2.  # noqa: E501

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :return: The uid_token of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._uid_token

    @uid_token.setter
    def uid_token(self, uid_token):
        """Sets the uid_token of this UpdateAuthMethodOAuth2.

        The universal identity token, Required only for universal_identity authentication  # noqa: E501

        :param uid_token: The uid_token of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """

        self._uid_token = uid_token

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this UpdateAuthMethodOAuth2.  # noqa: E501

        A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \"sub claim\" that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization.  # noqa: E501

        :return: The unique_identifier of this UpdateAuthMethodOAuth2.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this UpdateAuthMethodOAuth2.

        A unique identifier (ID) value should be configured for OAuth2, LDAP and SAML authentication method types and is usually a value such as the email, username, or upn for example. Whenever a user logs in with a token, these authentication types issue a \"sub claim\" that contains details uniquely identifying that user. This sub claim includes a key containing the ID value that you configured, and is used to distinguish between different users from within the same organization.  # noqa: E501

        :param unique_identifier: The unique_identifier of this UpdateAuthMethodOAuth2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unique_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_identifier`, must not be `None`")  # noqa: E501

        self._unique_identifier = unique_identifier

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
        if not isinstance(other, UpdateAuthMethodOAuth2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAuthMethodOAuth2):
            return True

        return self.to_dict() != other.to_dict()
