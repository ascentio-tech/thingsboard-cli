# swagger_client.RulechaincontrollerApi

All URIs are relative to *https://demo-epec:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rule_chain_using_delete**](RulechaincontrollerApi.md#delete_rule_chain_using_delete) | **DELETE** /api/ruleChain/{ruleChainId} | deleteRuleChain
[**get_latest_rule_node_debug_input_using_get**](RulechaincontrollerApi.md#get_latest_rule_node_debug_input_using_get) | **GET** /api/ruleNode/{ruleNodeId}/debugIn | getLatestRuleNodeDebugInput
[**get_rule_chain_by_id_using_get**](RulechaincontrollerApi.md#get_rule_chain_by_id_using_get) | **GET** /api/ruleChain/{ruleChainId} | getRuleChainById
[**get_rule_chain_meta_data_using_get**](RulechaincontrollerApi.md#get_rule_chain_meta_data_using_get) | **GET** /api/ruleChain/{ruleChainId}/metadata | getRuleChainMetaData
[**get_rule_chains_using_get**](RulechaincontrollerApi.md#get_rule_chains_using_get) | **GET** /api/ruleChains | getRuleChains
[**save_rule_chain_meta_data_using_post**](RulechaincontrollerApi.md#save_rule_chain_meta_data_using_post) | **POST** /api/ruleChain/metadata | saveRuleChainMetaData
[**save_rule_chain_using_post**](RulechaincontrollerApi.md#save_rule_chain_using_post) | **POST** /api/ruleChain | saveRuleChain
[**set_root_rule_chain_using_post**](RulechaincontrollerApi.md#set_root_rule_chain_using_post) | **POST** /api/ruleChain/{ruleChainId}/root | setRootRuleChain
[**test_script_using_post**](RulechaincontrollerApi.md#test_script_using_post) | **POST** /api/ruleChain/testScript | testScript


# **delete_rule_chain_using_delete**
> delete_rule_chain_using_delete(rule_chain_id)

deleteRuleChain

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain_id = 'rule_chain_id_example' # str | ruleChainId

try: 
    # deleteRuleChain
    api_instance.delete_rule_chain_using_delete(rule_chain_id)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->delete_rule_chain_using_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain_id** | **str**| ruleChainId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_rule_node_debug_input_using_get**
> str get_latest_rule_node_debug_input_using_get(rule_node_id)

getLatestRuleNodeDebugInput

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_node_id = 'rule_node_id_example' # str | ruleNodeId

try: 
    # getLatestRuleNodeDebugInput
    api_response = api_instance.get_latest_rule_node_debug_input_using_get(rule_node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->get_latest_rule_node_debug_input_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_node_id** | **str**| ruleNodeId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_chain_by_id_using_get**
> RuleChain get_rule_chain_by_id_using_get(rule_chain_id)

getRuleChainById

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain_id = 'rule_chain_id_example' # str | ruleChainId

try: 
    # getRuleChainById
    api_response = api_instance.get_rule_chain_by_id_using_get(rule_chain_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->get_rule_chain_by_id_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain_id** | **str**| ruleChainId | 

### Return type

[**RuleChain**](RuleChain.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_chain_meta_data_using_get**
> RuleChainMetaData get_rule_chain_meta_data_using_get(rule_chain_id)

getRuleChainMetaData

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain_id = 'rule_chain_id_example' # str | ruleChainId

try: 
    # getRuleChainMetaData
    api_response = api_instance.get_rule_chain_meta_data_using_get(rule_chain_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->get_rule_chain_meta_data_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain_id** | **str**| ruleChainId | 

### Return type

[**RuleChainMetaData**](RuleChainMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_chains_using_get**
> TextPageDataRuleChain get_rule_chains_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getRuleChains

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
api_instance = swagger_client.RulechaincontrollerApi()
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getRuleChains
    api_response = api_instance.get_rule_chains_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->get_rule_chains_using_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataRuleChain**](TextPageDataRuleChain.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_rule_chain_meta_data_using_post**
> RuleChainMetaData save_rule_chain_meta_data_using_post(rule_chain_meta_data)

saveRuleChainMetaData

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain_meta_data = swagger_client.RuleChainMetaData() # RuleChainMetaData | ruleChainMetaData

try: 
    # saveRuleChainMetaData
    api_response = api_instance.save_rule_chain_meta_data_using_post(rule_chain_meta_data)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->save_rule_chain_meta_data_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain_meta_data** | [**RuleChainMetaData**](RuleChainMetaData.md)| ruleChainMetaData | 

### Return type

[**RuleChainMetaData**](RuleChainMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_rule_chain_using_post**
> RuleChain save_rule_chain_using_post(rule_chain)

saveRuleChain

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain = swagger_client.RuleChain() # RuleChain | ruleChain

try: 
    # saveRuleChain
    api_response = api_instance.save_rule_chain_using_post(rule_chain)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->save_rule_chain_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain** | [**RuleChain**](RuleChain.md)| ruleChain | 

### Return type

[**RuleChain**](RuleChain.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_root_rule_chain_using_post**
> RuleChain set_root_rule_chain_using_post(rule_chain_id)

setRootRuleChain

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
api_instance = swagger_client.RulechaincontrollerApi()
rule_chain_id = 'rule_chain_id_example' # str | ruleChainId

try: 
    # setRootRuleChain
    api_response = api_instance.set_root_rule_chain_using_post(rule_chain_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->set_root_rule_chain_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_chain_id** | **str**| ruleChainId | 

### Return type

[**RuleChain**](RuleChain.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_script_using_post**
> str test_script_using_post(input_params)

testScript

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
api_instance = swagger_client.RulechaincontrollerApi()
input_params = 'input_params_example' # str | inputParams

try: 
    # testScript
    api_response = api_instance.test_script_using_post(input_params)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RulechaincontrollerApi->test_script_using_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_params** | **str**| inputParams | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

