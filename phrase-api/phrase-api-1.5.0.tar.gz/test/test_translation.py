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
from phrase_api.models.translation import Translation  # noqa: E501
from phrase_api.rest import ApiException

class TestTranslation(unittest.TestCase):
    """Translation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Translation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.translation.Translation()  # noqa: E501
        if include_optional :
            return Translation(
                id = '0', 
                content = '0', 
                unverified = True, 
                excluded = True, 
                plural_suffix = '0', 
                key = phrase_api.models.key_preview.key_preview(
                    id = '0', 
                    name = '0', 
                    plural = True, ), 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                placeholders = [
                    '0'
                    ], 
                state = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Translation(
        )

    def testTranslation(self):
        """Test Translation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
