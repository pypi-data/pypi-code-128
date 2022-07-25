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


class Links10(object):
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
        'assets': 'Link',
        'documents': 'Link',
        'instrumentations': 'Link',
        'specifications': 'Link'
    }

    attribute_map = {
        'assets': 'assets',
        'documents': 'documents',
        'instrumentations': 'instrumentations',
        'specifications': 'specifications'
    }

    def __init__(self, assets=None, documents=None, instrumentations=None, specifications=None, _configuration=None):  # noqa: E501
        """Links10 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assets = None
        self._documents = None
        self._instrumentations = None
        self._specifications = None
        self.discriminator = None

        self.assets = assets
        if documents is not None:
            self.documents = documents
        if instrumentations is not None:
            self.instrumentations = instrumentations
        if specifications is not None:
            self.specifications = specifications

    @property
    def assets(self):
        """Gets the assets of this Links10.  # noqa: E501


        :return: The assets of this Links10.  # noqa: E501
        :rtype: Link
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Links10.


        :param assets: The assets of this Links10.  # noqa: E501
        :type: Link
        """
        if self._configuration.client_side_validation and assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501

        self._assets = assets

    @property
    def documents(self):
        """Gets the documents of this Links10.  # noqa: E501


        :return: The documents of this Links10.  # noqa: E501
        :rtype: Link
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Links10.


        :param documents: The documents of this Links10.  # noqa: E501
        :type: Link
        """

        self._documents = documents

    @property
    def instrumentations(self):
        """Gets the instrumentations of this Links10.  # noqa: E501


        :return: The instrumentations of this Links10.  # noqa: E501
        :rtype: Link
        """
        return self._instrumentations

    @instrumentations.setter
    def instrumentations(self, instrumentations):
        """Sets the instrumentations of this Links10.


        :param instrumentations: The instrumentations of this Links10.  # noqa: E501
        :type: Link
        """

        self._instrumentations = instrumentations

    @property
    def specifications(self):
        """Gets the specifications of this Links10.  # noqa: E501


        :return: The specifications of this Links10.  # noqa: E501
        :rtype: Link
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this Links10.


        :param specifications: The specifications of this Links10.  # noqa: E501
        :type: Link
        """

        self._specifications = specifications

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
        if issubclass(Links10, dict):
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
        if not isinstance(other, Links10):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Links10):
            return True

        return self.to_dict() != other.to_dict()
