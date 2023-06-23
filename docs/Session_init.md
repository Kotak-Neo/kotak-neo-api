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
    
#the session initializes when the following constructor is called
client = NeoAPI(consumer_key="",consumer_secret="",environment='uat',on_message=on_message, on_error=on_error, neo_fin_key="neotradeapi")
```
### Parameters

| Name                        | Description                                | Type           |
|-----------------------------|--------------------------------------------|----------------|
| *consumer_key*              | Mandatory if not passing access token      | Str [optional] |
| *consumer_secret*           | Mandatory if not passing access token      | Str [optional] |
| *access_token*              | Mandatory if generate_new_access_token="N" | Str [optional] |
| *environment*               | UAT/PROD, Default Value = "UAT"            | Str [optional] |
| *generate_new_access_token* | Allowed Values - Y/N, Default Value - Y    | Str [optional] |
| *neo_fin_key*               | Default Value = "neotradeapi"              | Str [optional] |


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
