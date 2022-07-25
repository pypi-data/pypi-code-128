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
from phrase_api.models.job_create_parameters import JobCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestJobCreateParameters(unittest.TestCase):
    """JobCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_create_parameters.JobCreateParameters()  # noqa: E501
        if include_optional :
            return JobCreateParameters(
                branch = 'my-feature-branch', 
                name = 'de', 
                source_locale_id = 'abcd1234cdef1234abcd1234cdef1234', 
                briefing = 'de-DE', 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                ticket_url = 'https://example.atlassian.net/browse/FOO', 
                tags = ["myUploadTag"], 
                translation_key_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                job_template_id = 'abcd1234cdef1234abcd1234cdef1234'
            )
        else :
            return JobCreateParameters(
        )

    def testJobCreateParameters(self):
        """Test JobCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
