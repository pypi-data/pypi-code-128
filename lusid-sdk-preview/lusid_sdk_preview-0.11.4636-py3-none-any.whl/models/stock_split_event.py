# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4636
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


class StockSplitEvent(object):
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
        'equity_split_ratio': 'float',
        'payment_date': 'datetime',
        'record_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'equity_split_ratio': 'equitySplitRatio',
        'payment_date': 'paymentDate',
        'record_date': 'recordDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'equity_split_ratio': 'required',
        'payment_date': 'required',
        'record_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, equity_split_ratio=None, payment_date=None, record_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """StockSplitEvent - a model defined in OpenAPI"
        
        :param equity_split_ratio:  This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old. (required)
        :type equity_split_ratio: float
        :param payment_date:  Date on which the stock-split takes effect. (required)
        :type payment_date: datetime
        :param record_date:  Date you have to be the holder of record in order to participate in the tender. (required)
        :type record_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._equity_split_ratio = None
        self._payment_date = None
        self._record_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.equity_split_ratio = equity_split_ratio
        self.payment_date = payment_date
        self.record_date = record_date
        self.instrument_event_type = instrument_event_type

    @property
    def equity_split_ratio(self):
        """Gets the equity_split_ratio of this StockSplitEvent.  # noqa: E501

        This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old.  # noqa: E501

        :return: The equity_split_ratio of this StockSplitEvent.  # noqa: E501
        :rtype: float
        """
        return self._equity_split_ratio

    @equity_split_ratio.setter
    def equity_split_ratio(self, equity_split_ratio):
        """Sets the equity_split_ratio of this StockSplitEvent.

        This number describes the rate at which the company will be dividing their current shares outstanding. It is displayed as new shares per old.  # noqa: E501

        :param equity_split_ratio: The equity_split_ratio of this StockSplitEvent.  # noqa: E501
        :type equity_split_ratio: float
        """
        if self.local_vars_configuration.client_side_validation and equity_split_ratio is None:  # noqa: E501
            raise ValueError("Invalid value for `equity_split_ratio`, must not be `None`")  # noqa: E501

        self._equity_split_ratio = equity_split_ratio

    @property
    def payment_date(self):
        """Gets the payment_date of this StockSplitEvent.  # noqa: E501

        Date on which the stock-split takes effect.  # noqa: E501

        :return: The payment_date of this StockSplitEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this StockSplitEvent.

        Date on which the stock-split takes effect.  # noqa: E501

        :param payment_date: The payment_date of this StockSplitEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def record_date(self):
        """Gets the record_date of this StockSplitEvent.  # noqa: E501

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :return: The record_date of this StockSplitEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this StockSplitEvent.

        Date you have to be the holder of record in order to participate in the tender.  # noqa: E501

        :param record_date: The record_date of this StockSplitEvent.  # noqa: E501
        :type record_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and record_date is None:  # noqa: E501
            raise ValueError("Invalid value for `record_date`, must not be `None`")  # noqa: E501

        self._record_date = record_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this StockSplitEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent  # noqa: E501

        :return: The instrument_event_type of this StockSplitEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this StockSplitEvent.

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this StockSplitEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InternalEvent", "CouponEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, StockSplitEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StockSplitEvent):
            return True

        return self.to_dict() != other.to_dict()
