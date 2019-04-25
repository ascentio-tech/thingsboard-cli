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
from thingsboard_client.apis.alarmcontroller_api import AlarmcontrollerApi


class TestAlarmcontrollerApi(unittest.TestCase):
    """ AlarmcontrollerApi unit test stubs """

    def setUp(self):
        self.api = thingsboard_client.apis.alarmcontroller_api.AlarmcontrollerApi()

    def tearDown(self):
        pass

    def test_ack_alarm_using_post(self):
        """
        Test case for ack_alarm_using_post

        ackAlarm
        """
        pass

    def test_clear_alarm_using_post(self):
        """
        Test case for clear_alarm_using_post

        clearAlarm
        """
        pass

    def test_get_alarm_by_id_using_get(self):
        """
        Test case for get_alarm_by_id_using_get

        getAlarmById
        """
        pass

    def test_get_alarm_info_by_id_using_get(self):
        """
        Test case for get_alarm_info_by_id_using_get

        getAlarmInfoById
        """
        pass

    def test_get_alarms_using_get(self):
        """
        Test case for get_alarms_using_get

        getAlarms
        """
        pass

    def test_get_highest_alarm_severity_using_get(self):
        """
        Test case for get_highest_alarm_severity_using_get

        getHighestAlarmSeverity
        """
        pass

    def test_save_alarm_using_post(self):
        """
        Test case for save_alarm_using_post

        saveAlarm
        """
        pass


if __name__ == '__main__':
    unittest.main()
