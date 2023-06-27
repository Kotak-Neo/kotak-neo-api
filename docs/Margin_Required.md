# **Margin_Required**
Get required margin details

```python
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "", quantity = "", instrument_token = "",
                       transaction_type = "")
```

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")
except Exception as e:
    print("Exception when calling margin_required->margin_required: %s\n" % e)
```

### Parameters

| Name               | Description                                                                                                              | Type           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|----------------|
| *exchange_segment* | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>bcs_fo - BCD                        | Str            |
| *price*            |                                                                                                                          | Str            |
| *product*          | NRML - Normal<br/>CNC - Cash and Carry<br/>MIS - MIS<br/>INTRADAY - INTRADAY<br/>CO - Cover Order<br/>BO - Bracket Order | Str            |
| *order_type*       | L - Limit<br/>MKT - Market<br/>SL - Stop loss limit<br/>SL-M - Stop loss market                                          | Str            |
| *quantity*         |                                                                                                                          | Str            |
| *instrument_token* | pSymbol in ScripMaster                                                                                                   | Str            |
| *transaction_type* | B(Buy), S(sell)                                                                                                          | Str            |
| *trading_symbol*   |                                                                                                                          | Str            |
| *transaction_type* | B(Buy), S(sell)                                                                                                          | Str            |
| *trigger_price*    |                                                                                                                          | Str [Optional] |


### Return type

**object**

### Sample response

```json
{
    "data": 
                {
                    "avlCash": "104.96", 
                    "insufFund": "12520.04", 
                    "stat": "Ok", 
                    "totMrgnUsd": "12625.00", 
                    "mrgnUsd": "0.00", 
                    "reqdMrgn": "12625.00", 
                    "avlMrgn": "104.96", 
                    "stCode": 200, 
                    "tid": "server2_2330220", 
                    "ordMrgn": "12625.00", 
                    "rmsVldtd": 78
                }
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                           | Response headers |
|-------------|-------------------------------------------------------|------------------|
| *200*       | Gets the margin_required data for a client account    | -                |
| *400*       | Invalid or missing input parameters                   | -                |
| *403*       | Invalid session, please re-login to continue          | -                |
| *429*       | Too many requests to the API                          | -                |
| *500*       | Unexpected error                                      | -                |
| *502*       | Not able to communicate with OMS                      | -                |
| *503*       | Trade API service is unavailable                      | -                |
| *504*       | Gateway timeout, trade API is unreachable             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
