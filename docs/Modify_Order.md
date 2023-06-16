# **modify_order**
> object modify_order(order_id, price , quantity , disclosed_quantity, trigger_price)

Modify an existing order

# **Method 1 Quick method** 
client.modify_order(instrument_token = "", exchange_segment = "", product = "", price = "", order_type = "", quantity= "", validity = "", trading_symbol = "", transaction_type = "", order_id = "")

# **Method 2 Delayed method**
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "")

### Example


```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Modify an existing order
    client.modify_order(instrument_token = "", exchange_segment = "", product = "", price = "", 
                        order_type = "", quantity= "", validity = "", trading_symbol = "",transaction_type = "", order_id = "")
except Exception as e:
    print("Exception when calling OrderApi->modify_order: %s\n" % e)

```

### Parameters

|Name | Type    | Description                                                                                                           | Notes
**instrument_token ** | **str** | pSymbol in ScripMaster (first Column)                                                                                 | 
**market_protection** | **str** | String - (Default Value - 0)                                                                                          | [optional]
**product** | **str** | Product types - NRML - Normal, CNC - Cash and Carry, MIS - MIS, INTRADAY - INTRADAY, CO - Cover Order, BO - Bracket Order |
**dd** | **str** | Default Value - “NA”                                  | [optional]
**disclosed_quantity** | **str** | (Default Value - 0)                                 | [optional]
**filled_quantity** | **str** | (Default Value - 0)         | [optional]
**validity** | **str** | Validity of the order - DAY, IOC  
**trading_symbol** | **str** | 
*transaction_type** | **str** | B(Buy), S(sell)
**trigger_price** | **str** | (Default Value - 0) | [optional]
**quantity** | **str** |                                                     |
**order_id** | **str** |     | 
**exchange_segment** | **str** | nse_cm NSE bse_cm BSE nse_fo NFO bse_fo BFO cde_fo CDS bcs_fo BCD    | 
**order_type** | **str** | L - Limit, MKT Market, SL Stop loss limit, SL-M Stop loss market
 



### Return type

**object**

### Sample response

```python
{
  {
    "stat": "Ok",
    "nOrdNo": "220621000000097",
    "stCode": 200
  }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
**200** | Order modified successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
