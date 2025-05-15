# DocumentSign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document | [optional] 
**sign_url** | **str** | Secured url to access your doc | [optional] 
**expired_at** | **datetime** | Timestamp when signed URL will expire. Your signUrl can&#39;t be used any more after this date. | [optional] 
**created_at** | **datetime** | Timestamp when signed url has been emit. | [optional] 

## Example

```python
from verbatim_client.models.document_sign import DocumentSign

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSign from a JSON string
document_sign_instance = DocumentSign.from_json(json)
# print the JSON string representation of the object
print(DocumentSign.to_json())

# convert the object into a dict
document_sign_dict = document_sign_instance.to_dict()
# create an instance of DocumentSign from a dict
document_sign_from_dict = DocumentSign.from_dict(document_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


