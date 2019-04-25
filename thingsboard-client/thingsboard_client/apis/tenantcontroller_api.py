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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TenantcontrollerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_tenant_using_delete(self, tenant_id, **kwargs):
        """
        deleteTenant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tenant_using_delete(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)
        else:
            (data) = self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)
            return data

    def delete_tenant_using_delete_with_http_info(self, tenant_id, **kwargs):
        """
        deleteTenant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tenant_using_delete_with_http_info(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tenant_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `delete_tenant_using_delete`")

        resource_path = '/api/tenant/{tenantId}'.replace('{format}', 'json')
        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_tenant_by_id_using_get(self, tenant_id, **kwargs):
        """
        getTenantById
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tenant_by_id_using_get(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)
        else:
            (data) = self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)
            return data

    def get_tenant_by_id_using_get_with_http_info(self, tenant_id, **kwargs):
        """
        getTenantById
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tenant_by_id_using_get_with_http_info(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenant_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_tenant_by_id_using_get`")

        resource_path = '/api/tenant/{tenantId}'.replace('{format}', 'json')
        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Tenant',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_tenants_using_get(self, limit, **kwargs):
        """
        getTenants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tenants_using_get(limit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tenants_using_get_with_http_info(limit, **kwargs)
        else:
            (data) = self.get_tenants_using_get_with_http_info(limit, **kwargs)
            return data

    def get_tenants_using_get_with_http_info(self, limit, **kwargs):
        """
        getTenants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tenants_using_get_with_http_info(limit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'text_search', 'id_offset', 'text_offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenants_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_tenants_using_get`")

        resource_path = '/api/tenants'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'text_search' in params:
            query_params['textSearch'] = params['text_search']
        if 'id_offset' in params:
            query_params['idOffset'] = params['id_offset']
        if 'text_offset' in params:
            query_params['textOffset'] = params['text_offset']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TextPageDataTenant',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def save_tenant_using_post(self, tenant, **kwargs):
        """
        saveTenant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_tenant_using_post(tenant, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_tenant_using_post_with_http_info(tenant, **kwargs)
        else:
            (data) = self.save_tenant_using_post_with_http_info(tenant, **kwargs)
            return data

    def save_tenant_using_post_with_http_info(self, tenant, **kwargs):
        """
        saveTenant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_tenant_using_post_with_http_info(tenant, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_tenant_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant' is set
        if ('tenant' not in params) or (params['tenant'] is None):
            raise ValueError("Missing the required parameter `tenant` when calling `save_tenant_using_post`")

        resource_path = '/api/tenant'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenant' in params:
            body_params = params['tenant']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Tenant',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
