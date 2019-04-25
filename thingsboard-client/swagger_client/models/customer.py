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


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_info=None, address=None, address2=None, city=None, country=None, created_time=None, email=None, id=None, name=None, phone=None, state=None, tenant_id=None, title=None, zip=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_info': 'str',
            'address': 'str',
            'address2': 'str',
            'city': 'str',
            'country': 'str',
            'created_time': 'int',
            'email': 'str',
            'id': 'CustomerId',
            'name': 'str',
            'phone': 'str',
            'state': 'str',
            'tenant_id': 'TenantId',
            'title': 'str',
            'zip': 'str'
        }

        self.attribute_map = {
            'additional_info': 'additionalInfo',
            'address': 'address',
            'address2': 'address2',
            'city': 'city',
            'country': 'country',
            'created_time': 'createdTime',
            'email': 'email',
            'id': 'id',
            'name': 'name',
            'phone': 'phone',
            'state': 'state',
            'tenant_id': 'tenantId',
            'title': 'title',
            'zip': 'zip'
        }

        self._additional_info = additional_info
        self._address = address
        self._address2 = address2
        self._city = city
        self._country = country
        self._created_time = created_time
        self._email = email
        self._id = id
        self._name = name
        self._phone = phone
        self._state = state
        self._tenant_id = tenant_id
        self._title = title
        self._zip = zip

    @property
    def additional_info(self):
        """
        Gets the additional_info of this Customer.


        :return: The additional_info of this Customer.
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """
        Sets the additional_info of this Customer.


        :param additional_info: The additional_info of this Customer.
        :type: str
        """

        self._additional_info = additional_info

    @property
    def address(self):
        """
        Gets the address of this Customer.


        :return: The address of this Customer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Customer.


        :param address: The address of this Customer.
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """
        Gets the address2 of this Customer.


        :return: The address2 of this Customer.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Customer.


        :param address2: The address2 of this Customer.
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """
        Gets the city of this Customer.


        :return: The city of this Customer.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Customer.


        :param city: The city of this Customer.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this Customer.


        :return: The country of this Customer.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Customer.


        :param country: The country of this Customer.
        :type: str
        """

        self._country = country

    @property
    def created_time(self):
        """
        Gets the created_time of this Customer.


        :return: The created_time of this Customer.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this Customer.


        :param created_time: The created_time of this Customer.
        :type: int
        """

        self._created_time = created_time

    @property
    def email(self):
        """
        Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Customer.


        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """
        Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: CustomerId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.


        :param id: The id of this Customer.
        :type: CustomerId
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Customer.


        :return: The name of this Customer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Customer.


        :param name: The name of this Customer.
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """
        Gets the phone of this Customer.


        :return: The phone of this Customer.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Customer.


        :param phone: The phone of this Customer.
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """
        Gets the state of this Customer.


        :return: The state of this Customer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Customer.


        :param state: The state of this Customer.
        :type: str
        """

        self._state = state

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this Customer.


        :return: The tenant_id of this Customer.
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this Customer.


        :param tenant_id: The tenant_id of this Customer.
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """
        Gets the title of this Customer.


        :return: The title of this Customer.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Customer.


        :param title: The title of this Customer.
        :type: str
        """

        self._title = title

    @property
    def zip(self):
        """
        Gets the zip of this Customer.


        :return: The zip of this Customer.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this Customer.


        :param zip: The zip of this Customer.
        :type: str
        """

        self._zip = zip

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
