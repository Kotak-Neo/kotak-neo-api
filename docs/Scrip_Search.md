# **scrip_search**
> object search_scrip(exchange_segment = "nse_cm", symbol = "YESBANK",  expiry = "", option_type = "", strike_price = "")

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # get scrip search details for particular exchange segment
    client.search_scrip(exchange_segment = "nse_cm", symbol = "YESBANK",  expiry = "", option_type = "", strike_price = "")
except Exception as e:
    print("Exception when calling scrip search api->scrip_search: %s\n" % e)

```
### Parameters

| Name                | Description                     | Type           |
|---------------------|---------------------------------|----------------|
| *exchange_segment*  |                                 | Str            |
| *symbol*            |                                 | Str            |
| *expiry*            | User can search multiple expiry | Str [optional] |
| *option_type*       | User can search option_type     | Str [optional] |
| *strike_price*      | User can search strike_price    | Str [optional] |
| *ignore_50multiple* | Boolean value                   | True/False     |


### Return type

**object**

### Sample response

```python
{ 
    "instrument_token": "11915", 
    "trading_symbol": "YESBANK-EQ", 
    "exchange_segment": "nse_cm", 
    "series": "EQ", 
    "scrip_name": "YES BANK LTD", 
    "option_type": "", 
    "expiry_date": "", 
    "strick_price": "", 
    "tick_size": "", 
    "lot_size": "", 
    "exchange": "NSE", 
    "segment": "CASH", 
    "multiplier": "-1", 
    "precision": "2", 
    "instrument_type": "", 
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
