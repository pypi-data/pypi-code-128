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


class PtsV2PaymentsPost201ResponseProcessorInformationAchVerification(object):
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
        'result_code': 'str',
        'result_code_raw': 'str'
    }

    attribute_map = {
        'result_code': 'resultCode',
        'result_code_raw': 'resultCodeRaw'
    }

    def __init__(self, result_code=None, result_code_raw=None):
        """
        PtsV2PaymentsPost201ResponseProcessorInformationAchVerification - a model defined in Swagger
        """

        self._result_code = None
        self._result_code_raw = None

        if result_code is not None:
          self.result_code = result_code
        if result_code_raw is not None:
          self.result_code_raw = result_code_raw

    @property
    def result_code(self):
        """
        Gets the result_code of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        Results from the ACH verification service. For details about this service and the possible values for the results, see \"ACH Verification\" and \"Verification Codes\" in the [Electronic Check Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/). 

        :return: The result_code of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """
        Sets the result_code of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        Results from the ACH verification service. For details about this service and the possible values for the results, see \"ACH Verification\" and \"Verification Codes\" in the [Electronic Check Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/). 

        :param result_code: The result_code of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        :type: str
        """

        self._result_code = result_code

    @property
    def result_code_raw(self):
        """
        Gets the result_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        Raw results from the ACH verification service. For details about this service and the possible values for the raw results, see \"ACH Verification\" and \"Verification Codes\" in the [Electronic Check Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/). 

        :return: The result_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        :rtype: str
        """
        return self._result_code_raw

    @result_code_raw.setter
    def result_code_raw(self, result_code_raw):
        """
        Sets the result_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        Raw results from the ACH verification service. For details about this service and the possible values for the raw results, see \"ACH Verification\" and \"Verification Codes\" in the [Electronic Check Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/EChecks_SCMP_API/html/). 

        :param result_code_raw: The result_code_raw of this PtsV2PaymentsPost201ResponseProcessorInformationAchVerification.
        :type: str
        """

        self._result_code_raw = result_code_raw

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseProcessorInformationAchVerification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
