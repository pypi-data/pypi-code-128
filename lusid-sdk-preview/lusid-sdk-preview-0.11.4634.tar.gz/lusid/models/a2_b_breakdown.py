# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4634
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


class A2BBreakdown(object):
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
        'total': 'float',
        'currency': 'str',
        'components': 'dict(str, float)'
    }

    attribute_map = {
        'total': 'total',
        'currency': 'currency',
        'components': 'components'
    }

    required_map = {
        'total': 'optional',
        'currency': 'optional',
        'components': 'optional'
    }

    def __init__(self, total=None, currency=None, components=None, local_vars_configuration=None):  # noqa: E501
        """A2BBreakdown - a model defined in OpenAPI"
        
        :param total:  The total value of all the components within this category.
        :type total: float
        :param currency:  The currency. Applies to the Total, as well as all the componenents.
        :type currency: str
        :param components:  The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components.
        :type components: dict(str, float)

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._currency = None
        self._components = None
        self.discriminator = None

        if total is not None:
            self.total = total
        self.currency = currency
        self.components = components

    @property
    def total(self):
        """Gets the total of this A2BBreakdown.  # noqa: E501

        The total value of all the components within this category.  # noqa: E501

        :return: The total of this A2BBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this A2BBreakdown.

        The total value of all the components within this category.  # noqa: E501

        :param total: The total of this A2BBreakdown.  # noqa: E501
        :type total: float
        """

        self._total = total

    @property
    def currency(self):
        """Gets the currency of this A2BBreakdown.  # noqa: E501

        The currency. Applies to the Total, as well as all the componenents.  # noqa: E501

        :return: The currency of this A2BBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this A2BBreakdown.

        The currency. Applies to the Total, as well as all the componenents.  # noqa: E501

        :param currency: The currency of this A2BBreakdown.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

    @property
    def components(self):
        """Gets the components of this A2BBreakdown.  # noqa: E501

        The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components.  # noqa: E501

        :return: The components of this A2BBreakdown.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this A2BBreakdown.

        The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components.  # noqa: E501

        :param components: The components of this A2BBreakdown.  # noqa: E501
        :type components: dict(str, float)
        """

        self._components = components

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
        if not isinstance(other, A2BBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, A2BBreakdown):
            return True

        return self.to_dict() != other.to_dict()
