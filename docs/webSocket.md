# **webSocket**
Get live feed details of the given tokens
```python
inst_tokens = [{"instrument_token": "", "exchange_segment": ""}]

client.subscribe(instrument_tokens = inst_tokens, isIndex=False, isDepth=False) 
```

Un_Subscribe method first checks whether the token is already subscribed.<br/>
If not Subscribed you will see an error message else; the given tokens will be unsubscribed.
```python
client.un_subscribe(instrument_tokens, isIndex=False, isDepth=False)
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

client = NeoAPI(consumer_key="", consumer_secret="", environment="prod", access_token=None, neo_fin_key=None)
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

# Setup Callbacks for websocket events (Optional)
client.on_message = on_message  # called when message is received from websocket
client.on_error = on_error  # called when any error or exception occurs in code or websocket
client.on_close = on_close  # called when websocket connection is closed
client.on_open = on_open  # called when websocket successfully connects

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
| *instrument_tokens* | List of instrument Token (wToken) to be passed                                       | list                    |
| *exchange_segment*  | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>mcx_fo - MCX<br/>Index -  INDEX | Str                    |
| *isDepth*           | Pass True if want to subscribe Market Depth                                                                       | Boolean value [optional]  |
| *isIndex*           | Pass True if want to subscribe Index                                                                       | Boolean value [optional]  |

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

```python
{  
    #Gets live data 
}

```
### Response Parameters

#### For Index

| Name                | Description                                                                         |
|---------------------|-------------------------------------------------------------------------------------|
| *ftm0* | Ignore this value                                                
| *dtm1*  | Ignore this value
| *iv*           | Last Traded Price
| *ic*           | Previous Day Close
| *tvalue*           | Index exchange feed time
| *highPrice*           | High Price
| *lowPrice*           | Low Price
| *openingPrice*           | Open Price
| *mul*           | Multiplier
| *prec*           | Precision
| *cng*           | Change
| *nc*           | Net Change in Percentage
| *name*           | if - Index <br/> sf - Stock <br/> dp - Depth
| *tk*           | Intrument Token
| *e*           | Exchange Segment

#### For Stocks and Derivatives

| Name                | Description                                                                         |
|---------------------|-------------------------------------------------------------------------------------|
| *ftm0* | Ignore this value                                                
| *dtm1*  | Ignore this value
| *ftdm*  | Exchange Feeder Time
| *ltt*  | Last Traded Time
| *v*  | Volume
| *ltp*           | Last Traded Price
| *ltq*           | Last Traded Quantity
| *tbq*           | Total Buy Quantity
| *tsq*           | Total Sell Quantity
| *bp*           | Bid Price 1
| *sp*           | Offer Price 1
| *bq*           | Bid Size 1
| *bs*           | Offer Size 1
| *ap*           | Average Price
| *lo*           | Low Price
| *h*           | High Price
| *lcl*           | Lower Circuit Limit
| *ucl*           | Upper Circuit Limit
| *yh*           | 52 Week High
| *yl*           | 52 Week Low
| *op*           | Open Price
| *c*           | Closing Price
| *mul* | Multiplier
| *prec* | Precision
| *cng* | Change
| *nc* | Net Change in Percentage
| *to* | Turn Over
| *name*           | if - Index <br/> sf - Stock <br/> dp - Depth
| *tk* | Instrument Token
| *e* | Exchange Segment
| *ts* | Trading Symbol
| *oi* | Open Interest

#### For Depth

| Name                | Description                                                                         |
|---------------------|-------------------------------------------------------------------------------------|
| *ftm0* | Ignore this value                                                
| *dtm1*  | Ignore this value
| *bp, bp1,2,3,4* | Bid Price
| *sp, sp1,2,3,4* | Offfer Price
| *bq, bq1,2,3,4* | Bid Size
| *bs, bs1,2,3,4* | Offer Size
| *bno1,2,3,4,5* | Bid Orders
| *sno1,2,3,4,5* | Offer Orders
| *mul* | Multiplier
| *prec* | Precision
| *name*           | if - Index <br/> sf - Stock <br/> dp - Depth
| *tk* | Instrument Token
| *e* | Exchange Segment
| *ts* | Trading Symbol




### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  | 
|-------------|----------------------------------------------|
| *200*       | ok                                           |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
