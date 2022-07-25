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
from phrase_api.models.job_comment_update_parameters import JobCommentUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestJobCommentUpdateParameters(unittest.TestCase):
    """JobCommentUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobCommentUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_comment_update_parameters.JobCommentUpdateParameters()  # noqa: E501
        if include_optional :
            return JobCommentUpdateParameters(
                message = 'Some message...'
            )
        else :
            return JobCommentUpdateParameters(
        )

    def testJobCommentUpdateParameters(self):
        """Test JobCommentUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
