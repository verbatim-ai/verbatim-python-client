# WebPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**corpus_id** | **str** | ID of the corpus where the document is stored | [optional] 
**state** | **str** | Storage size, given in bytes | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from verbatim_client.models.web_page import WebPage

# TODO update the JSON string below
json = "{}"
# create an instance of WebPage from a JSON string
web_page_instance = WebPage.from_json(json)
# print the JSON string representation of the object
print(WebPage.to_json())

# convert the object into a dict
web_page_dict = web_page_instance.to_dict()
# create an instance of WebPage from a dict
web_page_from_dict = WebPage.from_dict(web_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


