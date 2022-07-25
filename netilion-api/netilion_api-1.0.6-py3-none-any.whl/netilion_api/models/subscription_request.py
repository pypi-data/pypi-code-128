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


class SubscriptionRequest(object):
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
        'user': 'NestedID',
        'client_application': 'NestedID',
        'billing_address': 'BillingAddressRequest',
        'shipping_address': 'ShippingAddressRequest',
        'successor': 'NestedID',
        'predecessor': 'NestedID',
        'customer': 'NestedID'
    }

    attribute_map = {
        'user': 'user',
        'client_application': 'client_application',
        'billing_address': 'billing_address',
        'shipping_address': 'shipping_address',
        'successor': 'successor',
        'predecessor': 'predecessor',
        'customer': 'customer'
    }

    def __init__(self, user=None, client_application=None, billing_address=None, shipping_address=None, successor=None, predecessor=None, customer=None, _configuration=None):  # noqa: E501
        """SubscriptionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user = None
        self._client_application = None
        self._billing_address = None
        self._shipping_address = None
        self._successor = None
        self._predecessor = None
        self._customer = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if client_application is not None:
            self.client_application = client_application
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if successor is not None:
            self.successor = successor
        if predecessor is not None:
            self.predecessor = predecessor
        if customer is not None:
            self.customer = customer

    @property
    def user(self):
        """Gets the user of this SubscriptionRequest.  # noqa: E501


        :return: The user of this SubscriptionRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SubscriptionRequest.


        :param user: The user of this SubscriptionRequest.  # noqa: E501
        :type: NestedID
        """

        self._user = user

    @property
    def client_application(self):
        """Gets the client_application of this SubscriptionRequest.  # noqa: E501


        :return: The client_application of this SubscriptionRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this SubscriptionRequest.


        :param client_application: The client_application of this SubscriptionRequest.  # noqa: E501
        :type: NestedID
        """

        self._client_application = client_application

    @property
    def billing_address(self):
        """Gets the billing_address of this SubscriptionRequest.  # noqa: E501


        :return: The billing_address of this SubscriptionRequest.  # noqa: E501
        :rtype: BillingAddressRequest
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this SubscriptionRequest.


        :param billing_address: The billing_address of this SubscriptionRequest.  # noqa: E501
        :type: BillingAddressRequest
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this SubscriptionRequest.  # noqa: E501


        :return: The shipping_address of this SubscriptionRequest.  # noqa: E501
        :rtype: ShippingAddressRequest
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this SubscriptionRequest.


        :param shipping_address: The shipping_address of this SubscriptionRequest.  # noqa: E501
        :type: ShippingAddressRequest
        """

        self._shipping_address = shipping_address

    @property
    def successor(self):
        """Gets the successor of this SubscriptionRequest.  # noqa: E501


        :return: The successor of this SubscriptionRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._successor

    @successor.setter
    def successor(self, successor):
        """Sets the successor of this SubscriptionRequest.


        :param successor: The successor of this SubscriptionRequest.  # noqa: E501
        :type: NestedID
        """

        self._successor = successor

    @property
    def predecessor(self):
        """Gets the predecessor of this SubscriptionRequest.  # noqa: E501


        :return: The predecessor of this SubscriptionRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._predecessor

    @predecessor.setter
    def predecessor(self, predecessor):
        """Sets the predecessor of this SubscriptionRequest.


        :param predecessor: The predecessor of this SubscriptionRequest.  # noqa: E501
        :type: NestedID
        """

        self._predecessor = predecessor

    @property
    def customer(self):
        """Gets the customer of this SubscriptionRequest.  # noqa: E501


        :return: The customer of this SubscriptionRequest.  # noqa: E501
        :rtype: NestedID
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SubscriptionRequest.


        :param customer: The customer of this SubscriptionRequest.  # noqa: E501
        :type: NestedID
        """

        self._customer = customer

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
        if issubclass(SubscriptionRequest, dict):
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
        if not isinstance(other, SubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
