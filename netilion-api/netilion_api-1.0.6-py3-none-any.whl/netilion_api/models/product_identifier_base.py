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


class ProductIdentifierBase(object):
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
        'product_identifier': 'str',
        'organization_name': 'str',
        'protocol': 'str',
        'protocol_version': 'str'
    }

    attribute_map = {
        'product_identifier': 'product_identifier',
        'organization_name': 'organization_name',
        'protocol': 'protocol',
        'protocol_version': 'protocol_version'
    }

    discriminator_value_class_map = {
        'ProductIdentifierRequestNoProducts': 'ProductIdentifierRequestNoProducts',
        'ProductIdentifierResponse': 'ProductIdentifierResponse',
        'ProductIdentifierRequest': 'ProductIdentifierRequest'
    }

    def __init__(self, product_identifier=None, organization_name=None, protocol=None, protocol_version=None, _configuration=None):  # noqa: E501
        """ProductIdentifierBase - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_identifier = None
        self._organization_name = None
        self._protocol = None
        self._protocol_version = None
        self.discriminator = 'productIdentifierBaseType'

        self.product_identifier = product_identifier
        self.organization_name = organization_name
        if protocol is not None:
            self.protocol = protocol
        if protocol_version is not None:
            self.protocol_version = protocol_version

    @property
    def product_identifier(self):
        """Gets the product_identifier of this ProductIdentifierBase.  # noqa: E501

        Product identifiers are HEX codes registered by the defined organization.  # noqa: E501

        :return: The product_identifier of this ProductIdentifierBase.  # noqa: E501
        :rtype: str
        """
        return self._product_identifier

    @product_identifier.setter
    def product_identifier(self, product_identifier):
        """Sets the product_identifier of this ProductIdentifierBase.

        Product identifiers are HEX codes registered by the defined organization.  # noqa: E501

        :param product_identifier: The product_identifier of this ProductIdentifierBase.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_identifier is None:
            raise ValueError("Invalid value for `product_identifier`, must not be `None`")  # noqa: E501

        self._product_identifier = product_identifier

    @property
    def organization_name(self):
        """Gets the organization_name of this ProductIdentifierBase.  # noqa: E501

        Possilbe values are 'FIELDCOMM_GROUP', 'PROFIBUS_PROFINET, 'ODVA', 'MODBUS_ORGANIZATION', 'OTHER_ORGANIZATION'  # noqa: E501

        :return: The organization_name of this ProductIdentifierBase.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this ProductIdentifierBase.

        Possilbe values are 'FIELDCOMM_GROUP', 'PROFIBUS_PROFINET, 'ODVA', 'MODBUS_ORGANIZATION', 'OTHER_ORGANIZATION'  # noqa: E501

        :param organization_name: The organization_name of this ProductIdentifierBase.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and organization_name is None:
            raise ValueError("Invalid value for `organization_name`, must not be `None`")  # noqa: E501

        self._organization_name = organization_name

    @property
    def protocol(self):
        """Gets the protocol of this ProductIdentifierBase.  # noqa: E501

        Possilbe values are 'HART', 'PROFIBUS', 'ETHERNETIP', 'MODBUS', 'OTHERS'  # noqa: E501

        :return: The protocol of this ProductIdentifierBase.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ProductIdentifierBase.

        Possilbe values are 'HART', 'PROFIBUS', 'ETHERNETIP', 'MODBUS', 'OTHERS'  # noqa: E501

        :param protocol: The protocol of this ProductIdentifierBase.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def protocol_version(self):
        """Gets the protocol_version of this ProductIdentifierBase.  # noqa: E501

        For certain protocols the version needs to be defined as well.  # noqa: E501

        :return: The protocol_version of this ProductIdentifierBase.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this ProductIdentifierBase.

        For certain protocols the version needs to be defined as well.  # noqa: E501

        :param protocol_version: The protocol_version of this ProductIdentifierBase.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(ProductIdentifierBase, dict):
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
        if not isinstance(other, ProductIdentifierBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductIdentifierBase):
            return True

        return self.to_dict() != other.to_dict()
