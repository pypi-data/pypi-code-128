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


class PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation(object):
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
        'account_features': 'PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformationAccountFeatures'
    }

    attribute_map = {
        'account_features': 'accountFeatures'
    }

    def __init__(self, account_features=None):
        """
        PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation - a model defined in Swagger
        """

        self._account_features = None

        if account_features is not None:
          self.account_features = account_features

    @property
    def account_features(self):
        """
        Gets the account_features of this PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation.

        :return: The account_features of this PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformationAccountFeatures
        """
        return self._account_features

    @account_features.setter
    def account_features(self, account_features):
        """
        Sets the account_features of this PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation.

        :param account_features: The account_features of this PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation.
        :type: PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformationAccountFeatures
        """

        self._account_features = account_features

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
        if not isinstance(other, PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
