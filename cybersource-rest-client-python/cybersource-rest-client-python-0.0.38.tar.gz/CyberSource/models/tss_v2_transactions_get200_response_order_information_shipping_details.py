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


class TssV2TransactionsGet200ResponseOrderInformationShippingDetails(object):
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
        'gift_wrap': 'bool',
        'shipping_method': 'str'
    }

    attribute_map = {
        'gift_wrap': 'giftWrap',
        'shipping_method': 'shippingMethod'
    }

    def __init__(self, gift_wrap=None, shipping_method=None):
        """
        TssV2TransactionsGet200ResponseOrderInformationShippingDetails - a model defined in Swagger
        """

        self._gift_wrap = None
        self._shipping_method = None

        if gift_wrap is not None:
          self.gift_wrap = gift_wrap
        if shipping_method is not None:
          self.shipping_method = shipping_method

    @property
    def gift_wrap(self):
        """
        Gets the gift_wrap of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        Boolean that indicates whether the customer requested gift wrapping for this purchase. This field can contain one of the following values: - true: The customer requested gift wrapping. - false: The customer did not request gift wrapping. 

        :return: The gift_wrap of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        :rtype: bool
        """
        return self._gift_wrap

    @gift_wrap.setter
    def gift_wrap(self, gift_wrap):
        """
        Sets the gift_wrap of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        Boolean that indicates whether the customer requested gift wrapping for this purchase. This field can contain one of the following values: - true: The customer requested gift wrapping. - false: The customer did not request gift wrapping. 

        :param gift_wrap: The gift_wrap of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        :type: bool
        """

        self._gift_wrap = gift_wrap

    @property
    def shipping_method(self):
        """
        Gets the shipping_method of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        Shipping method for the product. Possible values:   - `lowcost`: Lowest-cost service  - `sameday`: Courier or same-day service  - `oneday`: Next-day or overnight service  - `twoday`: Two-day service  - `threeday`: Three-day service  - `pickup`: Store pick-up  - `other`: Other shipping method  - `none`: No shipping method because product is a service or subscription 

        :return: The shipping_method of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """
        Sets the shipping_method of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        Shipping method for the product. Possible values:   - `lowcost`: Lowest-cost service  - `sameday`: Courier or same-day service  - `oneday`: Next-day or overnight service  - `twoday`: Two-day service  - `threeday`: Three-day service  - `pickup`: Store pick-up  - `other`: Other shipping method  - `none`: No shipping method because product is a service or subscription 

        :param shipping_method: The shipping_method of this TssV2TransactionsGet200ResponseOrderInformationShippingDetails.
        :type: str
        """

        self._shipping_method = shipping_method

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
        if not isinstance(other, TssV2TransactionsGet200ResponseOrderInformationShippingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
