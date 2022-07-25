# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import akeyless
from akeyless.models.update_dockerhub_target import UpdateDockerhubTarget  # noqa: E501
from akeyless.rest import ApiException

class TestUpdateDockerhubTarget(unittest.TestCase):
    """UpdateDockerhubTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateDockerhubTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = akeyless.models.update_dockerhub_target.UpdateDockerhubTarget()  # noqa: E501
        if include_optional :
            return UpdateDockerhubTarget(
                comment = '0', 
                dockerhub_password = '0', 
                dockerhub_username = '0', 
                keep_prev_version = '0', 
                key = '0', 
                name = '0', 
                new_name = '0', 
                token = '0', 
                uid_token = '0', 
                update_version = True
            )
        else :
            return UpdateDockerhubTarget(
                name = '0',
        )

    def testUpdateDockerhubTarget(self):
        """Test UpdateDockerhubTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
