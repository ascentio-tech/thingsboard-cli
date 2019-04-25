# swagger_client.TenantcontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tenant_using_delete**](TenantcontrollerApi.md#delete_tenant_using_delete) | **DELETE** /api/tenant/{tenantId} | deleteTenant
[**get_tenant_by_id_using_get**](TenantcontrollerApi.md#get_tenant_by_id_using_get) | **GET** /api/tenant/{tenantId} | getTenantById
[**get_tenants_using_get**](TenantcontrollerApi.md#get_tenants_using_get) | **GET** /api/tenants | getTenants
[**save_tenant_using_post**](TenantcontrollerApi.md#save_tenant_using_post) | **POST** /api/tenant | saveTenant


# **delete_tenant_using_delete**
> delete_tenant_using_delete(tenant_id)

deleteTenant

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
api_instance = swagger_client.TenantcontrollerApi()
tenant_id = 'tenant_id_example' # str | tenantId

try: 
    # deleteTenant
    api_instance.delete_tenant_using_delete(tenant_id)
except ApiException as e:
    print "Exception when calling TenantcontrollerApi->delete_tenant_using_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_by_id_using_get**
> Tenant get_tenant_by_id_using_get(tenant_id)

getTenantById

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
api_instance = swagger_client.TenantcontrollerApi()
tenant_id = 'tenant_id_example' # str | tenantId

try: 
    # getTenantById
    api_response = api_instance.get_tenant_by_id_using_get(tenant_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TenantcontrollerApi->get_tenant_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenants_using_get**
> TextPageDataTenant get_tenants_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenants

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
api_instance = swagger_client.TenantcontrollerApi()
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenants
    api_response = api_instance.get_tenants_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TenantcontrollerApi->get_tenants_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataTenant**](TextPageDataTenant.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_tenant_using_post**
> Tenant save_tenant_using_post(tenant)

saveTenant

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
api_instance = swagger_client.TenantcontrollerApi()
tenant = swagger_client.Tenant() # Tenant | tenant

try: 
    # saveTenant
    api_response = api_instance.save_tenant_using_post(tenant)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TenantcontrollerApi->save_tenant_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | [**Tenant**](Tenant.md)| tenant | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

