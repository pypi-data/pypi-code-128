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


class Ptsv2paymentsTravelInformationTransitAirlineLegs(object):
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
        'carrier_code': 'str',
        'flight_number': 'str',
        'originating_airport_code': 'str',
        '_class': 'str',
        'stopover_indicator': 'int',
        'departure_date': 'int',
        'destination_airport_code': 'str',
        'fare_basis': 'str',
        'depart_tax_amount': 'str',
        'conjunction_ticket': 'str',
        'exchange_ticket_number': 'str',
        'coupon_number': 'str',
        'departure_time': 'int',
        'departure_time_meridian': 'str',
        'arrival_time': 'int',
        'arrival_time_meridian': 'str',
        'endorsements_restrictions': 'str',
        'total_fare_amount': 'str',
        'fee_amount': 'str',
        'tax_amount': 'str'
    }

    attribute_map = {
        'carrier_code': 'carrierCode',
        'flight_number': 'flightNumber',
        'originating_airport_code': 'originatingAirportCode',
        '_class': 'class',
        'stopover_indicator': 'stopoverIndicator',
        'departure_date': 'departureDate',
        'destination_airport_code': 'destinationAirportCode',
        'fare_basis': 'fareBasis',
        'depart_tax_amount': 'departTaxAmount',
        'conjunction_ticket': 'conjunctionTicket',
        'exchange_ticket_number': 'exchangeTicketNumber',
        'coupon_number': 'couponNumber',
        'departure_time': 'departureTime',
        'departure_time_meridian': 'departureTimeMeridian',
        'arrival_time': 'arrivalTime',
        'arrival_time_meridian': 'arrivalTimeMeridian',
        'endorsements_restrictions': 'endorsementsRestrictions',
        'total_fare_amount': 'totalFareAmount',
        'fee_amount': 'feeAmount',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, carrier_code=None, flight_number=None, originating_airport_code=None, _class=None, stopover_indicator=None, departure_date=None, destination_airport_code=None, fare_basis=None, depart_tax_amount=None, conjunction_ticket=None, exchange_ticket_number=None, coupon_number=None, departure_time=None, departure_time_meridian=None, arrival_time=None, arrival_time_meridian=None, endorsements_restrictions=None, total_fare_amount=None, fee_amount=None, tax_amount=None):
        """
        Ptsv2paymentsTravelInformationTransitAirlineLegs - a model defined in Swagger
        """

        self._carrier_code = None
        self._flight_number = None
        self._originating_airport_code = None
        self.__class = None
        self._stopover_indicator = None
        self._departure_date = None
        self._destination_airport_code = None
        self._fare_basis = None
        self._depart_tax_amount = None
        self._conjunction_ticket = None
        self._exchange_ticket_number = None
        self._coupon_number = None
        self._departure_time = None
        self._departure_time_meridian = None
        self._arrival_time = None
        self._arrival_time_meridian = None
        self._endorsements_restrictions = None
        self._total_fare_amount = None
        self._fee_amount = None
        self._tax_amount = None

        if carrier_code is not None:
          self.carrier_code = carrier_code
        if flight_number is not None:
          self.flight_number = flight_number
        if originating_airport_code is not None:
          self.originating_airport_code = originating_airport_code
        if _class is not None:
          self._class = _class
        if stopover_indicator is not None:
          self.stopover_indicator = stopover_indicator
        if departure_date is not None:
          self.departure_date = departure_date
        if destination_airport_code is not None:
          self.destination_airport_code = destination_airport_code
        if fare_basis is not None:
          self.fare_basis = fare_basis
        if depart_tax_amount is not None:
          self.depart_tax_amount = depart_tax_amount
        if conjunction_ticket is not None:
          self.conjunction_ticket = conjunction_ticket
        if exchange_ticket_number is not None:
          self.exchange_ticket_number = exchange_ticket_number
        if coupon_number is not None:
          self.coupon_number = coupon_number
        if departure_time is not None:
          self.departure_time = departure_time
        if departure_time_meridian is not None:
          self.departure_time_meridian = departure_time_meridian
        if arrival_time is not None:
          self.arrival_time = arrival_time
        if arrival_time_meridian is not None:
          self.arrival_time_meridian = arrival_time_meridian
        if endorsements_restrictions is not None:
          self.endorsements_restrictions = endorsements_restrictions
        if total_fare_amount is not None:
          self.total_fare_amount = total_fare_amount
        if fee_amount is not None:
          self.fee_amount = fee_amount
        if tax_amount is not None:
          self.tax_amount = tax_amount

    @property
    def carrier_code(self):
        """
        Gets the carrier_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the carrier for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The carrier_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """
        Sets the carrier_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the carrier for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param carrier_code: The carrier_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._carrier_code = carrier_code

    @property
    def flight_number(self):
        """
        Gets the flight_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Flight number for this leg of the trip. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :return: The flight_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, flight_number):
        """
        Sets the flight_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Flight number for this leg of the trip. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :param flight_number: The flight_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._flight_number = flight_number

    @property
    def originating_airport_code(self):
        """
        Gets the originating_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the originating airport for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The originating_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._originating_airport_code

    @originating_airport_code.setter
    def originating_airport_code(self, originating_airport_code):
        """
        Sets the originating_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the originating airport for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param originating_airport_code: The originating_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._originating_airport_code = originating_airport_code

    @property
    def _class(self):
        """
        Gets the _class of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the class of service for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The _class of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """
        Sets the _class of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the class of service for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param _class: The _class of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self.__class = _class

    @property
    def stopover_indicator(self):
        """
        Gets the stopover_indicator of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Code that indicates whether a stopover is allowed on this leg of the trip. Possible values: - `O` (capital letter “O”) (default): Stopover allowed - `X` (capital letter “X”): Stopover not allowed Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The stopover_indicator of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: int
        """
        return self._stopover_indicator

    @stopover_indicator.setter
    def stopover_indicator(self, stopover_indicator):
        """
        Sets the stopover_indicator of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Code that indicates whether a stopover is allowed on this leg of the trip. Possible values: - `O` (capital letter “O”) (default): Stopover allowed - `X` (capital letter “X”): Stopover not allowed Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param stopover_indicator: The stopover_indicator of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: int
        """

        self._stopover_indicator = stopover_indicator

    @property
    def departure_date(self):
        """
        Gets the departure_date of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Departure date for the first leg of the trip. Format: `YYYYMMDD`. Format: English characters only. Optional request field for travel legs. 

        :return: The departure_date of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: int
        """
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        """
        Sets the departure_date of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Departure date for the first leg of the trip. Format: `YYYYMMDD`. Format: English characters only. Optional request field for travel legs. 

        :param departure_date: The departure_date of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: int
        """

        self._departure_date = departure_date

    @property
    def destination_airport_code(self):
        """
        Gets the destination_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the destination airport for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The destination_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._destination_airport_code

    @destination_airport_code.setter
    def destination_airport_code(self, destination_airport_code):
        """
        Sets the destination_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        IATA code for the destination airport for this leg of the trip. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param destination_airport_code: The destination_airport_code of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._destination_airport_code = destination_airport_code

    @property
    def fare_basis(self):
        """
        Gets the fare_basis of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Code for the fare basis for this leg of the trip. The fare basis is assigned by the carriers and indicates a particular ticket type, such as business class or discounted/nonrefundable. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Format: English characters only. Optional request field for travel legs.auto_rental_regular_mileage_cost 

        :return: The fare_basis of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._fare_basis

    @fare_basis.setter
    def fare_basis(self, fare_basis):
        """
        Sets the fare_basis of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Code for the fare basis for this leg of the trip. The fare basis is assigned by the carriers and indicates a particular ticket type, such as business class or discounted/nonrefundable. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Format: English characters only. Optional request field for travel legs.auto_rental_regular_mileage_cost 

        :param fare_basis: The fare_basis of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._fare_basis = fare_basis

    @property
    def depart_tax_amount(self):
        """
        Gets the depart_tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Amount of departure tax for this leg of the trip. 

        :return: The depart_tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._depart_tax_amount

    @depart_tax_amount.setter
    def depart_tax_amount(self, depart_tax_amount):
        """
        Sets the depart_tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Amount of departure tax for this leg of the trip. 

        :param depart_tax_amount: The depart_tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._depart_tax_amount = depart_tax_amount

    @property
    def conjunction_ticket(self):
        """
        Gets the conjunction_ticket of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Ticket that contains additional coupons for this leg of the trip on an itinerary that has more than four segments. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The conjunction_ticket of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._conjunction_ticket

    @conjunction_ticket.setter
    def conjunction_ticket(self, conjunction_ticket):
        """
        Sets the conjunction_ticket of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Ticket that contains additional coupons for this leg of the trip on an itinerary that has more than four segments. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param conjunction_ticket: The conjunction_ticket of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._conjunction_ticket = conjunction_ticket

    @property
    def exchange_ticket_number(self):
        """
        Gets the exchange_ticket_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        New ticket number that is issued when the ticket is exchanged for this leg of the trip. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :return: The exchange_ticket_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._exchange_ticket_number

    @exchange_ticket_number.setter
    def exchange_ticket_number(self, exchange_ticket_number):
        """
        Sets the exchange_ticket_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        New ticket number that is issued when the ticket is exchanged for this leg of the trip. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :param exchange_ticket_number: The exchange_ticket_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._exchange_ticket_number = exchange_ticket_number

    @property
    def coupon_number(self):
        """
        Gets the coupon_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Coupon number. Each leg on the ticket requires a separate coupon, and each coupon is identified by the coupon number. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The coupon_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._coupon_number

    @coupon_number.setter
    def coupon_number(self, coupon_number):
        """
        Sets the coupon_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Coupon number. Each leg on the ticket requires a separate coupon, and each coupon is identified by the coupon number. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param coupon_number: The coupon_number of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._coupon_number = coupon_number

    @property
    def departure_time(self):
        """
        Gets the departure_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Time of departure for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be `00-23` and the minutes must be `00-59`. Format: English characters only. Optional request field for travel legs. 

        :return: The departure_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: int
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """
        Sets the departure_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Time of departure for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be `00-23` and the minutes must be `00-59`. Format: English characters only. Optional request field for travel legs. 

        :param departure_time: The departure_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: int
        """

        self._departure_time = departure_time

    @property
    def departure_time_meridian(self):
        """
        Gets the departure_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        AM or PM for the departure time. Possible values: - A: 12:00 midnight to 11:59 a.m. - P: 12:00 noon to 11:59 p.m Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The departure_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._departure_time_meridian

    @departure_time_meridian.setter
    def departure_time_meridian(self, departure_time_meridian):
        """
        Sets the departure_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        AM or PM for the departure time. Possible values: - A: 12:00 midnight to 11:59 a.m. - P: 12:00 noon to 11:59 p.m Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param departure_time_meridian: The departure_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._departure_time_meridian = departure_time_meridian

    @property
    def arrival_time(self):
        """
        Gets the arrival_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Time of arrival for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be `00-23` and the minutes must be `00-59` Format: English characters only. Optional request field for travel legs. 

        :return: The arrival_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: int
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """
        Sets the arrival_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Time of arrival for this leg of the trip. The format is military time and HHMM: If not all zeros, then the hours must be `00-23` and the minutes must be `00-59` Format: English characters only. Optional request field for travel legs. 

        :param arrival_time: The arrival_time of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: int
        """

        self._arrival_time = arrival_time

    @property
    def arrival_time_meridian(self):
        """
        Gets the arrival_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        AM or PM for the arrival time for this leg of the trip. Possible values: - `A`: 12:00 midnight to 11:59 a.m. - `P`: 12:00 noon to 11:59 p.m. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :return: The arrival_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._arrival_time_meridian

    @arrival_time_meridian.setter
    def arrival_time_meridian(self, arrival_time_meridian):
        """
        Sets the arrival_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        AM or PM for the arrival time for this leg of the trip. Possible values: - `A`: 12:00 midnight to 11:59 a.m. - `P`: 12:00 noon to 11:59 p.m. Format: English characters only. Restricted string data type that indicates a sequence of letters, numbers, and spaces; special characters are not included. Optional request field for travel legs. 

        :param arrival_time_meridian: The arrival_time_meridian of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._arrival_time_meridian = arrival_time_meridian

    @property
    def endorsements_restrictions(self):
        """
        Gets the endorsements_restrictions of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Notes or notations about endorsements and restrictions for this leg of the trip. Endorsements can be notations added by the travel agency, including mandatory government-required notations such as value added tax. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :return: The endorsements_restrictions of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._endorsements_restrictions

    @endorsements_restrictions.setter
    def endorsements_restrictions(self, endorsements_restrictions):
        """
        Sets the endorsements_restrictions of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Notes or notations about endorsements and restrictions for this leg of the trip. Endorsements can be notations added by the travel agency, including mandatory government-required notations such as value added tax. Restrictions are limitations for the ticket based on the type of fare, such as a nonrefundable ticket or a 3-day minimum stay. Format: English characters only. Optional request field for travel legs. 

        :param endorsements_restrictions: The endorsements_restrictions of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._endorsements_restrictions = endorsements_restrictions

    @property
    def total_fare_amount(self):
        """
        Gets the total_fare_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Total fare for this leg of the trip. Format: English characters only. Optional request field for travel legs. 

        :return: The total_fare_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._total_fare_amount

    @total_fare_amount.setter
    def total_fare_amount(self, total_fare_amount):
        """
        Sets the total_fare_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Total fare for this leg of the trip. Format: English characters only. Optional request field for travel legs. 

        :param total_fare_amount: The total_fare_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._total_fare_amount = total_fare_amount

    @property
    def fee_amount(self):
        """
        Gets the fee_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Fee for this leg of the trip, such as an airport fee or country fee. Format: English characters only. Optional request field for travel legs. 

        :return: The fee_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """
        Sets the fee_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Fee for this leg of the trip, such as an airport fee or country fee. Format: English characters only. Optional request field for travel legs. 

        :param fee_amount: The fee_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._fee_amount = fee_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Tax for this leg of the trip. Format: English characters only. Optional request field for travel legs. 

        :return: The tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        Tax for this leg of the trip. Format: English characters only. Optional request field for travel legs. 

        :param tax_amount: The tax_amount of this Ptsv2paymentsTravelInformationTransitAirlineLegs.
        :type: str
        """

        self._tax_amount = tax_amount

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
        if not isinstance(other, Ptsv2paymentsTravelInformationTransitAirlineLegs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
