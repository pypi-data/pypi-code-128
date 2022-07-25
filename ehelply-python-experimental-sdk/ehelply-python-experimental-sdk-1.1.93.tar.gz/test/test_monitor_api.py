# coding: utf-8

"""
    eHelply SDK - 1.1.93

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.93
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import ehelply_python_experimental_sdk
from ehelply_python_experimental_sdk.api.monitor_api import MonitorApi  # noqa: E501


class TestMonitorApi(unittest.TestCase):
    """MonitorApi unit test stubs"""

    def setUp(self):
        self.api = MonitorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acknowledge_alarm(self):
        """Test case for acknowledge_alarm

        Acknowledgealarm  # noqa: E501
        """
        pass

    def test_assign_alarm(self):
        """Test case for assign_alarm

        Assignalarm  # noqa: E501
        """
        pass

    def test_attach_alarm_note(self):
        """Test case for attach_alarm_note

        Attachalarmnote  # noqa: E501
        """
        pass

    def test_attach_alarm_ticket(self):
        """Test case for attach_alarm_ticket

        Attachalarmticket  # noqa: E501
        """
        pass

    def test_clear_alarm(self):
        """Test case for clear_alarm

        Clearalarm  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Getservice  # noqa: E501
        """
        pass

    def test_get_service_alarm(self):
        """Test case for get_service_alarm

        Getservicealarm  # noqa: E501
        """
        pass

    def test_get_service_alarms(self):
        """Test case for get_service_alarms

        Getservicealarms  # noqa: E501
        """
        pass

    def test_get_service_heartbeat(self):
        """Test case for get_service_heartbeat

        Getserviceheartbeat  # noqa: E501
        """
        pass

    def test_get_service_kpis(self):
        """Test case for get_service_kpis

        Getservicekpis  # noqa: E501
        """
        pass

    def test_get_service_spec(self):
        """Test case for get_service_spec

        Getservicespec  # noqa: E501
        """
        pass

    def test_get_service_specs(self):
        """Test case for get_service_specs

        Getservicespecs  # noqa: E501
        """
        pass

    def test_get_service_vitals(self):
        """Test case for get_service_vitals

        Getservicevitals  # noqa: E501
        """
        pass

    def test_get_services(self):
        """Test case for get_services

        Getservices  # noqa: E501
        """
        pass

    def test_get_services_with_specs(self):
        """Test case for get_services_with_specs

        Getserviceswithspecs  # noqa: E501
        """
        pass

    def test_hide_service(self):
        """Test case for hide_service

        Hideservice  # noqa: E501
        """
        pass

    def test_ignore_alarm(self):
        """Test case for ignore_alarm

        Ignorealarm  # noqa: E501
        """
        pass

    def test_register_service(self):
        """Test case for register_service

        Registerservice  # noqa: E501
        """
        pass

    def test_search_alarms(self):
        """Test case for search_alarms

        Searchalarms  # noqa: E501
        """
        pass

    def test_show_service(self):
        """Test case for show_service

        Showservice  # noqa: E501
        """
        pass

    def test_terminate_alarm(self):
        """Test case for terminate_alarm

        Terminatealarm  # noqa: E501
        """
        pass

    def test_trigger_alarm(self):
        """Test case for trigger_alarm

        Triggeralarm  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
