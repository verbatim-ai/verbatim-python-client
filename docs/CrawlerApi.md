# verbatim_client.CrawlerApi

All URIs are relative to *https://api.verbatim.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](CrawlerApi.md#add) | **POST** /v1/crawler/{corpusId} | Create a new crawler
[**delete**](CrawlerApi.md#delete) | **DELETE** /v1/crawler/{corpusId}/id/{crawlerId} | Delete a crawler
[**get**](CrawlerApi.md#get) | **GET** /v1/crawler/{corpusId}/id/{crawlerId} | Get a crawler
[**list1**](CrawlerApi.md#list1) | **GET** /v1/crawler/{corpusId} | List the crawler
[**update**](CrawlerApi.md#update) | **PUT** /v1/crawler/{corpusId}/id/{crawlerId} | Update metadata of a Crawler


# **add**
> Crawler add(corpus_id, crawler_metadata)

Create a new crawler

Create a new crawler. Only available if account has been init and attached to an organization

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.crawler import Crawler
from verbatim_client.models.crawler_metadata import CrawlerMetadata
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
    api_instance = verbatim_client.CrawlerApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus
    crawler_metadata = verbatim_client.CrawlerMetadata() # CrawlerMetadata | 

    try:
        # Create a new crawler
        api_response = api_instance.add(corpus_id, crawler_metadata)
        print("The response of CrawlerApi->add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlerApi->add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 
 **crawler_metadata** | [**CrawlerMetadata**](CrawlerMetadata.md)|  | 

### Return type

[**Crawler**](Crawler.md)

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
**200** | Corpus is ready to use |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(corpus_id, crawler_id)

Delete a crawler

Permanent removal of a crawler. No restore after a delete

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
    api_instance = verbatim_client.CrawlerApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus
    crawler_id = 'crawler_id_example' # str | Id of the crawler

    try:
        # Delete a crawler
        api_instance.delete(corpus_id, crawler_id)
    except Exception as e:
        print("Exception when calling CrawlerApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 
 **crawler_id** | **str**| Id of the crawler | 

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
**200** | Crawler is deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Crawler get(corpus_id, crawler_id)

Get a crawler

Get detail info about a Crawler

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.crawler import Crawler
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
    api_instance = verbatim_client.CrawlerApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus
    crawler_id = 'crawler_id_example' # str | Id of the crawler

    try:
        # Get a crawler
        api_response = api_instance.get(corpus_id, crawler_id)
        print("The response of CrawlerApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlerApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 
 **crawler_id** | **str**| Id of the crawler | 

### Return type

[**Crawler**](Crawler.md)

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
**200** | Crawler detail is given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list1**
> PageCrawler list1(corpus_id, page_token=page_token, page_size=page_size)

List the crawler

List your crawlers

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.page_crawler import PageCrawler
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
    api_instance = verbatim_client.CrawlerApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus
    page_token = 'page_token_example' # str | Page token. Null to fetch the first page (optional)
    page_size = 25 # int | Page size (max 100) (optional) (default to 25)

    try:
        # List the crawler
        api_response = api_instance.list1(corpus_id, page_token=page_token, page_size=page_size)
        print("The response of CrawlerApi->list1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlerApi->list1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 
 **page_token** | **str**| Page token. Null to fetch the first page | [optional] 
 **page_size** | **int**| Page size (max 100) | [optional] [default to 25]

### Return type

[**PageCrawler**](PageCrawler.md)

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
**200** | page of crawler given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Crawler update(corpus_id, crawler_id, crawler_metadata)

Update metadata of a Crawler

Update display info of your crawler

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.crawler import Crawler
from verbatim_client.models.crawler_metadata import CrawlerMetadata
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
    api_instance = verbatim_client.CrawlerApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus
    crawler_id = 'crawler_id_example' # str | Id of the crawler
    crawler_metadata = verbatim_client.CrawlerMetadata() # CrawlerMetadata | 

    try:
        # Update metadata of a Crawler
        api_response = api_instance.update(corpus_id, crawler_id, crawler_metadata)
        print("The response of CrawlerApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrawlerApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus | 
 **crawler_id** | **str**| Id of the crawler | 
 **crawler_metadata** | [**CrawlerMetadata**](CrawlerMetadata.md)|  | 

### Return type

[**Crawler**](Crawler.md)

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
**200** | Updated crawler given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

