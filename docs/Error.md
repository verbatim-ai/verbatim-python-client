# Error

API response error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp of the error | [optional] 
**status** | **int** | HTTP Code | [optional] 
**error** | **str** | HTTP Error | [optional] 
**message** | **str** | Error message | [optional] 
**path** | **str** | Path of the initial request | [optional] 

## Example

```python
from verbatim_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


