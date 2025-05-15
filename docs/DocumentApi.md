# verbatim_client.DocumentApi

All URIs are relative to *https://api.verbatim.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete2**](DocumentApi.md#delete2) | **DELETE** /v1/doc/{corpusId}/id/{documentId} | Delete a document
[**download**](DocumentApi.md#download) | **GET** /v1/doc/{corpusId}/doc/{documentId}/download | Get the download link
[**get_doc**](DocumentApi.md#get_doc) | **GET** /v1/doc/{corpusId}/doc/{documentId} | Get a document
[**get_web_page**](DocumentApi.md#get_web_page) | **GET** /v1/doc/{corpusId}/web/{documentId} | Get a WebPage
[**list**](DocumentApi.md#list) | **GET** /v1/doc/{corpusId} | List documents
[**preview_doc**](DocumentApi.md#preview_doc) | **GET** /v1/doc/{corpusId}/doc/{documentId}/page/{pageIndex}/preview/{previewSize} | Preview a document image
[**preview_web**](DocumentApi.md#preview_web) | **GET** /v1/doc/{corpusId}/web/{documentId}/preview/{previewSize} | Preview a web page
[**upload**](DocumentApi.md#upload) | **POST** /v1/doc/{corpusId} | Upload a document


# **delete2**
> delete2(corpus_id, document_id)

Delete a document

Delete a document from your corpus

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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document

    try:
        # Delete a document
        api_instance.delete2(corpus_id, document_id)
    except Exception as e:
        print("Exception when calling DocumentApi->delete2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 

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
**200** | Document has been deleted form your corpus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> DocumentSign download(corpus_id, document_id)

Get the download link

Get a secured and signed urls to download file from a document ID

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.document_sign import DocumentSign
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document

    try:
        # Get the download link
        api_response = api_instance.download(corpus_id, document_id)
        print("The response of DocumentApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 

### Return type

[**DocumentSign**](DocumentSign.md)

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
**200** | Access url given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doc**
> Document get_doc(corpus_id, document_id)

Get a document

Get detail info about a Document

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.document import Document
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document

    try:
        # Get a document
        api_response = api_instance.get_doc(corpus_id, document_id)
        print("The response of DocumentApi->get_doc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get_doc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 

### Return type

[**Document**](Document.md)

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
**200** | Document given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_page**
> WebPage get_web_page(corpus_id, document_id)

Get a WebPage

Get detail info about a Web page

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.web_page import WebPage
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document

    try:
        # Get a WebPage
        api_response = api_instance.get_web_page(corpus_id, document_id)
        print("The response of DocumentApi->get_web_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->get_web_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 

### Return type

[**WebPage**](WebPage.md)

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
**200** | Document given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PageDocument list(corpus_id, page_token=page_token, page_size=page_size)

List documents

List documents available in your corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.page_document import PageDocument
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is pushed. See Corpus section to learn more
    page_token = 'page_token_example' # str | Page token. Null to get first page (optional)
    page_size = 25 # int | Page size (optional) (default to 25)

    try:
        # List documents
        api_response = api_instance.list(corpus_id, page_token=page_token, page_size=page_size)
        print("The response of DocumentApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is pushed. See Corpus section to learn more | 
 **page_token** | **str**| Page token. Null to get first page | [optional] 
 **page_size** | **int**| Page size | [optional] [default to 25]

### Return type

[**PageDocument**](PageDocument.md)

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
**200** | result page given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_doc**
> DocumentSign preview_doc(corpus_id, document_id, page_index, preview_size)

Preview a document image

Get the preview url of one of the page of the document.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.document_sign import DocumentSign
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document
    page_index = 56 # int | Index of the page in the document, use 0 for the first page
    preview_size = 'preview_size_example' # str | Size of the preview

    try:
        # Preview a document image
        api_response = api_instance.preview_doc(corpus_id, document_id, page_index, preview_size)
        print("The response of DocumentApi->preview_doc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->preview_doc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 
 **page_index** | **int**| Index of the page in the document, use 0 for the first page | 
 **preview_size** | **str**| Size of the preview | 

### Return type

[**DocumentSign**](DocumentSign.md)

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
**200** | Access url given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_web**
> DocumentSign preview_web(corpus_id, document_id, preview_size)

Preview a web page

Get the preview url of a web page.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.document_sign import DocumentSign
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is hosted. See Corpus section to learn more
    document_id = 'document_id_example' # str | Id of the document
    preview_size = 'preview_size_example' # str | Size of the preview

    try:
        # Preview a web page
        api_response = api_instance.preview_web(corpus_id, document_id, preview_size)
        print("The response of DocumentApi->preview_web:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->preview_web: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is hosted. See Corpus section to learn more | 
 **document_id** | **str**| Id of the document | 
 **preview_size** | **str**| Size of the preview | 

### Return type

[**DocumentSign**](DocumentSign.md)

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
**200** | Access url given in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> DocumentResumable upload(corpus_id, filename)

Upload a document

Upload a new document in a corpus

### Example

* Bearer (JWT) Authentication (JWT):

```python
import verbatim_client
from verbatim_client.models.document_resumable import DocumentResumable
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
    api_instance = verbatim_client.DocumentApi(api_client)
    corpus_id = 'corpus_id_example' # str | Id of the corpus where document is pushed. See [Corpus section](https://www.verbatim.cloud/api-docs/index.html#tag/Corpus) to learn more.
    filename = 'myfile.txt' # str | the name of your file (max 128 characters)

    try:
        # Upload a document
        api_response = api_instance.upload(corpus_id, filename)
        print("The response of DocumentApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpus_id** | **str**| Id of the corpus where document is pushed. See [Corpus section](https://www.verbatim.cloud/api-docs/index.html#tag/Corpus) to learn more. | 
 **filename** | **str**| the name of your file (max 128 characters) | 

### Return type

[**DocumentResumable**](DocumentResumable.md)

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
**200** | Document is ready to be uploaded. Resumable upload session is given in the body. Use uploadUrl to start the upload. Please check doc attached to field uploadUrl |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

