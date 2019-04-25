# swagger_client.BillingcontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_cycle_using_post**](BillingcontrollerApi.md#create_billing_cycle_using_post) | **POST** /api/billing/cycle | createBillingCycle


# **create_billing_cycle_using_post**
> BillingInfoResponse create_billing_cycle_using_post()

createBillingCycle

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
api_instance = swagger_client.BillingcontrollerApi()

try: 
    # createBillingCycle
    api_response = api_instance.create_billing_cycle_using_post()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BillingcontrollerApi->create_billing_cycle_using_post: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillingInfoResponse**](BillingInfoResponse.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

