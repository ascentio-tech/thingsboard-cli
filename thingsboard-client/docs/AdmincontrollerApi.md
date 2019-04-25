# swagger_client.AdmincontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_updates_using_get**](AdmincontrollerApi.md#check_updates_using_get) | **GET** /api/admin/updates | checkUpdates
[**get_admin_settings_using_get**](AdmincontrollerApi.md#get_admin_settings_using_get) | **GET** /api/admin/settings/{key} | getAdminSettings
[**save_admin_settings_using_post**](AdmincontrollerApi.md#save_admin_settings_using_post) | **POST** /api/admin/settings | saveAdminSettings
[**send_test_mail_using_post**](AdmincontrollerApi.md#send_test_mail_using_post) | **POST** /api/admin/settings/testMail | sendTestMail


# **check_updates_using_get**
> UpdateMessage check_updates_using_get()

checkUpdates

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
api_instance = swagger_client.AdmincontrollerApi()

try: 
    # checkUpdates
    api_response = api_instance.check_updates_using_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdmincontrollerApi->check_updates_using_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateMessage**](UpdateMessage.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_settings_using_get**
> AdminSettings get_admin_settings_using_get(key)

getAdminSettings

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
api_instance = swagger_client.AdmincontrollerApi()
key = 'key_example' # str | key

try: 
    # getAdminSettings
    api_response = api_instance.get_admin_settings_using_get(key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdmincontrollerApi->get_admin_settings_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

### Return type

[**AdminSettings**](AdminSettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_admin_settings_using_post**
> AdminSettings save_admin_settings_using_post(admin_settings)

saveAdminSettings

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
api_instance = swagger_client.AdmincontrollerApi()
admin_settings = swagger_client.AdminSettings() # AdminSettings | adminSettings

try: 
    # saveAdminSettings
    api_response = api_instance.save_admin_settings_using_post(admin_settings)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdmincontrollerApi->save_admin_settings_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_settings** | [**AdminSettings**](AdminSettings.md)| adminSettings | 

### Return type

[**AdminSettings**](AdminSettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_mail_using_post**
> send_test_mail_using_post(admin_settings)

sendTestMail

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
api_instance = swagger_client.AdmincontrollerApi()
admin_settings = swagger_client.AdminSettings() # AdminSettings | adminSettings

try: 
    # sendTestMail
    api_instance.send_test_mail_using_post(admin_settings)
except ApiException as e:
    print "Exception when calling AdmincontrollerApi->send_test_mail_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_settings** | [**AdminSettings**](AdminSettings.md)| adminSettings | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

