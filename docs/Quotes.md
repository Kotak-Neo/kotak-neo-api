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

client = NeoAPI(consumer_key="", consumer_secret="", environment="prod", access_token=None, neo_fin_key=None)
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

# Setup Callbacks for websocket events (Optional)
client.on_message = on_message  # called when message is received from websocket
client.on_error = on_error  # called when any error or exception occurs in code or websocket
client.on_close = None  # called when websocket connection is closed
client.on_open = None  # called when websocket successfully connects

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

### For Indexes
Exchange Identifier is not a number in case of Indexes. Below is the Index Names that should be used in place of instrument token. 
For Example - `inst_tokens = [{"instrument_token": "Nifty 50", "exchange_segment": "nse_cm"}]`

| Exchange Identifier   |
|--------|
| Nifty 50<br/> |
| Nifty Bank<br/> |
| Nifty Fin Service<br/> |
| SENSEX<br/> |
| INDIA VIX<br/> |
| NIFTY MIDCAP 100<br/> |
| Nifty 100<br/> |
| Nifty PSU Bank<br/> |
| Nifty Pharma<br/> |
| Nifty IT<br/> |
| Nifty PSE<br/> |
| Nifty FMCG<br/> |
| Nifty 500<br/> |
| Nifty Auto<br/> |
| Nifty CPSE<br/> |
| Nifty 200<br/> |
| Nifty Next 50<br/> |
| NIFTY MID SELECT <br/> |

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
