# **Session_Init**
Initiate trading session for a User

```python
client = NeoAPI(consumer_key="",consumer_secret="",environment="uat",on_message=None, on_error=None, on_close=None,
                on_open=None, neo_fin_key=None)
```

### Example

```python
from neo_api_client import NeoAPI

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)
    
#the session initializes when the following constructor is called
client = NeoAPI(consumer_key="",consumer_secret="",environment="uat",on_message=on_message, on_error=on_error)
```
### Parameters

| Name                        | Description                                      | Type           |
|-----------------------------|--------------------------------------------------|----------------|
| *consumer_key*              | Mandatory if not passing access token            | Str [optional] |
| *consumer_secret*           | Mandatory if not passing access token            | Str [optional] |
| *access_token*              | Mandatory if not passing consumer key and secret | Str [optional] |
| *environment*               | UAT/PROD, Default Value = "UAT"                  | Str [optional] |
| *neo_fin_key*               | Default Value = "neotradeapi"                    | Str [optional] |


### HTTP request headers

 - **Accept**: application/json

### HTTP response details

| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Ok                                           |
| *401*       | Invalid or missing input parameters          |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
