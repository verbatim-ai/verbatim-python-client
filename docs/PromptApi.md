# verbatim_client.PromptApi

All URIs are relative to *https://api.verbatim.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prompt**](PromptApi.md#prompt) | **GET** /v1/prompt/{corpusId} | Run a prompt


# **prompt**
> PromptResponse prompt(corpus_id, model, query)

Run a prompt

Your prompt is process in the engine. Semantic response if give in the body with attachments found from your corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.prompt_response import PromptResponse
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
    api_instance = verbatim_client.PromptApi(api_client)
    corpus_id = 'corpus_id_example' # str | ID of your corpus
    model = 'gemini_15_pro' # str | AI Model to use
    query = 'What is the name of the Uk prime minister ?' # str | Query to run on the engine (Max 1014 characters allowed)

    try:
        # Run a prompt
        api_response = api_instance.prompt(corpus_id, model, query)
        print("The response of PromptApi->prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptApi->prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| ID of your corpus | 
 **model** | **str**| AI Model to use | 
 **query** | **str**| Query to run on the engine (Max 1014 characters allowed) | 

### Return type

[**PromptResponse**](PromptResponse.md)

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
**200** | Response is given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

