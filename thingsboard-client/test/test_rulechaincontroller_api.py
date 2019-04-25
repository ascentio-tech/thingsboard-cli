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
from thingsboard_client.apis.rulechaincontroller_api import RulechaincontrollerApi


class TestRulechaincontrollerApi(unittest.TestCase):
    """ RulechaincontrollerApi unit test stubs """

    def setUp(self):
        self.api = thingsboard_client.apis.rulechaincontroller_api.RulechaincontrollerApi()

    def tearDown(self):
        pass

    def test_delete_rule_chain_using_delete(self):
        """
        Test case for delete_rule_chain_using_delete

        deleteRuleChain
        """
        pass

    def test_get_latest_rule_node_debug_input_using_get(self):
        """
        Test case for get_latest_rule_node_debug_input_using_get

        getLatestRuleNodeDebugInput
        """
        pass

    def test_get_rule_chain_by_id_using_get(self):
        """
        Test case for get_rule_chain_by_id_using_get

        getRuleChainById
        """
        pass

    def test_get_rule_chain_meta_data_using_get(self):
        """
        Test case for get_rule_chain_meta_data_using_get

        getRuleChainMetaData
        """
        pass

    def test_get_rule_chains_using_get(self):
        """
        Test case for get_rule_chains_using_get

        getRuleChains
        """
        pass

    def test_save_rule_chain_meta_data_using_post(self):
        """
        Test case for save_rule_chain_meta_data_using_post

        saveRuleChainMetaData
        """
        pass

    def test_save_rule_chain_using_post(self):
        """
        Test case for save_rule_chain_using_post

        saveRuleChain
        """
        pass

    def test_set_root_rule_chain_using_post(self):
        """
        Test case for set_root_rule_chain_using_post

        setRootRuleChain
        """
        pass

    def test_test_script_using_post(self):
        """
        Test case for test_script_using_post

        testScript
        """
        pass


if __name__ == '__main__':
    unittest.main()
