# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase_api
from phrase_api.models.job_keys_create_parameters import JobKeysCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestJobKeysCreateParameters(unittest.TestCase):
    """JobKeysCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobKeysCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_keys_create_parameters.JobKeysCreateParameters()  # noqa: E501
        if include_optional :
            return JobKeysCreateParameters(
                branch = 'my-feature-branch', 
                translation_key_ids = ["abcd1234cdef1234abcd1234cdef1234"]
            )
        else :
            return JobKeysCreateParameters(
        )

    def testJobKeysCreateParameters(self):
        """Test JobKeysCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
