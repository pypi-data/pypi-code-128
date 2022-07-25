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


class PtsV2PaymentsPost201ResponseLinks(object):
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
        '_self': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'reversal': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'capture': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'customer': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'payment_instrument': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'shipping_address': 'PtsV2PaymentsPost201ResponseLinksSelf',
        'instrument_identifier': 'PtsV2PaymentsPost201ResponseLinksSelf'
    }

    attribute_map = {
        '_self': 'self',
        'reversal': 'reversal',
        'capture': 'capture',
        'customer': 'customer',
        'payment_instrument': 'paymentInstrument',
        'shipping_address': 'shippingAddress',
        'instrument_identifier': 'instrumentIdentifier'
    }

    def __init__(self, _self=None, reversal=None, capture=None, customer=None, payment_instrument=None, shipping_address=None, instrument_identifier=None):
        """
        PtsV2PaymentsPost201ResponseLinks - a model defined in Swagger
        """

        self.__self = None
        self._reversal = None
        self._capture = None
        self._customer = None
        self._payment_instrument = None
        self._shipping_address = None
        self._instrument_identifier = None

        if _self is not None:
          self._self = _self
        if reversal is not None:
          self.reversal = reversal
        if capture is not None:
          self.capture = capture
        if customer is not None:
          self.customer = customer
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier

    @property
    def _self(self):
        """
        Gets the _self of this PtsV2PaymentsPost201ResponseLinks.

        :return: The _self of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this PtsV2PaymentsPost201ResponseLinks.

        :param _self: The _self of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self.__self = _self

    @property
    def reversal(self):
        """
        Gets the reversal of this PtsV2PaymentsPost201ResponseLinks.

        :return: The reversal of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._reversal

    @reversal.setter
    def reversal(self, reversal):
        """
        Sets the reversal of this PtsV2PaymentsPost201ResponseLinks.

        :param reversal: The reversal of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._reversal = reversal

    @property
    def capture(self):
        """
        Gets the capture of this PtsV2PaymentsPost201ResponseLinks.

        :return: The capture of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._capture

    @capture.setter
    def capture(self, capture):
        """
        Sets the capture of this PtsV2PaymentsPost201ResponseLinks.

        :param capture: The capture of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._capture = capture

    @property
    def customer(self):
        """
        Gets the customer of this PtsV2PaymentsPost201ResponseLinks.

        :return: The customer of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this PtsV2PaymentsPost201ResponseLinks.

        :param customer: The customer of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._customer = customer

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this PtsV2PaymentsPost201ResponseLinks.

        :return: The payment_instrument of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this PtsV2PaymentsPost201ResponseLinks.

        :param payment_instrument: The payment_instrument of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._payment_instrument = payment_instrument

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this PtsV2PaymentsPost201ResponseLinks.

        :return: The shipping_address of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this PtsV2PaymentsPost201ResponseLinks.

        :param shipping_address: The shipping_address of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._shipping_address = shipping_address

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this PtsV2PaymentsPost201ResponseLinks.

        :return: The instrument_identifier of this PtsV2PaymentsPost201ResponseLinks.
        :rtype: PtsV2PaymentsPost201ResponseLinksSelf
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this PtsV2PaymentsPost201ResponseLinks.

        :param instrument_identifier: The instrument_identifier of this PtsV2PaymentsPost201ResponseLinks.
        :type: PtsV2PaymentsPost201ResponseLinksSelf
        """

        self._instrument_identifier = instrument_identifier

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
