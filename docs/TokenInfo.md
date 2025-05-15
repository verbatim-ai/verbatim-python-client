# TokenInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Issuer of the token | [optional] 
**issued_at** | **datetime** | When this token has been produced | [optional] 
**expires_at** | **datetime** | Expiration date of this token | [optional] 
**organization_id** | **str** | ID of the organization who owned the authenticate user | [optional] 
**user_id** | **str** | UID of the user, authenticated when the current token | [optional] 
**key_id** | **str** | ID of the key used to sign he token. Only for Verbatim issuer | [optional] 
**email** | **str** | Email of the authenticate user | [optional] 
**name** | **str** | Name of the authenticate user | [optional] 
**email_verified** | **bool** | True when email is verified | [optional] 

## Example

```python
from verbatim_client.models.token_info import TokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfo from a JSON string
token_info_instance = TokenInfo.from_json(json)
# print the JSON string representation of the object
print(TokenInfo.to_json())

# convert the object into a dict
token_info_dict = token_info_instance.to_dict()
# create an instance of TokenInfo from a dict
token_info_from_dict = TokenInfo.from_dict(token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


