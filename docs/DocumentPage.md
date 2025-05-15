# DocumentPage

Page of the document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the page, 0 for the first, n-1 for the last one | [optional] 
**title** | **str** | Title of the page | [optional] 

## Example

```python
from verbatim_client.models.document_page import DocumentPage

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPage from a JSON string
document_page_instance = DocumentPage.from_json(json)
# print the JSON string representation of the object
print(DocumentPage.to_json())

# convert the object into a dict
document_page_dict = document_page_instance.to_dict()
# create an instance of DocumentPage from a dict
document_page_from_dict = DocumentPage.from_dict(document_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


