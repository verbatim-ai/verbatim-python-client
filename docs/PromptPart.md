# PromptPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | define the beginning of the substring in the answer which is attached to a document. Document is defined by the attachmentIndex | [optional] 
**end** | **int** | define the end of the substring in the answer which is attached to a document.Document is defined by the attachmentIndex | [optional] 
**index** | **int** | Index of the attachment related to this substring | [optional] 
**kind** | **str** | Kind of attachment. For web, you&#39;ll found the attachment in web[index]. For document, you&#39;ll found the attachment in document[index] | [optional] 

## Example

```python
from verbatim_client.models.prompt_part import PromptPart

# TODO update the JSON string below
json = "{}"
# create an instance of PromptPart from a JSON string
prompt_part_instance = PromptPart.from_json(json)
# print the JSON string representation of the object
print(PromptPart.to_json())

# convert the object into a dict
prompt_part_dict = prompt_part_instance.to_dict()
# create an instance of PromptPart from a dict
prompt_part_from_dict = PromptPart.from_dict(prompt_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


