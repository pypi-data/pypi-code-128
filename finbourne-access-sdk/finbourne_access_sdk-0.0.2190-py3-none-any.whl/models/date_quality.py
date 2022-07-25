# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2190
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

from finbourne_access.configuration import Configuration


class DateQuality(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNDEFINED = "Undefined"
    ISFIRSTDAYOFANYMONTH = "IsFirstDayOfAnyMonth"
    ISLASTDAYOFANYMONTH = "IsLastDayOfAnyMonth"
    ISBUSINESSDAYOFANYMONTH = "IsBusinessDayOfAnyMonth"
    ISFIRSTDAYOFTHECURRENTMONTH = "IsFirstDayOfTheCurrentMonth"
    ISLASTDAYOFTHECURRENTMONTH = "IsLastDayOfTheCurrentMonth"
    ISBUSINESSDAYOFTHECURRENTMONTH = "IsBusinessDayOfTheCurrentMonth"
    ISBEFOREMIDDAY = "IsBeforeMidday"
    ISBEFORE5PM = "IsBefore5pm"
    ISAFTER5PM = "IsAfter5pm"

    allowable_values = [UNDEFINED, ISFIRSTDAYOFANYMONTH, ISLASTDAYOFANYMONTH, ISBUSINESSDAYOFANYMONTH, ISFIRSTDAYOFTHECURRENTMONTH, ISLASTDAYOFTHECURRENTMONTH, ISBUSINESSDAYOFTHECURRENTMONTH, ISBEFOREMIDDAY, ISBEFORE5PM, ISAFTER5PM]  # noqa: E501

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
    }

    attribute_map = {
    }

    required_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """DateQuality - a model defined in OpenAPI"
        

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, DateQuality):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateQuality):
            return True

        return self.to_dict() != other.to_dict()
