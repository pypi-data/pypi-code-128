# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4633
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class MarketContextSuppliers(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'commodity': 'str',
        'credit': 'str',
        'equity': 'str',
        'fx': 'str',
        'rates': 'str'
    }

    attribute_map = {
        'commodity': 'Commodity',
        'credit': 'Credit',
        'equity': 'Equity',
        'fx': 'Fx',
        'rates': 'Rates'
    }

    required_map = {
        'commodity': 'optional',
        'credit': 'optional',
        'equity': 'optional',
        'fx': 'optional',
        'rates': 'optional'
    }

    def __init__(self, commodity=None, credit=None, equity=None, fx=None, rates=None, local_vars_configuration=None):  # noqa: E501
        """MarketContextSuppliers - a model defined in OpenAPI"
        
        :param commodity: 
        :type commodity: str
        :param credit: 
        :type credit: str
        :param equity: 
        :type equity: str
        :param fx: 
        :type fx: str
        :param rates: 
        :type rates: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._commodity = None
        self._credit = None
        self._equity = None
        self._fx = None
        self._rates = None
        self.discriminator = None

        if commodity is not None:
            self.commodity = commodity
        if credit is not None:
            self.credit = credit
        if equity is not None:
            self.equity = equity
        if fx is not None:
            self.fx = fx
        if rates is not None:
            self.rates = rates

    @property
    def commodity(self):
        """Gets the commodity of this MarketContextSuppliers.  # noqa: E501


        :return: The commodity of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._commodity

    @commodity.setter
    def commodity(self, commodity):
        """Sets the commodity of this MarketContextSuppliers.


        :param commodity: The commodity of this MarketContextSuppliers.  # noqa: E501
        :type commodity: str
        """

        self._commodity = commodity

    @property
    def credit(self):
        """Gets the credit of this MarketContextSuppliers.  # noqa: E501


        :return: The credit of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this MarketContextSuppliers.


        :param credit: The credit of this MarketContextSuppliers.  # noqa: E501
        :type credit: str
        """

        self._credit = credit

    @property
    def equity(self):
        """Gets the equity of this MarketContextSuppliers.  # noqa: E501


        :return: The equity of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this MarketContextSuppliers.


        :param equity: The equity of this MarketContextSuppliers.  # noqa: E501
        :type equity: str
        """

        self._equity = equity

    @property
    def fx(self):
        """Gets the fx of this MarketContextSuppliers.  # noqa: E501


        :return: The fx of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._fx

    @fx.setter
    def fx(self, fx):
        """Sets the fx of this MarketContextSuppliers.


        :param fx: The fx of this MarketContextSuppliers.  # noqa: E501
        :type fx: str
        """

        self._fx = fx

    @property
    def rates(self):
        """Gets the rates of this MarketContextSuppliers.  # noqa: E501


        :return: The rates of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this MarketContextSuppliers.


        :param rates: The rates of this MarketContextSuppliers.  # noqa: E501
        :type rates: str
        """

        self._rates = rates

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarketContextSuppliers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketContextSuppliers):
            return True

        return self.to_dict() != other.to_dict()
