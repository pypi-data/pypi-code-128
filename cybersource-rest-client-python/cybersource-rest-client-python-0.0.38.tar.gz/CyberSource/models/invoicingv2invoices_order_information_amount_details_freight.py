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


class Invoicingv2invoicesOrderInformationAmountDetailsFreight(object):
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
        'amount': 'str',
        'taxable': 'bool'
    }

    attribute_map = {
        'amount': 'amount',
        'taxable': 'taxable'
    }

    def __init__(self, amount=None, taxable=None):
        """
        Invoicingv2invoicesOrderInformationAmountDetailsFreight - a model defined in Swagger
        """

        self._amount = None
        self._taxable = None

        if amount is not None:
          self.amount = amount
        if taxable is not None:
          self.taxable = taxable

    @property
    def amount(self):
        """
        Gets the amount of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        Total freight or shipping and handling charges for the order. When you include this field in your request, you must also include the **totalAmount** field.  For processor-specific information, see the freight_amount field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The amount of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        Total freight or shipping and handling charges for the order. When you include this field in your request, you must also include the **totalAmount** field.  For processor-specific information, see the freight_amount field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param amount: The amount of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        :type: str
        """

        self._amount = amount

    @property
    def taxable(self):
        """
        Gets the taxable of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        Flag that indicates whether an order is taxable. This value must be true if the sum of all _lineItems[].taxAmount_ values > 0.  If you do not include any `lineItems[].taxAmount` values in your request, CyberSource does not include `invoiceDetails.taxable` in the data it sends to the processor.  For processor-specific information, see the `tax_indicator` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  Possible values:  - **true**  - **false** 

        :return: The taxable of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        :rtype: bool
        """
        return self._taxable

    @taxable.setter
    def taxable(self, taxable):
        """
        Sets the taxable of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        Flag that indicates whether an order is taxable. This value must be true if the sum of all _lineItems[].taxAmount_ values > 0.  If you do not include any `lineItems[].taxAmount` values in your request, CyberSource does not include `invoiceDetails.taxable` in the data it sends to the processor.  For processor-specific information, see the `tax_indicator` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  Possible values:  - **true**  - **false** 

        :param taxable: The taxable of this Invoicingv2invoicesOrderInformationAmountDetailsFreight.
        :type: bool
        """

        self._taxable = taxable

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
        if not isinstance(other, Invoicingv2invoicesOrderInformationAmountDetailsFreight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
