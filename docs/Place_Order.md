# neo_api_client.OrderApi

All URIs are relative to "host" parameter

|Method | Description | Response Normal Order | Response SOR Order | Response MTF Order |
[**place_order**](docs/Place_Order.md#place_order) | Place a New order | 
[**modify_order**](docs/Modify_Order.md#modify_order) | Modify an existing order |
[**cancel_order**](docs/cancel_Order.md#cancel_order) | Cancel an order |

# **place_new_order**
> object place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",trigger_price="0", tag=None)

Place a New order

### Example


```python
from neo_api_client import NeoAPI
        
#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Place a Order
    client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                       transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                       trigger_price="0", tag=None)
except Exception as e:
    print("Exception when calling OrderApi->place_order: %s\n" % e)
``` 

### Parameters

|Name                   | Type    | Description                                                                                                              | Notes      

 **amo**               | **str** | YES/NO - (Default Value - NO)              | [optional] 
 **disclosed_quantity** | **str** | (Default Value - 0)                  | [optional] 
 **exchange_segment**  | **str** | nse_cm NSE bse_cm BSE nse_fo NFO bse_fo BFO cde_fo CDS bcs_fo BCD
 **market_protection** | **str** | (Default Value - 0)           | [optional] 
 **product**           | **str** | Product types - NRML - Normal, CNC - Cash and Carry, MIS - MIS, INTRADAY - INTRADAY, CO - Cover Order, BO - Bracket Order | [optional] 
 **pf**                | **str** | Default Value - “N”                 | [optional]
 **price**             | **str** |                            | [optional] 
 **order_type**        | **str** | L - Limit, MKT Market, SL Stop loss limit, SL-M Stop loss market
 **quantity**          | **str** |  
 **validity**          | **str** | Validity of the order - DAY, IOC 
 **trigger_price**     | **str** | 
 **trading_symmbol**   | **str** |
 **transaction_type**  | **str** |  B(Buy), S(Sell)
 **tag**               | **str**   | Tag for this order | [optional]

### Return type

**object**

### Sample response

```python
{
  "Success": {
                'stat': 'Ok',
                'nOrdNo': '230120000017243',
                'stCode': 200
                }
  }
```
### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |

**200** | Order placed successfully |  -  |
**400** | Invalid or missing input parameters |  -  |
**403** | Invalid session, please re-login to continue |  -  |
**429** | Too many requests to the API |  -  |
**500** | Unexpected error |  -  |
**502** | Not able to communicate with OMS |  -  |
**503** | Trade API service is unavailable |  -  |
**504** | Gateway timeout, trade API is unreachable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)




