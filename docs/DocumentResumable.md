# DocumentResumable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**corpus_id** | **str** | ID of the corpus where the document is stored | [optional] 
**state** | **str** | Storage size, given in bytes | [optional] 
**filename** | **str** | Filename of the document | [optional] 
**content_type** | **str** | Content type of the document | [optional] 
**size** | **int** | Storage size, given in bytes | [optional] 
**nb_pages** | **int** | Total number of pages in the document | [optional] 
**pages** | [**List[DocumentPage]**](DocumentPage.md) | Info abouts pages of the document (title, previews, fileId of the preview) | [optional] 
**upload_session_url** | **str** | Upload url to push chunks of your file.**[Resumable documentation from Google](https://cloud.google.com/storage/docs/performing-resumable-uploads#chunked-upload)** and **[our Cookbook](https://www.verbatim.cloud/cookbook/resumable-uploads)** explain how use this &#x60;uploadSessionURL&#x60; | [optional] 
**upload_session_expired_at** | **datetime** | Timestamp when URL will be expired. &#x60;uploadSessionURL&#x60; can&#39;t be used any more after the date | [optional] 

## Example

```python
from verbatim_client.models.document_resumable import DocumentResumable

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResumable from a JSON string
document_resumable_instance = DocumentResumable.from_json(json)
# print the JSON string representation of the object
print(DocumentResumable.to_json())

# convert the object into a dict
document_resumable_dict = document_resumable_instance.to_dict()
# create an instance of DocumentResumable from a dict
document_resumable_from_dict = DocumentResumable.from_dict(document_resumable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


