# coding: utf-8

"""
    eHelply SDK - 1.1.92

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.92
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.logging_api_endpoints.get_logs import GetLogs
from ehelply_python_experimental_sdk.api.logging_api_endpoints.get_service_logs import GetServiceLogs
from ehelply_python_experimental_sdk.api.logging_api_endpoints.get_subject_logs import GetSubjectLogs


class LoggingApi(
    GetLogs,
    GetServiceLogs,
    GetSubjectLogs,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
