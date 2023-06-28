# **Socket**
Get live feed details of the given tokens
```python
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False) 
```

Un_Subscribe method first checks weather the token is already subscribed.<br/>
If not Subscribed you will see an error message else the given tokens will be unsubscribed.
```python
client.un_subscribe(instrument_tokens, isIndex=False, isDepth=False):
```

### Example

```python
from neo_api_client import NeoAPI

def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)
    
def on_open(message):
    print('[OnOpen]: ', message)
    
def on_close(message):
    print('[OnClose]: ', message)

client = NeoAPI(consumer_key="", consumer_secret="", environment='uat', on_message=on_message, on_error=on_error, on_open=on_open, on_close=on_close)
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
               {"instrument_token": "1594", "exchange_segment": "nse_cm"},
               {"instrument_token": "11915", "exchange_segment": "nse_cm"},
               {"instrument_token": "13245", "exchange_segment": "nse_cm"}]

try:
    # Get live feed data
    client.subscribe(instrument_tokens=inst_tokens)
except Exception as e:
    print("Exception while connection to socket->socket: %s\n" % e)

```
### Parameters

| Name                | Description                                                                         | Type                   |
|---------------------|-------------------------------------------------------------------------------------|------------------------|
| *instrument_tokens* | List of instrument Token (wToken) to be passed                                       | Str                    |
| *exchange_segment*  | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>bcs_fo - BCD<br/>Index -  INDEX | Str                    |
| *isDepth*           | Boolean value                                                                       | True/False [optional]  |
| *isIndex*           | Boolean value                                                                       | True/False [optional]  |


### Return type

**object**

### Sample response

```python
{  
    #Gets live data 
}

```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | ok                                           | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
