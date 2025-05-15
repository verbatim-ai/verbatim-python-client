# Document


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

## Example

```python
from verbatim_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


