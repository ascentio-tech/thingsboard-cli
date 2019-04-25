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
from thingsboard_client.apis.customercontroller_api import CustomercontrollerApi


class TestCustomercontrollerApi(unittest.TestCase):
    """ CustomercontrollerApi unit test stubs """

    def setUp(self):
        self.api = thingsboard_client.apis.customercontroller_api.CustomercontrollerApi()

    def tearDown(self):
        pass

    def test_delete_customer_using_delete(self):
        """
        Test case for delete_customer_using_delete

        deleteCustomer
        """
        pass

    def test_get_customer_by_id_using_get(self):
        """
        Test case for get_customer_by_id_using_get

        getCustomerById
        """
        pass

    def test_get_customer_title_by_id_using_get(self):
        """
        Test case for get_customer_title_by_id_using_get

        getCustomerTitleById
        """
        pass

    def test_get_customers_using_get(self):
        """
        Test case for get_customers_using_get

        getCustomers
        """
        pass

    def test_get_short_customer_info_by_id_using_get(self):
        """
        Test case for get_short_customer_info_by_id_using_get

        getShortCustomerInfoById
        """
        pass

    def test_get_tenant_customer_using_get(self):
        """
        Test case for get_tenant_customer_using_get

        getTenantCustomer
        """
        pass

    def test_save_customer_using_post(self):
        """
        Test case for save_customer_using_post

        saveCustomer
        """
        pass


if __name__ == '__main__':
    unittest.main()
