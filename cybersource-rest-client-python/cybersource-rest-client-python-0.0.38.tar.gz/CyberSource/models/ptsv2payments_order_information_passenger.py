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


class Ptsv2paymentsOrderInformationPassenger(object):
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
        'status': 'str',
        'phone': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'id': 'str',
        'email': 'str',
        'nationality': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'phone': 'phone',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'id': 'id',
        'email': 'email',
        'nationality': 'nationality'
    }

    def __init__(self, type=None, status=None, phone=None, first_name=None, last_name=None, id=None, email=None, nationality=None):
        """
        Ptsv2paymentsOrderInformationPassenger - a model defined in Swagger
        """

        self._type = None
        self._status = None
        self._phone = None
        self._first_name = None
        self._last_name = None
        self._id = None
        self._email = None
        self._nationality = None

        if type is not None:
          self.type = type
        if status is not None:
          self.status = status
        if phone is not None:
          self.phone = phone
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if id is not None:
          self.id = id
        if email is not None:
          self.email = email
        if nationality is not None:
          self.nationality = nationality

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsOrderInformationPassenger.
        Passenger classification associated with the price of the ticket. You can use one of the following values: - `ADT`: Adult - `CNN`: Child - `INF`: Infant - `YTH`: Youth - `STU`: Student - `SCR`: Senior Citizen - `MIL`: Military 

        :return: The type of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsOrderInformationPassenger.
        Passenger classification associated with the price of the ticket. You can use one of the following values: - `ADT`: Adult - `CNN`: Child - `INF`: Infant - `YTH`: Youth - `STU`: Student - `SCR`: Senior Citizen - `MIL`: Military 

        :param type: The type of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this Ptsv2paymentsOrderInformationPassenger.
        Your company's passenger classification, such as with a frequent flyer program. In this case, you might use values such as `standard`, `gold`, or `platinum`. 

        :return: The status of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Ptsv2paymentsOrderInformationPassenger.
        Your company's passenger classification, such as with a frequent flyer program. In this case, you might use values such as `standard`, `gold`, or `platinum`. 

        :param status: The status of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._status = status

    @property
    def phone(self):
        """
        Gets the phone of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's phone number. If the order is from outside the U.S., CyberSource recommends that you include the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf). 

        :return: The phone of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's phone number. If the order is from outside the U.S., CyberSource recommends that you include the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf). 

        :param phone: The phone of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._phone = phone

    @property
    def first_name(self):
        """
        Gets the first_name of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's first name.

        :return: The first_name of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's first name.

        :param first_name: The first_name of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's last name.

        :return: The last_name of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's last name.

        :param last_name: The last_name of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._last_name = last_name

    @property
    def id(self):
        """
        Gets the id of this Ptsv2paymentsOrderInformationPassenger.
        ID of the passenger to whom the ticket was issued. For example, you can use this field for the frequent flyer number. 

        :return: The id of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ptsv2paymentsOrderInformationPassenger.
        ID of the passenger to whom the ticket was issued. For example, you can use this field for the frequent flyer number. 

        :param id: The id of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's email address, including the full domain name, such as jdoe@example.com.

        :return: The email of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's email address, including the full domain name, such as jdoe@example.com.

        :param email: The email of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._email = email

    @property
    def nationality(self):
        """
        Gets the nationality of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's nationality country. Use the two character [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).

        :return: The nationality of this Ptsv2paymentsOrderInformationPassenger.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """
        Sets the nationality of this Ptsv2paymentsOrderInformationPassenger.
        Passenger's nationality country. Use the two character [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).

        :param nationality: The nationality of this Ptsv2paymentsOrderInformationPassenger.
        :type: str
        """

        self._nationality = nationality

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
        if not isinstance(other, Ptsv2paymentsOrderInformationPassenger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
