# **Quotes**
Get quotes details - `quote_type` can be `market_depth`, `ohlc`, `ltp`, `52w`, `circuit_limits`, `scrip_details` <br/>

By default, `quote_type` is set as `None`, which means you will get the complete data.<br/>

Quotes API can be accessed without completing login by passing `session_token`, `sid`, and `server_id`.

```python
client.quotes(instrument_tokens = instrument_tokens, quote_type="", isIndex=False, session_token="", sid="", server_id="")
```

### Example

```python
from neo_api_client import NeoAPI

def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)

client = NeoAPI(consumer_key="", consumer_secret="", environment="prod", on_message=on_message, on_error=on_error)
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
               {"instrument_token": "1594", "exchange_segment": "nse_cm"},
               {"instrument_token": "11915", "exchange_segment": "nse_cm"},
               {"instrument_token": "13245", "exchange_segment": "nse_cm"}]

try:
    # get LTP and Market Depth Data
    client.quotes(instrument_tokens=inst_tokens, quote_type="", isIndex=False)
    
   # OR Quotes API can be accessed without completing login by passing session_token, sid, and server_id
    client.quotes(instrument_tokens = inst_tokens, quote_type="", isIndex=False, session_token="", sid="",server_id="")
except Exception as e:
    print("Exception when calling get Quote api->quotes: %s\n" % e)

```
### Parameters

| Name                | Description                                                                                         | Type                   |
|---------------------|-----------------------------------------------------------------------------------------------------|------------------------|
| *instrument_tokens* | wToken or instrument Token                                                                          | Str                    |
| *exchange_segment*  | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>mcx_fo - MCX   | Str [optional]         |
| *quote_type*        | ltp - Last Trading Price<br/>market_depth - Market Depth<br/>ohlc - Open, High, Low, Close<br/>52w - 52 week high and low<br/>circuit_limits - Crcuit limits of the day<br/>scrip_details - All Details                                 | Str [optional]         |
| *isIndex*           | Pass `True` for Indexes                                                                                       | Boolean value [optional]  |


### Return type

**object**

### Sample response

```json
{
  "message": [
    {
      "last_traded_time": "28/06/2023 15:59:47",
      "volume": "63502734",
      "last_traded_price": "16.20",
      "last_traded_quantity": "3",
      "total_buy_quantity": "622552",
      "total_sell_quantity": "0",
      "buy_price": "16.20",
      "sell_price": "0.00",
      "buy_quantity": "622552",
      "average_price": "16.14",
      "lower_circuit_limit": "13.00",
      "upper_circuit_limit": "19.40",
      "52week_high": "24.75",
      "52week_low": "12.55",
      "open_interest": "2147483648",
      "multiplier": "1",
      "precision": "2",
      "change": "0.15",
      "net_change_percentage": "0.93",
      "total_traded_value": "1024934126.76",
      "instrument_token": "11915",
      "exchange_segment": "nse_cm",
      "trading_symbol": "YESBANK-EQ",
      "ohlc": {
        "open": "16.10",
        "high": "16.35",
        "low": "15.95",
        "close": "16.05"
      }}]
}


```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | ok                                           |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *500*       | Unexpected error                             |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
