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


class TssV2TransactionsGet200ResponseConsumerAuthenticationInformation(object):
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
        'eci_raw': 'str',
        'cavv': 'str',
        'xid': 'str',
        'transaction_id': 'str',
        'strong_authentication': 'TssV2TransactionsGet200ResponseConsumerAuthenticationInformationStrongAuthentication'
    }

    attribute_map = {
        'eci_raw': 'eciRaw',
        'cavv': 'cavv',
        'xid': 'xid',
        'transaction_id': 'transactionId',
        'strong_authentication': 'strongAuthentication'
    }

    def __init__(self, eci_raw=None, cavv=None, xid=None, transaction_id=None, strong_authentication=None):
        """
        TssV2TransactionsGet200ResponseConsumerAuthenticationInformation - a model defined in Swagger
        """

        self._eci_raw = None
        self._cavv = None
        self._xid = None
        self._transaction_id = None
        self._strong_authentication = None

        if eci_raw is not None:
          self.eci_raw = eci_raw
        if cavv is not None:
          self.cavv = cavv
        if xid is not None:
          self.xid = xid
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if strong_authentication is not None:
          self.strong_authentication = strong_authentication

    @property
    def eci_raw(self):
        """
        Gets the eci_raw of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Raw electronic commerce indicator (ECI).  For details, see `eci_raw` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The eci_raw of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._eci_raw

    @eci_raw.setter
    def eci_raw(self, eci_raw):
        """
        Sets the eci_raw of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Raw electronic commerce indicator (ECI).  For details, see `eci_raw` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param eci_raw: The eci_raw of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :type: str
        """

        self._eci_raw = eci_raw

    @property
    def cavv(self):
        """
        Gets the cavv of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Cardholder authentication verification value (CAVV).

        :return: The cavv of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """
        Sets the cavv of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Cardholder authentication verification value (CAVV).

        :param cavv: The cavv of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :type: str
        """

        self._cavv = cavv

    @property
    def xid(self):
        """
        Gets the xid of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Transaction identifier.  For details, see `xid` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The xid of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """
        Sets the xid of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Transaction identifier.  For details, see `xid` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param xid: The xid of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :type: str
        """

        self._xid = xid

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Payer auth Transaction identifier.

        :return: The transaction_id of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        Payer auth Transaction identifier.

        :param transaction_id: The transaction_id of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def strong_authentication(self):
        """
        Gets the strong_authentication of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.

        :return: The strong_authentication of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :rtype: TssV2TransactionsGet200ResponseConsumerAuthenticationInformationStrongAuthentication
        """
        return self._strong_authentication

    @strong_authentication.setter
    def strong_authentication(self, strong_authentication):
        """
        Sets the strong_authentication of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.

        :param strong_authentication: The strong_authentication of this TssV2TransactionsGet200ResponseConsumerAuthenticationInformation.
        :type: TssV2TransactionsGet200ResponseConsumerAuthenticationInformationStrongAuthentication
        """

        self._strong_authentication = strong_authentication

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
        if not isinstance(other, TssV2TransactionsGet200ResponseConsumerAuthenticationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
