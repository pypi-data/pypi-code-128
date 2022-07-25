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


class APIKeyResponse(object):
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
        'id': 'int',
        'api_key': 'str',
        'api_secret': 'str',
        'client_application': 'NestedIDHref'
    }

    attribute_map = {
        'id': 'id',
        'api_key': 'api_key',
        'api_secret': 'api_secret',
        'client_application': 'client_application'
    }

    def __init__(self, id=None, api_key=None, api_secret=None, client_application=None, _configuration=None):  # noqa: E501
        """APIKeyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._api_key = None
        self._api_secret = None
        self._client_application = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if api_key is not None:
            self.api_key = api_key
        if api_secret is not None:
            self.api_secret = api_secret
        if client_application is not None:
            self.client_application = client_application

    @property
    def id(self):
        """Gets the id of this APIKeyResponse.  # noqa: E501

        Id of object  # noqa: E501

        :return: The id of this APIKeyResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APIKeyResponse.

        Id of object  # noqa: E501

        :param id: The id of this APIKeyResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def api_key(self):
        """Gets the api_key of this APIKeyResponse.  # noqa: E501

        the api_key value  # noqa: E501

        :return: The api_key of this APIKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this APIKeyResponse.

        the api_key value  # noqa: E501

        :param api_key: The api_key of this APIKeyResponse.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def api_secret(self):
        """Gets the api_secret of this APIKeyResponse.  # noqa: E501

        API Key api_secret (only for oauth authentication)  # noqa: E501

        :return: The api_secret of this APIKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this APIKeyResponse.

        API Key api_secret (only for oauth authentication)  # noqa: E501

        :param api_secret: The api_secret of this APIKeyResponse.  # noqa: E501
        :type: str
        """

        self._api_secret = api_secret

    @property
    def client_application(self):
        """Gets the client_application of this APIKeyResponse.  # noqa: E501


        :return: The client_application of this APIKeyResponse.  # noqa: E501
        :rtype: NestedIDHref
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this APIKeyResponse.


        :param client_application: The client_application of this APIKeyResponse.  # noqa: E501
        :type: NestedIDHref
        """

        self._client_application = client_application

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
        if issubclass(APIKeyResponse, dict):
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
        if not isinstance(other, APIKeyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIKeyResponse):
            return True

        return self.to_dict() != other.to_dict()
