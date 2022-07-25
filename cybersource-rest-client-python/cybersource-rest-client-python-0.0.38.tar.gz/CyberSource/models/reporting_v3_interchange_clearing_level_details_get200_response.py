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


class ReportingV3InterchangeClearingLevelDetailsGet200Response(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'interchange_clearing_level_details': 'list[ReportingV3InterchangeClearingLevelDetailsGet200ResponseInterchangeClearingLevelDetails]'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'interchange_clearing_level_details': 'interchangeClearingLevelDetails'
    }

    def __init__(self, start_date=None, end_date=None, interchange_clearing_level_details=None):
        """
        ReportingV3InterchangeClearingLevelDetailsGet200Response - a model defined in Swagger
        """

        self._start_date = None
        self._end_date = None
        self._interchange_clearing_level_details = None

        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date
        if interchange_clearing_level_details is not None:
          self.interchange_clearing_level_details = interchange_clearing_level_details

    @property
    def start_date(self):
        """
        Gets the start_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        Valid report Start Date in **ISO 8601 format**. Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14  **Example:** - yyyy-MM-dd'T'HH:mm:ss.SSSZZ 

        :return: The start_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        Valid report Start Date in **ISO 8601 format**. Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14  **Example:** - yyyy-MM-dd'T'HH:mm:ss.SSSZZ 

        :param start_date: The start_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        Valid report Start Date in **ISO 8601 format**. 

        :return: The end_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        Valid report Start Date in **ISO 8601 format**. 

        :param end_date: The end_date of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :type: datetime
        """

        self._end_date = end_date

    @property
    def interchange_clearing_level_details(self):
        """
        Gets the interchange_clearing_level_details of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        List of InterchangeClearingLevelDetail

        :return: The interchange_clearing_level_details of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :rtype: list[ReportingV3InterchangeClearingLevelDetailsGet200ResponseInterchangeClearingLevelDetails]
        """
        return self._interchange_clearing_level_details

    @interchange_clearing_level_details.setter
    def interchange_clearing_level_details(self, interchange_clearing_level_details):
        """
        Sets the interchange_clearing_level_details of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        List of InterchangeClearingLevelDetail

        :param interchange_clearing_level_details: The interchange_clearing_level_details of this ReportingV3InterchangeClearingLevelDetailsGet200Response.
        :type: list[ReportingV3InterchangeClearingLevelDetailsGet200ResponseInterchangeClearingLevelDetails]
        """

        self._interchange_clearing_level_details = interchange_clearing_level_details

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
        if not isinstance(other, ReportingV3InterchangeClearingLevelDetailsGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
