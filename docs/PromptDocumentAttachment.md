# PromptDocumentAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document id | [optional] 
**text** | **str** | Grounding text attach to the prompt | [optional] 
**pages** | **List[int]** | List of the index of the pages in the document attach to this prompt | [optional] 
**document** | [**Document**](Document.md) | Main document related to this attachment | [optional] 

## Example

```python
from verbatim_client.models.prompt_document_attachment import PromptDocumentAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of PromptDocumentAttachment from a JSON string
prompt_document_attachment_instance = PromptDocumentAttachment.from_json(json)
# print the JSON string representation of the object
print(PromptDocumentAttachment.to_json())

# convert the object into a dict
prompt_document_attachment_dict = prompt_document_attachment_instance.to_dict()
# create an instance of PromptDocumentAttachment from a dict
prompt_document_attachment_from_dict = PromptDocumentAttachment.from_dict(prompt_document_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


