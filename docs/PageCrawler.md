# PageCrawler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Crawler]**](Crawler.md) |  | [optional] 
**next_page_token** | **object** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from verbatim_client.models.page_crawler import PageCrawler

# TODO update the JSON string below
json = "{}"
# create an instance of PageCrawler from a JSON string
page_crawler_instance = PageCrawler.from_json(json)
# print the JSON string representation of the object
print(PageCrawler.to_json())

# convert the object into a dict
page_crawler_dict = page_crawler_instance.to_dict()
# create an instance of PageCrawler from a dict
page_crawler_from_dict = PageCrawler.from_dict(page_crawler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


