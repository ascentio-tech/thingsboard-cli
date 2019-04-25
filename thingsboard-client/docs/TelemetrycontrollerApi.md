# swagger_client.TelemetrycontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_entity_attributes_using_delete**](TelemetrycontrollerApi.md#delete_entity_attributes_using_delete) | **DELETE** /api/plugins/telemetry/{deviceId}/{scope} | deleteEntityAttributes
[**delete_entity_attributes_using_delete1**](TelemetrycontrollerApi.md#delete_entity_attributes_using_delete1) | **DELETE** /api/plugins/telemetry/{entityType}/{entityId}/{scope} | deleteEntityAttributes
[**get_attribute_keys_by_scope_using_get**](TelemetrycontrollerApi.md#get_attribute_keys_by_scope_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/keys/attributes/{scope} | getAttributeKeysByScope
[**get_attribute_keys_using_get**](TelemetrycontrollerApi.md#get_attribute_keys_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/keys/attributes | getAttributeKeys
[**get_attributes_by_scope_using_get**](TelemetrycontrollerApi.md#get_attributes_by_scope_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/values/attributes/{scope} | getAttributesByScope
[**get_attributes_using_get**](TelemetrycontrollerApi.md#get_attributes_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/values/attributes | getAttributes
[**get_latest_timeseries_using_get**](TelemetrycontrollerApi.md#get_latest_timeseries_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/values/timeseries | getLatestTimeseries
[**get_timeseries_keys_using_get**](TelemetrycontrollerApi.md#get_timeseries_keys_using_get) | **GET** /api/plugins/telemetry/{entityType}/{entityId}/keys/timeseries | getTimeseriesKeys
[**save_device_attributes_using_post**](TelemetrycontrollerApi.md#save_device_attributes_using_post) | **POST** /api/plugins/telemetry/{deviceId}/{scope} | saveDeviceAttributes
[**save_entity_attributes_v1_using_post**](TelemetrycontrollerApi.md#save_entity_attributes_v1_using_post) | **POST** /api/plugins/telemetry/{entityType}/{entityId}/{scope} | saveEntityAttributesV1
[**save_entity_attributes_v2_using_post**](TelemetrycontrollerApi.md#save_entity_attributes_v2_using_post) | **POST** /api/plugins/telemetry/{entityType}/{entityId}/attributes/{scope} | saveEntityAttributesV2
[**save_entity_telemetry_using_post**](TelemetrycontrollerApi.md#save_entity_telemetry_using_post) | **POST** /api/plugins/telemetry/{entityType}/{entityId}/timeseries/{scope} | saveEntityTelemetry
[**save_entity_telemetry_with_ttl_using_post**](TelemetrycontrollerApi.md#save_entity_telemetry_with_ttl_using_post) | **POST** /api/plugins/telemetry/{entityType}/{entityId}/timeseries/{scope}/{ttl} | saveEntityTelemetryWithTTL


# **delete_entity_attributes_using_delete**
> DeferredResultResponseEntity delete_entity_attributes_using_delete(device_id, scope, keys)

deleteEntityAttributes

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
device_id = 'device_id_example' # str | deviceId
scope = 'scope_example' # str | scope
keys = 'keys_example' # str | keys

try: 
    # deleteEntityAttributes
    api_response = api_instance.delete_entity_attributes_using_delete(device_id, scope, keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->delete_entity_attributes_using_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **scope** | **str**| scope | 
 **keys** | **str**| keys | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_attributes_using_delete1**
> DeferredResultResponseEntity delete_entity_attributes_using_delete1(entity_type, entity_id, scope, keys)

deleteEntityAttributes

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
keys = 'keys_example' # str | keys

try: 
    # deleteEntityAttributes
    api_response = api_instance.delete_entity_attributes_using_delete1(entity_type, entity_id, scope, keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->delete_entity_attributes_using_delete1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **keys** | **str**| keys | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_keys_by_scope_using_get**
> DeferredResultResponseEntity get_attribute_keys_by_scope_using_get(entity_type, entity_id, scope)

getAttributeKeysByScope

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope

try: 
    # getAttributeKeysByScope
    api_response = api_instance.get_attribute_keys_by_scope_using_get(entity_type, entity_id, scope)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_attribute_keys_by_scope_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_keys_using_get**
> DeferredResultResponseEntity get_attribute_keys_using_get(entity_type, entity_id)

getAttributeKeys

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId

try: 
    # getAttributeKeys
    api_response = api_instance.get_attribute_keys_using_get(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_attribute_keys_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_by_scope_using_get**
> DeferredResultResponseEntity get_attributes_by_scope_using_get(entity_type, entity_id, scope, keys=keys)

getAttributesByScope

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
keys = 'keys_example' # str | keys (optional)

try: 
    # getAttributesByScope
    api_response = api_instance.get_attributes_by_scope_using_get(entity_type, entity_id, scope, keys=keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_attributes_by_scope_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **keys** | **str**| keys | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_using_get**
> DeferredResultResponseEntity get_attributes_using_get(entity_type, entity_id, keys=keys)

getAttributes

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
keys = 'keys_example' # str | keys (optional)

try: 
    # getAttributes
    api_response = api_instance.get_attributes_using_get(entity_type, entity_id, keys=keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_attributes_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **keys** | **str**| keys | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_timeseries_using_get**
> DeferredResultResponseEntity get_latest_timeseries_using_get(entity_type, entity_id, keys=keys)

getLatestTimeseries

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
keys = 'keys_example' # str | keys (optional)

try: 
    # getLatestTimeseries
    api_response = api_instance.get_latest_timeseries_using_get(entity_type, entity_id, keys=keys)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_latest_timeseries_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **keys** | **str**| keys | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timeseries_keys_using_get**
> DeferredResultResponseEntity get_timeseries_keys_using_get(entity_type, entity_id)

getTimeseriesKeys

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId

try: 
    # getTimeseriesKeys
    api_response = api_instance.get_timeseries_keys_using_get(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->get_timeseries_keys_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_device_attributes_using_post**
> DeferredResultResponseEntity save_device_attributes_using_post(device_id, scope, request)

saveDeviceAttributes

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
device_id = 'device_id_example' # str | deviceId
scope = 'scope_example' # str | scope
request = 'request_example' # str | request

try: 
    # saveDeviceAttributes
    api_response = api_instance.save_device_attributes_using_post(device_id, scope, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->save_device_attributes_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **scope** | **str**| scope | 
 **request** | **str**| request | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_attributes_v1_using_post**
> DeferredResultResponseEntity save_entity_attributes_v1_using_post(entity_type, entity_id, scope, request)

saveEntityAttributesV1

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
request = 'request_example' # str | request

try: 
    # saveEntityAttributesV1
    api_response = api_instance.save_entity_attributes_v1_using_post(entity_type, entity_id, scope, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->save_entity_attributes_v1_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **request** | **str**| request | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_attributes_v2_using_post**
> DeferredResultResponseEntity save_entity_attributes_v2_using_post(entity_type, entity_id, scope, request)

saveEntityAttributesV2

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
request = 'request_example' # str | request

try: 
    # saveEntityAttributesV2
    api_response = api_instance.save_entity_attributes_v2_using_post(entity_type, entity_id, scope, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->save_entity_attributes_v2_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **request** | **str**| request | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_telemetry_using_post**
> DeferredResultResponseEntity save_entity_telemetry_using_post(entity_type, entity_id, scope, request_body)

saveEntityTelemetry

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
request_body = 'request_body_example' # str | requestBody

try: 
    # saveEntityTelemetry
    api_response = api_instance.save_entity_telemetry_using_post(entity_type, entity_id, scope, request_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->save_entity_telemetry_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **request_body** | **str**| requestBody | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_telemetry_with_ttl_using_post**
> DeferredResultResponseEntity save_entity_telemetry_with_ttl_using_post(entity_type, entity_id, scope, ttl, request_body)

saveEntityTelemetryWithTTL

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
swagger_client.configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TelemetrycontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
scope = 'scope_example' # str | scope
ttl = 789 # int | ttl
request_body = 'request_body_example' # str | requestBody

try: 
    # saveEntityTelemetryWithTTL
    api_response = api_instance.save_entity_telemetry_with_ttl_using_post(entity_type, entity_id, scope, ttl, request_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TelemetrycontrollerApi->save_entity_telemetry_with_ttl_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **scope** | **str**| scope | 
 **ttl** | **int**| ttl | 
 **request_body** | **str**| requestBody | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

