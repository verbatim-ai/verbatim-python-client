# Crawler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of your Crawler | 
**description** | **str** | Description of your Crawler | [optional] 
**url** | **str** | Root url of the domain the crawl. Must start with http// or https:// | 
**max_crawl_depth** | **int** | Maximum crawl depth | [optional] 
**enabled** | **bool** | Activation state of the crawler. True, the crawler is enable and have recurrent crawl schedule. False, the crawler is disable, no crawl until is back to an enable state. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**id** | **str** | ID of the crawler. Primary key use to index this crawler | [optional] 
**corpus_id** | **str** | ID of the corpus where the crawler is attached | [optional] 
**next_crawl** | **datetime** |  | [optional] 
**last_crawl** | **datetime** |  | [optional] 
**nb_doc** | **int** | Number of document crawler by the crawler. Merged into your quota | [optional] 
**size** | **int** | Storage size use by the crawler.  Merged into your quota | [optional] 

## Example

```python
from verbatim_client.models.crawler import Crawler

# TODO update the JSON string below
json = "{}"
# create an instance of Crawler from a JSON string
crawler_instance = Crawler.from_json(json)
# print the JSON string representation of the object
print(Crawler.to_json())

# convert the object into a dict
crawler_dict = crawler_instance.to_dict()
# create an instance of Crawler from a dict
crawler_from_dict = Crawler.from_dict(crawler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


