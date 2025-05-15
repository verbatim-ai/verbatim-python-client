# verbatim_client.AuthenticateApi

All URIs are relative to *https://api.verbatim.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**whoami**](AuthenticateApi.md#whoami) | **GET** /v1/auth/whoami | Info about the token used for authenticated this query


# **whoami**
> TokenInfo whoami()

Info about the token used for authenticated this query

Get info about the active session (token)

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.token_info import TokenInfo
from verbatim_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.verbatim.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = verbatim_client.Configuration(
    host = "https://api.verbatim.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = verbatim_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with verbatim_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = verbatim_client.AuthenticateApi(api_client)

    try:
        # Info about the token used for authenticated this query
        api_response = api_instance.whoami()
        print("The response of AuthenticateApi->whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticateApi->whoami: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenInfo**](TokenInfo.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal error. Check body to get more info |  -  |
**429** | Too many request. Check your quota on your dashboard |  -  |
**503** | Service temporary not available. Reason is given the body |  -  |
**403** | Not authorized. Access not granted for this request |  -  |
**404** | Document not found |  -  |
**400** | Bad request. Invalid body or missing parameter |  -  |
**200** | Token info given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

