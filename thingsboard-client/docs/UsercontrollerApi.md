# swagger_client.UsercontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_using_delete**](UsercontrollerApi.md#delete_user_using_delete) | **DELETE** /api/user/{userId} | deleteUser
[**get_activation_link_using_get**](UsercontrollerApi.md#get_activation_link_using_get) | **GET** /api/user/{userId}/activationLink | getActivationLink
[**get_customer_users_using_get**](UsercontrollerApi.md#get_customer_users_using_get) | **GET** /api/customer/{customerId}/users | getCustomerUsers
[**get_tenant_admins_using_get**](UsercontrollerApi.md#get_tenant_admins_using_get) | **GET** /api/tenant/{tenantId}/users | getTenantAdmins
[**get_user_by_id_using_get**](UsercontrollerApi.md#get_user_by_id_using_get) | **GET** /api/user/{userId} | getUserById
[**get_user_token_using_get**](UsercontrollerApi.md#get_user_token_using_get) | **GET** /api/user/{userId}/token | getUserToken
[**is_user_token_access_enabled_using_get**](UsercontrollerApi.md#is_user_token_access_enabled_using_get) | **GET** /api/user/tokenAccessEnabled | isUserTokenAccessEnabled
[**save_user_using_post**](UsercontrollerApi.md#save_user_using_post) | **POST** /api/user | saveUser
[**send_activation_email_using_post**](UsercontrollerApi.md#send_activation_email_using_post) | **POST** /api/user/sendActivationMail | sendActivationEmail


# **delete_user_using_delete**
> delete_user_using_delete(user_id)

deleteUser

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
api_instance = swagger_client.UsercontrollerApi()
user_id = 'user_id_example' # str | userId

try: 
    # deleteUser
    api_instance.delete_user_using_delete(user_id)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->delete_user_using_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation_link_using_get**
> str get_activation_link_using_get(user_id)

getActivationLink

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
api_instance = swagger_client.UsercontrollerApi()
user_id = 'user_id_example' # str | userId

try: 
    # getActivationLink
    api_response = api_instance.get_activation_link_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->get_activation_link_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_users_using_get**
> TextPageDataUser get_customer_users_using_get(customer_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerUsers

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
api_instance = swagger_client.UsercontrollerApi()
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getCustomerUsers
    api_response = api_instance.get_customer_users_using_get(customer_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->get_customer_users_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_admins_using_get**
> TextPageDataUser get_tenant_admins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantAdmins

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
api_instance = swagger_client.UsercontrollerApi()
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantAdmins
    api_response = api_instance.get_tenant_admins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->get_tenant_admins_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id_using_get**
> User get_user_by_id_using_get(user_id)

getUserById

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
api_instance = swagger_client.UsercontrollerApi()
user_id = 'user_id_example' # str | userId

try: 
    # getUserById
    api_response = api_instance.get_user_by_id_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->get_user_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

[**User**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token_using_get**
> str get_user_token_using_get(user_id)

getUserToken

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
api_instance = swagger_client.UsercontrollerApi()
user_id = 'user_id_example' # str | userId

try: 
    # getUserToken
    api_response = api_instance.get_user_token_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->get_user_token_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_user_token_access_enabled_using_get**
> bool is_user_token_access_enabled_using_get()

isUserTokenAccessEnabled

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
api_instance = swagger_client.UsercontrollerApi()

try: 
    # isUserTokenAccessEnabled
    api_response = api_instance.is_user_token_access_enabled_using_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->is_user_token_access_enabled_using_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_using_post**
> User save_user_using_post(user, send_activation_mail=send_activation_mail)

saveUser

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
api_instance = swagger_client.UsercontrollerApi()
user = swagger_client.User() # User | user
send_activation_mail = true # bool | sendActivationMail (optional) (default to true)

try: 
    # saveUser
    api_response = api_instance.save_user_using_post(user, send_activation_mail=send_activation_mail)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->save_user_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| user | 
 **send_activation_mail** | **bool**| sendActivationMail | [optional] [default to true]

### Return type

[**User**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_activation_email_using_post**
> send_activation_email_using_post(email)

sendActivationEmail

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
api_instance = swagger_client.UsercontrollerApi()
email = 'email_example' # str | email

try: 
    # sendActivationEmail
    api_instance.send_activation_email_using_post(email)
except ApiException as e:
    print "Exception when calling UsercontrollerApi->send_activation_email_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

