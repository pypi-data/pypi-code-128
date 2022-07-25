# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.320
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

from finbourne_insights.configuration import Configuration


class AuditEntry(object):
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
        'id': 'str',
        'date': 'datetime',
        'process': 'AuditProcess',
        'data': 'AuditData',
        'notes': 'list[AuditEntryNote]'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'process': 'process',
        'data': 'data',
        'notes': 'notes'
    }

    required_map = {
        'id': 'required',
        'date': 'required',
        'process': 'required',
        'data': 'required',
        'notes': 'optional'
    }

    def __init__(self, id=None, date=None, process=None, data=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """AuditEntry - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: str
        :param date:  (required)
        :type date: datetime
        :param process:  (required)
        :type process: finbourne_insights.AuditProcess
        :param data:  (required)
        :type data: finbourne_insights.AuditData
        :param notes: 
        :type notes: list[finbourne_insights.AuditEntryNote]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._date = None
        self._process = None
        self._data = None
        self._notes = None
        self.discriminator = None

        self.id = id
        self.date = date
        self.process = process
        self.data = data
        self.notes = notes

    @property
    def id(self):
        """Gets the id of this AuditEntry.  # noqa: E501


        :return: The id of this AuditEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditEntry.


        :param id: The id of this AuditEntry.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date(self):
        """Gets the date of this AuditEntry.  # noqa: E501


        :return: The date of this AuditEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AuditEntry.


        :param date: The date of this AuditEntry.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def process(self):
        """Gets the process of this AuditEntry.  # noqa: E501


        :return: The process of this AuditEntry.  # noqa: E501
        :rtype: finbourne_insights.AuditProcess
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this AuditEntry.


        :param process: The process of this AuditEntry.  # noqa: E501
        :type process: finbourne_insights.AuditProcess
        """
        if self.local_vars_configuration.client_side_validation and process is None:  # noqa: E501
            raise ValueError("Invalid value for `process`, must not be `None`")  # noqa: E501

        self._process = process

    @property
    def data(self):
        """Gets the data of this AuditEntry.  # noqa: E501


        :return: The data of this AuditEntry.  # noqa: E501
        :rtype: finbourne_insights.AuditData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AuditEntry.


        :param data: The data of this AuditEntry.  # noqa: E501
        :type data: finbourne_insights.AuditData
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def notes(self):
        """Gets the notes of this AuditEntry.  # noqa: E501


        :return: The notes of this AuditEntry.  # noqa: E501
        :rtype: list[finbourne_insights.AuditEntryNote]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AuditEntry.


        :param notes: The notes of this AuditEntry.  # noqa: E501
        :type notes: list[finbourne_insights.AuditEntryNote]
        """

        self._notes = notes

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
        if not isinstance(other, AuditEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditEntry):
            return True

        return self.to_dict() != other.to_dict()
