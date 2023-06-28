# **Modify_Order**
Modify an existing order

## **Method 1 - Quick method**
```python
client.modify_order(instrument_token = "", exchange_segment = "", product = "", price = "", order_type = "", quantity= "",
                    validity = "", trading_symbol = "", transaction_type = "", order_id = "")
````

## **Method 2 - Delayed method**
This method verifies the order status first and then modifies the order if it is open.
```python
client.modify_order(order_id = "", price = "", quantity = "", trigger_price = "", validity = "", order_type = "", amo = "")
````

### Example


```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment=" ")
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Modify an existing order
    client.modify_order(instrument_token = "", exchange_segment = "", product = "", price = "", 
                        order_type = "", quantity= "", validity = "", trading_symbol = "",transaction_type = "", order_id = "", amo = "")
except Exception as e:
    print("Exception when calling OrderApi->modify_order: %s\n" % e)

```
### Parameters

| Name                 | Description                                                                                                              | Type           |
|----------------------|--------------------------------------------------------------------------------------------------------------------------|----------------|
| *instrument_token*   | pSymbol in ScripMaster file (first Column)                                                                               | Str [optional] |
| *market_protection*  | String - (Default Value - 0)                                                                                             | Str [optional] |
| *product*            | NRML - Normal<br/>CNC - Cash and Carry<br/>MIS - MIS<br/>INTRADAY - INTRADAY<br/>CO - Cover Order  | Str            |
| *dd*                 | Default Value - “NA”                                                                                                     | Str [optional] |
| *filled_quantity*    | (Default Value - 0)                                                                                                      | Str [optional] |
| *validity*           | Validity of the order - DAY, IOC                                                                                         | Str [optional] |
| *trading_symbol*     | pTrdSymbol in ScripMaster file                                                                                          | Str            |
| *transaction_type*   | B(Buy), S(sell)                                                                                                          | Str            |
| *order_type*         | L - Limit<br/>MKT - Market<br/>SL - Stop loss limit<br/>SL-M - Stop loss market                                          | Str            |
| *trigger_price*      | Optional, required for stop loss and cover order                                                          | Str [optional] |
| *quantity*           | quantity of the order                                                                                        | Str            |
| *order_id*           | order id of the order you want to modify                                                                                       | Str            |
| *exchange_segment*   | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS<br/>mcx_fo - MCX                        | Str [optional] |

### Return type

**object**

### Sample response

```json
{
    "stat": "Ok",
    "nOrdNo": "220621000000097",
    "stCode": 200
}

```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Order modified successfully                  |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
