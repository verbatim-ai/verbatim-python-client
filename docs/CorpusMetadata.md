# CorpusMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display nme of your Corpus. Name attached to your corpus but not used a sa key | [optional] 
**description** | **str** | Description nme of your Corpus | [optional] 

## Example

```python
from verbatim_client.models.corpus_metadata import CorpusMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CorpusMetadata from a JSON string
corpus_metadata_instance = CorpusMetadata.from_json(json)
# print the JSON string representation of the object
print(CorpusMetadata.to_json())

# convert the object into a dict
corpus_metadata_dict = corpus_metadata_instance.to_dict()
# create an instance of CorpusMetadata from a dict
corpus_metadata_from_dict = CorpusMetadata.from_dict(corpus_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


