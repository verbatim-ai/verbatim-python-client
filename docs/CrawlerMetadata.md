# CrawlerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of your Crawler | 
**description** | **str** | Description of your Crawler | [optional] 
**url** | **str** | Root url of the domain the crawl. Must start with http// or https:// | 
**max_crawl_depth** | **int** | Maximum crawl depth | [optional] 
**enabled** | **bool** | Activation state of the crawler. True, the crawler is enable and have recurrent crawl schedule. False, the crawler is disable, no crawl until is back to an enable state. | [optional] 

## Example

```python
from verbatim_client.models.crawler_metadata import CrawlerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerMetadata from a JSON string
crawler_metadata_instance = CrawlerMetadata.from_json(json)
# print the JSON string representation of the object
print(CrawlerMetadata.to_json())

# convert the object into a dict
crawler_metadata_dict = crawler_metadata_instance.to_dict()
# create an instance of CrawlerMetadata from a dict
crawler_metadata_from_dict = CrawlerMetadata.from_dict(crawler_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


