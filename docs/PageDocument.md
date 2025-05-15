# PageDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Document]**](Document.md) |  | [optional] 
**next_page_token** | **object** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from verbatim_client.models.page_document import PageDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PageDocument from a JSON string
page_document_instance = PageDocument.from_json(json)
# print the JSON string representation of the object
print(PageDocument.to_json())

# convert the object into a dict
page_document_dict = page_document_instance.to_dict()
# create an instance of PageDocument from a dict
page_document_from_dict = PageDocument.from_dict(page_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


