# **session_init**
> object NeoAPI(consumer_key="",consumer_secret="",environment='uat',on_message=None, on_error=None, on_close=None, on_open=None, neo_fin_key=None)

API to initiate trading session for a User.

### Example

```python
from neo_api_client import NeoAPI

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_open(message):
    print('[OnOpen]: ', message)
    
def on_close(message):
    print('[OnClose]: ', message)
    
#the session initializes when following constructor is called
client = NeoAPI(consumer_key="",consumer_secret="",environment='uat',on_message=None, on_error=None, on_close=None, on_open=None, neo_fin_key=None)
```
### Parameters

| Name                        | Description                                | Type           |
|-----------------------------|--------------------------------------------|----------------|
| *consumer_key*              |                                            | Str            |
| *consumer_secret*           |                                            | Str            |
| *access_token*              | Mandatory if generate_new_access_token="N" | Str [optional] |
| *environment*               | UAT/LIVE                                   | Str UAT        |
| *generate_new_access_token* | Y                                          | Str [optional] |


### HTTP request headers

 - **Accept**: application/json

### HTTP response details

| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | Order placed successfully                    | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)