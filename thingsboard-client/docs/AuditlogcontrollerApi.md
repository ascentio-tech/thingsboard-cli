# swagger_client.AuditlogcontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs_by_customer_id_using_get**](AuditlogcontrollerApi.md#get_audit_logs_by_customer_id_using_get) | **GET** /api/audit/logs/customer/{customerId} | getAuditLogsByCustomerId
[**get_audit_logs_by_entity_id_using_get**](AuditlogcontrollerApi.md#get_audit_logs_by_entity_id_using_get) | **GET** /api/audit/logs/entity/{entityType}/{entityId} | getAuditLogsByEntityId
[**get_audit_logs_by_user_id_using_get**](AuditlogcontrollerApi.md#get_audit_logs_by_user_id_using_get) | **GET** /api/audit/logs/user/{userId} | getAuditLogsByUserId
[**get_audit_logs_using_get**](AuditlogcontrollerApi.md#get_audit_logs_using_get) | **GET** /api/audit/logs | getAuditLogs


# **get_audit_logs_by_customer_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_customer_id_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getAuditLogsByCustomerId

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
api_instance = swagger_client.AuditlogcontrollerApi()
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getAuditLogsByCustomerId
    api_response = api_instance.get_audit_logs_by_customer_id_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogcontrollerApi->get_audit_logs_by_customer_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_by_entity_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_entity_id_using_get(entity_type, entity_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getAuditLogsByEntityId

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
api_instance = swagger_client.AuditlogcontrollerApi()
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getAuditLogsByEntityId
    api_response = api_instance.get_audit_logs_by_entity_id_using_get(entity_type, entity_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogcontrollerApi->get_audit_logs_by_entity_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_by_user_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_user_id_using_get(user_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getAuditLogsByUserId

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
api_instance = swagger_client.AuditlogcontrollerApi()
user_id = 'user_id_example' # str | userId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getAuditLogsByUserId
    api_response = api_instance.get_audit_logs_by_user_id_using_get(user_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogcontrollerApi->get_audit_logs_by_user_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_using_get**
> TimePageDataAuditLog get_audit_logs_using_get(limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getAuditLogs

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
api_instance = swagger_client.AuditlogcontrollerApi()
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getAuditLogs
    api_response = api_instance.get_audit_logs_using_get(limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditlogcontrollerApi->get_audit_logs_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

