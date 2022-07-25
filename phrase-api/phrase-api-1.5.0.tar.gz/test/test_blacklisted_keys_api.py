# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.blacklisted_keys_api import BlacklistedKeysApi  # noqa: E501
from phrase_api.rest import ApiException


class TestBlacklistedKeysApi(unittest.TestCase):
    """BlacklistedKeysApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.blacklisted_keys_api.BlacklistedKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_blacklisted_key_create(self):
        """Test case for blacklisted_key_create

        Create a blocked key  # noqa: E501
        """
        pass

    def test_blacklisted_key_delete(self):
        """Test case for blacklisted_key_delete

        Delete a blocked key  # noqa: E501
        """
        pass

    def test_blacklisted_key_show(self):
        """Test case for blacklisted_key_show

        Get a single blocked key  # noqa: E501
        """
        pass

    def test_blacklisted_key_update(self):
        """Test case for blacklisted_key_update

        Update a blocked key  # noqa: E501
        """
        pass

    def test_blacklisted_keys_list(self):
        """Test case for blacklisted_keys_list

        List blocked keys  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
