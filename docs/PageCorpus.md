# PageCorpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Corpus]**](Corpus.md) |  | [optional] 
**next_page_token** | **object** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from verbatim_client.models.page_corpus import PageCorpus

# TODO update the JSON string below
json = "{}"
# create an instance of PageCorpus from a JSON string
page_corpus_instance = PageCorpus.from_json(json)
# print the JSON string representation of the object
print(PageCorpus.to_json())

# convert the object into a dict
page_corpus_dict = page_corpus_instance.to_dict()
# create an instance of PageCorpus from a dict
page_corpus_from_dict = PageCorpus.from_dict(page_corpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


