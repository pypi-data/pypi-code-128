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


class PtsV2PayoutsPost201ResponseRecipientInformationCard(object):
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
        'balance': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'balance': 'balance',
        'currency': 'currency'
    }

    def __init__(self, balance=None, currency=None):
        """
        PtsV2PayoutsPost201ResponseRecipientInformationCard - a model defined in Swagger
        """

        self._balance = None
        self._currency = None

        if balance is not None:
          self.balance = balance
        if currency is not None:
          self.currency = currency

    @property
    def balance(self):
        """
        Gets the balance of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        This field shows the available balance in the prepaid account. Acquirers always receive the available balance in the transaction currency. 

        :return: The balance of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        This field shows the available balance in the prepaid account. Acquirers always receive the available balance in the transaction currency. 

        :param balance: The balance of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        :type: str
        """

        self._balance = balance

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer. 

        :return: The currency of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer. 

        :param currency: The currency of this PtsV2PayoutsPost201ResponseRecipientInformationCard.
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, PtsV2PayoutsPost201ResponseRecipientInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
