# PromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issued_at** | **datetime** |  | [optional] 
**corpus_id** | **str** |  | [optional] 
**query** | **str** | Your query | [optional] 
**text** | **str** | Generative AI Agent answer to your query | [optional] 
**parts** | [**List[PromptPart]**](PromptPart.md) |  | [optional] 
**document** | [**List[PromptDocumentAttachment]**](PromptDocumentAttachment.md) |  | [optional] 
**web** | [**List[PromptWebAttachment]**](PromptWebAttachment.md) |  | [optional] 

## Example

```python
from verbatim_client.models.prompt_response import PromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptResponse from a JSON string
prompt_response_instance = PromptResponse.from_json(json)
# print the JSON string representation of the object
print(PromptResponse.to_json())

# convert the object into a dict
prompt_response_dict = prompt_response_instance.to_dict()
# create an instance of PromptResponse from a dict
prompt_response_from_dict = PromptResponse.from_dict(prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


