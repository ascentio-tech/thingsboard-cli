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

from pprint import pformat
from six import iteritems
import re


class Alarm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ack_ts=None, clear_ts=None, created_time=None, details=None, end_ts=None, id=None, name=None, originator=None, propagate=None, severity=None, start_ts=None, status=None, tenant_id=None, type=None):
        """
        Alarm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ack_ts': 'int',
            'clear_ts': 'int',
            'created_time': 'int',
            'details': 'str',
            'end_ts': 'int',
            'id': 'AlarmId',
            'name': 'str',
            'originator': 'EntityId',
            'propagate': 'bool',
            'severity': 'str',
            'start_ts': 'int',
            'status': 'str',
            'tenant_id': 'TenantId',
            'type': 'str'
        }

        self.attribute_map = {
            'ack_ts': 'ackTs',
            'clear_ts': 'clearTs',
            'created_time': 'createdTime',
            'details': 'details',
            'end_ts': 'endTs',
            'id': 'id',
            'name': 'name',
            'originator': 'originator',
            'propagate': 'propagate',
            'severity': 'severity',
            'start_ts': 'startTs',
            'status': 'status',
            'tenant_id': 'tenantId',
            'type': 'type'
        }

        self._ack_ts = ack_ts
        self._clear_ts = clear_ts
        self._created_time = created_time
        self._details = details
        self._end_ts = end_ts
        self._id = id
        self._name = name
        self._originator = originator
        self._propagate = propagate
        self._severity = severity
        self._start_ts = start_ts
        self._status = status
        self._tenant_id = tenant_id
        self._type = type

    @property
    def ack_ts(self):
        """
        Gets the ack_ts of this Alarm.


        :return: The ack_ts of this Alarm.
        :rtype: int
        """
        return self._ack_ts

    @ack_ts.setter
    def ack_ts(self, ack_ts):
        """
        Sets the ack_ts of this Alarm.


        :param ack_ts: The ack_ts of this Alarm.
        :type: int
        """

        self._ack_ts = ack_ts

    @property
    def clear_ts(self):
        """
        Gets the clear_ts of this Alarm.


        :return: The clear_ts of this Alarm.
        :rtype: int
        """
        return self._clear_ts

    @clear_ts.setter
    def clear_ts(self, clear_ts):
        """
        Sets the clear_ts of this Alarm.


        :param clear_ts: The clear_ts of this Alarm.
        :type: int
        """

        self._clear_ts = clear_ts

    @property
    def created_time(self):
        """
        Gets the created_time of this Alarm.


        :return: The created_time of this Alarm.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this Alarm.


        :param created_time: The created_time of this Alarm.
        :type: int
        """

        self._created_time = created_time

    @property
    def details(self):
        """
        Gets the details of this Alarm.


        :return: The details of this Alarm.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Alarm.


        :param details: The details of this Alarm.
        :type: str
        """

        self._details = details

    @property
    def end_ts(self):
        """
        Gets the end_ts of this Alarm.


        :return: The end_ts of this Alarm.
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """
        Sets the end_ts of this Alarm.


        :param end_ts: The end_ts of this Alarm.
        :type: int
        """

        self._end_ts = end_ts

    @property
    def id(self):
        """
        Gets the id of this Alarm.


        :return: The id of this Alarm.
        :rtype: AlarmId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Alarm.


        :param id: The id of this Alarm.
        :type: AlarmId
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Alarm.


        :return: The name of this Alarm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Alarm.


        :param name: The name of this Alarm.
        :type: str
        """

        self._name = name

    @property
    def originator(self):
        """
        Gets the originator of this Alarm.


        :return: The originator of this Alarm.
        :rtype: EntityId
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """
        Sets the originator of this Alarm.


        :param originator: The originator of this Alarm.
        :type: EntityId
        """

        self._originator = originator

    @property
    def propagate(self):
        """
        Gets the propagate of this Alarm.


        :return: The propagate of this Alarm.
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        """
        Sets the propagate of this Alarm.


        :param propagate: The propagate of this Alarm.
        :type: bool
        """

        self._propagate = propagate

    @property
    def severity(self):
        """
        Gets the severity of this Alarm.


        :return: The severity of this Alarm.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Alarm.


        :param severity: The severity of this Alarm.
        :type: str
        """
        allowed_values = ["CRITICAL", "MAJOR", "MINOR", "WARNING", "INDETERMINATE"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def start_ts(self):
        """
        Gets the start_ts of this Alarm.


        :return: The start_ts of this Alarm.
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """
        Sets the start_ts of this Alarm.


        :param start_ts: The start_ts of this Alarm.
        :type: int
        """

        self._start_ts = start_ts

    @property
    def status(self):
        """
        Gets the status of this Alarm.


        :return: The status of this Alarm.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Alarm.


        :param status: The status of this Alarm.
        :type: str
        """
        allowed_values = ["ACTIVE_UNACK", "ACTIVE_ACK", "CLEARED_UNACK", "CLEARED_ACK"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this Alarm.


        :return: The tenant_id of this Alarm.
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this Alarm.


        :param tenant_id: The tenant_id of this Alarm.
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """
        Gets the type of this Alarm.


        :return: The type of this Alarm.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Alarm.


        :param type: The type of this Alarm.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
