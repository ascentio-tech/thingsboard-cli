# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import thingsboard_client
from thingsboard_client.rest import ApiException
from thingsboard_client.models.audit_log import AuditLog


class TestAuditLog(unittest.TestCase):
    """ AuditLog unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuditLog(self):
        """
        Test AuditLog
        """
        model = thingsboard_client.models.audit_log.AuditLog()


if __name__ == '__main__':
    unittest.main()
