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


class FxForwardCurveByQuoteReference(object):
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
        'dom_ccy': 'str',
        'fgn_ccy': 'str',
        'tenors': 'list[str]',
        'quote_references': 'list[dict(str, str)]',
        'lineage': 'str',
        'market_data_type': 'str'
    }

    attribute_map = {
        'dom_ccy': 'domCcy',
        'fgn_ccy': 'fgnCcy',
        'tenors': 'tenors',
        'quote_references': 'quoteReferences',
        'lineage': 'lineage',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'dom_ccy': 'required',
        'fgn_ccy': 'required',
        'tenors': 'required',
        'quote_references': 'required',
        'lineage': 'optional',
        'market_data_type': 'required'
    }

    def __init__(self, dom_ccy=None, fgn_ccy=None, tenors=None, quote_references=None, lineage=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardCurveByQuoteReference - a model defined in OpenAPI"
        
        :param dom_ccy:  Domestic currency of the fx forward (required)
        :type dom_ccy: str
        :param fgn_ccy:  Foreign currency of the fx forward (required)
        :type fgn_ccy: str
        :param tenors:  Tenors for which the forward rates apply (required)
        :type tenors: list[str]
        :param quote_references:  For each tenor, a list of identifiers. These will be looked up in the quotes store to resolve the actual rates. (required)
        :type quote_references: list[dict(str, str)]
        :param lineage:  Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dom_ccy = None
        self._fgn_ccy = None
        self._tenors = None
        self._quote_references = None
        self._lineage = None
        self._market_data_type = None
        self.discriminator = None

        self.dom_ccy = dom_ccy
        self.fgn_ccy = fgn_ccy
        self.tenors = tenors
        self.quote_references = quote_references
        self.lineage = lineage
        self.market_data_type = market_data_type

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501

        Domestic currency of the fx forward  # noqa: E501

        :return: The dom_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxForwardCurveByQuoteReference.

        Domestic currency of the fx forward  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501

        Foreign currency of the fx forward  # noqa: E501

        :return: The fgn_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxForwardCurveByQuoteReference.

        Foreign currency of the fx forward  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def tenors(self):
        """Gets the tenors of this FxForwardCurveByQuoteReference.  # noqa: E501

        Tenors for which the forward rates apply  # noqa: E501

        :return: The tenors of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenors

    @tenors.setter
    def tenors(self, tenors):
        """Sets the tenors of this FxForwardCurveByQuoteReference.

        Tenors for which the forward rates apply  # noqa: E501

        :param tenors: The tenors of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type tenors: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tenors is None:  # noqa: E501
            raise ValueError("Invalid value for `tenors`, must not be `None`")  # noqa: E501

        self._tenors = tenors

    @property
    def quote_references(self):
        """Gets the quote_references of this FxForwardCurveByQuoteReference.  # noqa: E501

        For each tenor, a list of identifiers. These will be looked up in the quotes store to resolve the actual rates.  # noqa: E501

        :return: The quote_references of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._quote_references

    @quote_references.setter
    def quote_references(self, quote_references):
        """Sets the quote_references of this FxForwardCurveByQuoteReference.

        For each tenor, a list of identifiers. These will be looked up in the quotes store to resolve the actual rates.  # noqa: E501

        :param quote_references: The quote_references of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type quote_references: list[dict(str, str)]
        """
        if self.local_vars_configuration.client_side_validation and quote_references is None:  # noqa: E501
            raise ValueError("Invalid value for `quote_references`, must not be `None`")  # noqa: E501

        self._quote_references = quote_references

    @property
    def lineage(self):
        """Gets the lineage of this FxForwardCurveByQuoteReference.  # noqa: E501

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this FxForwardCurveByQuoteReference.

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type lineage: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) > 1024):
            raise ValueError("Invalid value for `lineage`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) < 0):
            raise ValueError("Invalid value for `lineage`, length must be greater than or equal to `0`")  # noqa: E501

        self._lineage = lineage

    @property
    def market_data_type(self):
        """Gets the market_data_type of this FxForwardCurveByQuoteReference.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :return: The market_data_type of this FxForwardCurveByQuoteReference.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this FxForwardCurveByQuoteReference.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :param market_data_type: The market_data_type of this FxForwardCurveByQuoteReference.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, FxForwardCurveByQuoteReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardCurveByQuoteReference):
            return True

        return self.to_dict() != other.to_dict()
