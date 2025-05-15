# verbatim_client.CorpusApi

All URIs are relative to *https://api.verbatim.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add1**](CorpusApi.md#add1) | **POST** /v1/corpus | Create a new corpus
[**delete1**](CorpusApi.md#delete1) | **DELETE** /v1/corpus/{corpusId} | Delete a Corpus
[**get1**](CorpusApi.md#get1) | **GET** /v1/corpus/{corpusId} | Get a Corpus
[**list2**](CorpusApi.md#list2) | **GET** /v1/corpus | List corpus
[**update1**](CorpusApi.md#update1) | **PUT** /v1/corpus/{corpusId} | Update metadata of a Corpus


# **add1**
> Corpus add1(corpus_metadata)

Create a new corpus

Create a new corpus where your documents will be stored

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.corpus import Corpus
from verbatim_client.models.corpus_metadata import CorpusMetadata
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_metadata = verbatim_client.CorpusMetadata() # CorpusMetadata | 

    try:
        # Create a new corpus
        api_response = api_instance.add1(corpus_metadata)
        print("The response of CorpusApi->add1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->add1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_metadata** | [**CorpusMetadata**](CorpusMetadata.md)|  | 

### Return type

[**Corpus**](Corpus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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
**200** | Corpus is ready to use. ID of your corpus is given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> delete1(corpus_id)

Delete a Corpus

Permanent removal of a Corpus. No restore after a delete.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus

    try:
        # Delete a Corpus
        api_instance.delete1(corpus_id)
    except Exception as e:
        print("Exception when calling CorpusApi->delete1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 

### Return type

void (empty response body)

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
**200** | Corpus is deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> Corpus get1(corpus_id)

Get a Corpus

Get detail info about a Corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.corpus import Corpus
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus

    try:
        # Get a Corpus
        api_response = api_instance.get1(corpus_id)
        print("The response of CorpusApi->get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 

### Return type

[**Corpus**](Corpus.md)

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
**200** | Corpus given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list2**
> PageCorpus list2(page_token=page_token, page_size=page_size)

List corpus

List your corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.page_corpus import PageCorpus
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
    api_instance = verbatim_client.CorpusApi(api_client)
    page_token = 'page_token_example' # str | Page token (optional)
    page_size = 25 # int | Page size (optional) (default to 25)

    try:
        # List corpus
        api_response = api_instance.list2(page_token=page_token, page_size=page_size)
        print("The response of CorpusApi->list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| Page token | [optional] 
 **page_size** | **int**| Page size | [optional] [default to 25]

### Return type

[**PageCorpus**](PageCorpus.md)

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
**200** | page of corpus given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> Corpus update1(corpus_id, corpus_metadata)

Update metadata of a Corpus

Update display info of your corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.corpus import Corpus
from verbatim_client.models.corpus_metadata import CorpusMetadata
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
    api_instance = verbatim_client.CorpusApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpusId
    corpus_metadata = verbatim_client.CorpusMetadata() # CorpusMetadata | 

    try:
        # Update metadata of a Corpus
        api_response = api_instance.update1(corpus_id, corpus_metadata)
        print("The response of CorpusApi->update1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorpusApi->update1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpusId | 
 **corpus_metadata** | [**CorpusMetadata**](CorpusMetadata.md)|  | 

### Return type

[**Corpus**](Corpus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
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
**200** | Updated corpus given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

