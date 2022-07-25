# coding: utf-8

"""
    eHelply SDK - 1.1.93

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.93
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_experimental_sdk.api_client import ApiClient
from ehelply_python_experimental_sdk.api.tag_api_endpoints.create_tag_places_tags_post import CreateTagPlacesTagsPost
from ehelply_python_experimental_sdk.api.tag_api_endpoints.delete_tag_places_tags_tag_uuid_delete import DeleteTagPlacesTagsTagUuidDelete
from ehelply_python_experimental_sdk.api.tag_api_endpoints.get_tag_places_tags_tag_uuid_get import GetTagPlacesTagsTagUuidGet
from ehelply_python_experimental_sdk.api.tag_api_endpoints.search_tags_places_tags_get import SearchTagsPlacesTagsGet
from ehelply_python_experimental_sdk.api.tag_api_endpoints.update_tag_places_tags_tag_uuid_put import UpdateTagPlacesTagsTagUuidPut


class TagApi(
    CreateTagPlacesTagsPost,
    DeleteTagPlacesTagsTagUuidDelete,
    GetTagPlacesTagsTagUuidGet,
    SearchTagsPlacesTagsGet,
    UpdateTagPlacesTagsTagUuidPut,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
