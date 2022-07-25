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


class Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions(object):
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
        'sec_code': 'str'
    }

    attribute_map = {
        'sec_code': 'SECCode'
    }

    def __init__(self, sec_code=None):
        """
        Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions - a model defined in Swagger
        """

        self._sec_code = None

        if sec_code is not None:
          self.sec_code = sec_code

    @property
    def sec_code(self):
        """
        Gets the sec_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions.
        Specifies the authorization method for the transaction.  #### TeleCheck Valid values: - `ARC`: account receivable conversion - `CCD`: corporate cash disbursement - `POP`: point of purchase conversion - `PPD`: prearranged payment and deposit entry - `TEL`: telephone-initiated entry - `WEB`: internet-initiated entry  For details, see `ecp_sec_code` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :return: The sec_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._sec_code

    @sec_code.setter
    def sec_code(self, sec_code):
        """
        Sets the sec_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions.
        Specifies the authorization method for the transaction.  #### TeleCheck Valid values: - `ARC`: account receivable conversion - `CCD`: corporate cash disbursement - `POP`: point of purchase conversion - `PPD`: prearranged payment and deposit entry - `TEL`: telephone-initiated entry - `WEB`: internet-initiated entry  For details, see `ecp_sec_code` field description in the [Electronic Check Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/) 

        :param sec_code: The sec_code of this Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions.
        :type: str
        """

        self._sec_code = sec_code

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformationBankTransferOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
