# swagger_client.CustomercontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_using_delete**](CustomercontrollerApi.md#delete_customer_using_delete) | **DELETE** /api/customer/{customerId} | deleteCustomer
[**get_customer_by_id_using_get**](CustomercontrollerApi.md#get_customer_by_id_using_get) | **GET** /api/customer/{customerId} | getCustomerById
[**get_customer_title_by_id_using_get**](CustomercontrollerApi.md#get_customer_title_by_id_using_get) | **GET** /api/customer/{customerId}/title | getCustomerTitleById
[**get_customers_using_get**](CustomercontrollerApi.md#get_customers_using_get) | **GET** /api/customers | getCustomers
[**get_short_customer_info_by_id_using_get**](CustomercontrollerApi.md#get_short_customer_info_by_id_using_get) | **GET** /api/customer/{customerId}/shortInfo | getShortCustomerInfoById
[**get_tenant_customer_using_get**](CustomercontrollerApi.md#get_tenant_customer_using_get) | **GET** /api/tenant/customers | getTenantCustomer
[**save_customer_using_post**](CustomercontrollerApi.md#save_customer_using_post) | **POST** /api/customer | saveCustomer


# **delete_customer_using_delete**
> delete_customer_using_delete(customer_id)

deleteCustomer

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
api_instance = swagger_client.CustomercontrollerApi()
customer_id = 'customer_id_example' # str | customerId

try: 
    # deleteCustomer
    api_instance.delete_customer_using_delete(customer_id)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->delete_customer_using_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_id_using_get**
> Customer get_customer_by_id_using_get(customer_id)

getCustomerById

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
api_instance = swagger_client.CustomercontrollerApi()
customer_id = 'customer_id_example' # str | customerId

try: 
    # getCustomerById
    api_response = api_instance.get_customer_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->get_customer_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_title_by_id_using_get**
> str get_customer_title_by_id_using_get(customer_id)

getCustomerTitleById

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
api_instance = swagger_client.CustomercontrollerApi()
customer_id = 'customer_id_example' # str | customerId

try: 
    # getCustomerTitleById
    api_response = api_instance.get_customer_title_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->get_customer_title_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_using_get**
> TextPageDataCustomer get_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomers

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
api_instance = swagger_client.CustomercontrollerApi()
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getCustomers
    api_response = api_instance.get_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->get_customers_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataCustomer**](TextPageDataCustomer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_short_customer_info_by_id_using_get**
> str get_short_customer_info_by_id_using_get(customer_id)

getShortCustomerInfoById

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
api_instance = swagger_client.CustomercontrollerApi()
customer_id = 'customer_id_example' # str | customerId

try: 
    # getShortCustomerInfoById
    api_response = api_instance.get_short_customer_info_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->get_short_customer_info_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_customer_using_get**
> Customer get_tenant_customer_using_get(customer_title)

getTenantCustomer

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
api_instance = swagger_client.CustomercontrollerApi()
customer_title = 'customer_title_example' # str | customerTitle

try: 
    # getTenantCustomer
    api_response = api_instance.get_tenant_customer_using_get(customer_title)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->get_tenant_customer_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_title** | **str**| customerTitle | 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_customer_using_post**
> Customer save_customer_using_post(customer)

saveCustomer

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
api_instance = swagger_client.CustomercontrollerApi()
customer = swagger_client.Customer() # Customer | customer

try: 
    # saveCustomer
    api_response = api_instance.save_customer_using_post(customer)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomercontrollerApi->save_customer_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| customer | 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

