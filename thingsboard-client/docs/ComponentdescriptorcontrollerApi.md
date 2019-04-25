# swagger_client.ComponentdescriptorcontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_component_descriptor_by_clazz_using_get**](ComponentdescriptorcontrollerApi.md#get_component_descriptor_by_clazz_using_get) | **GET** /api/component/{componentDescriptorClazz} | getComponentDescriptorByClazz
[**get_component_descriptors_by_type_using_get**](ComponentdescriptorcontrollerApi.md#get_component_descriptors_by_type_using_get) | **GET** /api/components/{componentType} | getComponentDescriptorsByType
[**get_component_descriptors_by_types_using_get**](ComponentdescriptorcontrollerApi.md#get_component_descriptors_by_types_using_get) | **GET** /api/components | getComponentDescriptorsByTypes


# **get_component_descriptor_by_clazz_using_get**
> ComponentDescriptor get_component_descriptor_by_clazz_using_get(component_descriptor_clazz)

getComponentDescriptorByClazz

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
api_instance = swagger_client.ComponentdescriptorcontrollerApi()
component_descriptor_clazz = 'component_descriptor_clazz_example' # str | componentDescriptorClazz

try: 
    # getComponentDescriptorByClazz
    api_response = api_instance.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ComponentdescriptorcontrollerApi->get_component_descriptor_by_clazz_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_descriptor_clazz** | **str**| componentDescriptorClazz | 

### Return type

[**ComponentDescriptor**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_descriptors_by_type_using_get**
> list[ComponentDescriptor] get_component_descriptors_by_type_using_get(component_type)

getComponentDescriptorsByType

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
api_instance = swagger_client.ComponentdescriptorcontrollerApi()
component_type = 'component_type_example' # str | componentType

try: 
    # getComponentDescriptorsByType
    api_response = api_instance.get_component_descriptors_by_type_using_get(component_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ComponentdescriptorcontrollerApi->get_component_descriptors_by_type_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| componentType | 

### Return type

[**list[ComponentDescriptor]**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_descriptors_by_types_using_get**
> list[ComponentDescriptor] get_component_descriptors_by_types_using_get(component_types)

getComponentDescriptorsByTypes

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
api_instance = swagger_client.ComponentdescriptorcontrollerApi()
component_types = 'component_types_example' # str | componentTypes

try: 
    # getComponentDescriptorsByTypes
    api_response = api_instance.get_component_descriptors_by_types_using_get(component_types)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ComponentdescriptorcontrollerApi->get_component_descriptors_by_types_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_types** | **str**| componentTypes | 

### Return type

[**list[ComponentDescriptor]**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

