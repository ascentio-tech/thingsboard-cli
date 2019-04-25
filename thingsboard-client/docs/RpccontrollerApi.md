# swagger_client.RpccontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_one_way_device_rpc_request_using_post**](RpccontrollerApi.md#handle_one_way_device_rpc_request_using_post) | **POST** /api/plugins/rpc/oneway/{deviceId} | handleOneWayDeviceRPCRequest
[**handle_two_way_device_rpc_request_using_post**](RpccontrollerApi.md#handle_two_way_device_rpc_request_using_post) | **POST** /api/plugins/rpc/twoway/{deviceId} | handleTwoWayDeviceRPCRequest


# **handle_one_way_device_rpc_request_using_post**
> DeferredResultResponseEntity handle_one_way_device_rpc_request_using_post(device_id, request_body)

handleOneWayDeviceRPCRequest

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
api_instance = swagger_client.RpccontrollerApi()
device_id = 'device_id_example' # str | deviceId
request_body = 'request_body_example' # str | requestBody

try: 
    # handleOneWayDeviceRPCRequest
    api_response = api_instance.handle_one_way_device_rpc_request_using_post(device_id, request_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RpccontrollerApi->handle_one_way_device_rpc_request_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **request_body** | **str**| requestBody | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_two_way_device_rpc_request_using_post**
> DeferredResultResponseEntity handle_two_way_device_rpc_request_using_post(device_id, request_body)

handleTwoWayDeviceRPCRequest

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
api_instance = swagger_client.RpccontrollerApi()
device_id = 'device_id_example' # str | deviceId
request_body = 'request_body_example' # str | requestBody

try: 
    # handleTwoWayDeviceRPCRequest
    api_response = api_instance.handle_two_way_device_rpc_request_using_post(device_id, request_body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RpccontrollerApi->handle_two_way_device_rpc_request_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **request_body** | **str**| requestBody | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

