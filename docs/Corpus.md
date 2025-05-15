# Corpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of the Corpus | [optional] 
**description** | **str** | Description of the Corpus | [optional] 
**created_at** | **datetime** | Creation date of the corpus | [optional] 
**updated_at** | **datetime** | Last update on the corpus | [optional] 
**org_id** | **str** | ID of your organization. Internal use only | [optional] 
**id** | **str** | ID of the Corpus. Use this ID as primary key on API | [optional] 
**nb_doc** | **int** | Number of doc in the Corpus | [optional] 
**size** | **int** | Size (in bytes) of the corpus | [optional] 

## Example

```python
from verbatim_client.models.corpus import Corpus

# TODO update the JSON string below
json = "{}"
# create an instance of Corpus from a JSON string
corpus_instance = Corpus.from_json(json)
# print the JSON string representation of the object
print(Corpus.to_json())

# convert the object into a dict
corpus_dict = corpus_instance.to_dict()
# create an instance of Corpus from a dict
corpus_from_dict = Corpus.from_dict(corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


