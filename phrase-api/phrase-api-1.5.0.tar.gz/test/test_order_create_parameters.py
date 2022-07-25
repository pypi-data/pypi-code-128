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
from phrase_api.models.order_create_parameters import OrderCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestOrderCreateParameters(unittest.TestCase):
    """OrderCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrderCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.order_create_parameters.OrderCreateParameters()  # noqa: E501
        if include_optional :
            return OrderCreateParameters(
                branch = 'my-feature-branch', 
                name = 'Welcome message translations', 
                lsp = 'textmaster', 
                source_locale_id = 'abcd1234abcd1234abcd1234abcd1234', 
                target_locale_ids = ["1234abcd1234abcd1234abcd1234abcd","abcd1234abcd1234abcd1234abcd1234"], 
                translation_type = 'premium', 
                tag = 'my-awesome-feature', 
                message = 'Please make everything sound really nice :)', 
                styleguide_id = '1234abcd1234abcd1234abcd1234abcd', 
                unverify_translations_upon_delivery = True, 
                include_untranslated_keys = True, 
                include_unverified_translations = True, 
                category = 'C021', 
                quality = True, 
                priority = True
            )
        else :
            return OrderCreateParameters(
        )

    def testOrderCreateParameters(self):
        """Test OrderCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
