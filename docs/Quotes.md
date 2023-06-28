# **Quotes**
Get quotes details - quote_type can be market_depth, ohlc, ltp, 52w, circuit_limits, scrip_details<br/>
By Default quote_type is set as None that means you will get the complete data.<br/>
Quotes api can be accessed without completing login by passing session_token, sid and server_id.

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

client = NeoAPI(consumer_key="", consumer_secret="", environment='uat', on_message=on_message, on_error=on_error)
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
               {"instrument_token": "1594", "exchange_segment": "nse_cm"},
               {"instrument_token": "11915", "exchange_segment": "nse_cm"},
               {"instrument_token": "13245", "exchange_segment": "nse_cm"}]

try:
    # get LTP and Market Depth Data
    client.quotes(instrument_tokens=inst_tokens, quote_type="market_depth", isIndex=False)
    
   # OR Quotes api can be accessed without completing login by passing session_token, sid and server_id
    client.quotes(instrument_tokens = inst_tokens, quote_type="", isIndex=False, session_token="", sid="",server_id="")
except Exception as e:
    print("Exception when calling get Quote api->quotes: %s\n" % e)

```
### Parameters

| Name                | Description                                                                                         | Type                   |
|---------------------|-----------------------------------------------------------------------------------------------------|------------------------|
| *instrument_tokens* | wToken or instrument Token                                                                          | Str                    |
| *exchange_segment*  | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>bcs_fo - BCD   | Str [optional]         |
| *quote_type*        | LTP<br/>depth<br/>OHLC<br/>52W<br/>circuit_limits<br/>scrip_details                                 | Str [optional]         |
| *isIndex*           | Boolean value                                                                                       | True/False [optional]  |


### Return type

**object**

### Sample response

```json
{  
    "instrument_token": "11915", 
                    "trading_symbol": "YESBANK-EQ", 
                    "exchange_segment": "nse_cm", 
                    "last_trade_time": "19/01/2023 12:34:46", 
                    "ltp": "20.15", 
                    "last_traded_quantity": "8", 
                    "total_buy_quantity": "0", 
                    "total_sell_quantity": "20", 
                    "volume": "79640780", 
                    "average_price": "20.15", 
                    "oi": "0", 
                    "change": "-0.20", 
                    "net_change_percentage": "-0.98", 
                    "lower_circuit_limit": "16.15", 
                    "upper_circuit_limit": "24.15", 
                    "52week_high": "24.75", 
                    "52week_low": "12.10", 
                    "ohlc":
                          { 
                            "open": "20.25", 
                            "high": "21.00", 
                            "low": "19.50", 
                            "close": "20.50", 
                          },
                            "depth": 
                                   { "buy": 
                                            [ 
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "",
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              }, 
                                            ],
                                            "sell": 
                                                [ 
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  }, 
                                                ] 
                                   } 
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
