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


class VasV2PaymentsPost201ResponseOrderInformationJurisdiction(object):
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
        'type': 'str',
        'tax_name': 'str',
        'tax_amount': 'str',
        'taxable': 'str',
        'name': 'str',
        'code': 'str',
        'rate': 'str',
        'region': 'str',
        'country': 'str'
    }

    attribute_map = {
        'type': 'type',
        'tax_name': 'taxName',
        'tax_amount': 'taxAmount',
        'taxable': 'taxable',
        'name': 'name',
        'code': 'code',
        'rate': 'rate',
        'region': 'region',
        'country': 'country'
    }

    def __init__(self, type=None, tax_name=None, tax_amount=None, taxable=None, name=None, code=None, rate=None, region=None, country=None):
        """
        VasV2PaymentsPost201ResponseOrderInformationJurisdiction - a model defined in Swagger
        """

        self._type = None
        self._tax_name = None
        self._tax_amount = None
        self._taxable = None
        self._name = None
        self._code = None
        self._rate = None
        self._region = None
        self._country = None

        if type is not None:
          self.type = type
        if tax_name is not None:
          self.tax_name = tax_name
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if taxable is not None:
          self.taxable = taxable
        if name is not None:
          self.name = name
        if code is not None:
          self.code = code
        if rate is not None:
          self.rate = rate
        if region is not None:
          self.region = region
        if country is not None:
          self.country = country

    @property
    def type(self):
        """
        Gets the type of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Type of tax jurisdiction for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`.  Possible values: - `city` - `county` - `state` - `country` - `special` 

        :return: The type of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Type of tax jurisdiction for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`.  Possible values: - `city` - `county` - `state` - `country` - `special` 

        :param type: The type of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._type = type

    @property
    def tax_name(self):
        """
        Gets the tax_name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Name of the jurisdiction tax for the item. For example, CA State Tax. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The tax_name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._tax_name

    @tax_name.setter
    def tax_name(self, tax_name):
        """
        Sets the tax_name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Name of the jurisdiction tax for the item. For example, CA State Tax. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param tax_name: The tax_name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._tax_name = tax_name

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction tax amount for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The tax_amount of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction tax amount for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param tax_amount: The tax_amount of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def taxable(self):
        """
        Gets the taxable of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction taxable amount for the item, not including product level exemptions. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The taxable of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._taxable

    @taxable.setter
    def taxable(self, taxable):
        """
        Sets the taxable of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction taxable amount for the item, not including product level exemptions. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param taxable: The taxable of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._taxable = taxable

    @property
    def name(self):
        """
        Gets the name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Free-text description of the jurisdiction for the item. For example, San Mateo County. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Free-text description of the jurisdiction for the item. For example, San Mateo County. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param name: The name of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """
        Gets the code of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction code assigned by the tax provider. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The code of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction code assigned by the tax provider. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param code: The code of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._code = code

    @property
    def rate(self):
        """
        Gets the rate of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction tax rate for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The rate of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Jurisdiction tax rate for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param rate: The rate of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._rate = rate

    @property
    def region(self):
        """
        Gets the region of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Free-text description of the jurisdiction region for the item. For example, CA (California State) or GB (Great Britain). Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The region of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Free-text description of the jurisdiction region for the item. For example, CA (California State) or GB (Great Britain). Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param region: The region of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """
        Gets the country of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Tax jurisdiction country for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The country of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        Tax jurisdiction country for the item. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param country: The country of this VasV2PaymentsPost201ResponseOrderInformationJurisdiction.
        :type: str
        """

        self._country = country

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
        if not isinstance(other, VasV2PaymentsPost201ResponseOrderInformationJurisdiction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
