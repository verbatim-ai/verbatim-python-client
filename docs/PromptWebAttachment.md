# PromptWebAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document id | [optional] 
**text** | **str** | Grounding text attach to the prompt | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.prompt_web_attachment import PromptWebAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of PromptWebAttachment from a JSON string
prompt_web_attachment_instance = PromptWebAttachment.from_json(json)
# print the JSON string representation of the object
print(PromptWebAttachment.to_json())

# convert the object into a dict
prompt_web_attachment_dict = prompt_web_attachment_instance.to_dict()
# create an instance of PromptWebAttachment from a dict
prompt_web_attachment_from_dict = PromptWebAttachment.from_dict(prompt_web_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


