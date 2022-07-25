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


class V1FileDetailsGet200Response(object):
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
        'file_details': 'list[V1FileDetailsGet200ResponseFileDetails]',
        'links': 'V1FileDetailsGet200ResponseLinks'
    }

    attribute_map = {
        'file_details': 'fileDetails',
        'links': '_links'
    }

    def __init__(self, file_details=None, links=None):
        """
        V1FileDetailsGet200Response - a model defined in Swagger
        """

        self._file_details = None
        self._links = None

        if file_details is not None:
          self.file_details = file_details
        if links is not None:
          self.links = links

    @property
    def file_details(self):
        """
        Gets the file_details of this V1FileDetailsGet200Response.

        :return: The file_details of this V1FileDetailsGet200Response.
        :rtype: list[V1FileDetailsGet200ResponseFileDetails]
        """
        return self._file_details

    @file_details.setter
    def file_details(self, file_details):
        """
        Sets the file_details of this V1FileDetailsGet200Response.

        :param file_details: The file_details of this V1FileDetailsGet200Response.
        :type: list[V1FileDetailsGet200ResponseFileDetails]
        """

        self._file_details = file_details

    @property
    def links(self):
        """
        Gets the links of this V1FileDetailsGet200Response.

        :return: The links of this V1FileDetailsGet200Response.
        :rtype: V1FileDetailsGet200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this V1FileDetailsGet200Response.

        :param links: The links of this V1FileDetailsGet200Response.
        :type: V1FileDetailsGet200ResponseLinks
        """

        self._links = links

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
        if not isinstance(other, V1FileDetailsGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
