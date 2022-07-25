# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GeneratePublicKeyRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'encryption_type': 'str',
        'target_origin': 'str'
    }

    attribute_map = {
        'encryption_type': 'encryptionType',
        'target_origin': 'targetOrigin'
    }

    def __init__(self, encryption_type=None, target_origin=None):
        """
        GeneratePublicKeyRequest - a model defined in Swagger
        """

        self._encryption_type = None
        self._target_origin = None

        self.encryption_type = encryption_type
        if target_origin is not None:
          self.target_origin = target_origin

    @property
    def encryption_type(self):
        """
        Gets the encryption_type of this GeneratePublicKeyRequest.
        How the card number should be encrypted in the subsequent Tokenize Card request. Possible values are RsaOaep256 or None (if using this value the card number must be in plain text when included in the Tokenize Card request). The Tokenize Card request uses a secure connection (TLS 1.2+) regardless of what encryption type is specified.

        :return: The encryption_type of this GeneratePublicKeyRequest.
        :rtype: str
        """
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        """
        Sets the encryption_type of this GeneratePublicKeyRequest.
        How the card number should be encrypted in the subsequent Tokenize Card request. Possible values are RsaOaep256 or None (if using this value the card number must be in plain text when included in the Tokenize Card request). The Tokenize Card request uses a secure connection (TLS 1.2+) regardless of what encryption type is specified.

        :param encryption_type: The encryption_type of this GeneratePublicKeyRequest.
        :type: str
        """
        if encryption_type is None:
            raise ValueError("Invalid value for `encryption_type`, must not be `None`")

        self._encryption_type = encryption_type

    @property
    def target_origin(self):
        """
        Gets the target_origin of this GeneratePublicKeyRequest.
        The merchant origin (e.g. https://example.com) used to integrate with Flex API. Required to comply with CORS and CSP standards.

        :return: The target_origin of this GeneratePublicKeyRequest.
        :rtype: str
        """
        return self._target_origin

    @target_origin.setter
    def target_origin(self, target_origin):
        """
        Sets the target_origin of this GeneratePublicKeyRequest.
        The merchant origin (e.g. https://example.com) used to integrate with Flex API. Required to comply with CORS and CSP standards.

        :param target_origin: The target_origin of this GeneratePublicKeyRequest.
        :type: str
        """

        self._target_origin = target_origin

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GeneratePublicKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
