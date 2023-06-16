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


| Name                 | Description                                                                                                    | Type           |
|----------------------|----------------------------------------------------------------------------------------------------------------|----------------|
| *amo*                | YES/NO - (Default Value - NO)                                                                                  | Str [optional] |
| *disclosed_quantity* | (Default Value - 0)                                                                                            | Str [optional] |
| *exchange_segment*   | nse_cm NSE bse_cm BSE nse_fo NFO bse_fo BFO cde_fo CDS bcs_fo BCD                                              | Str            |
| *market_protection*  | (Default Value - 0)                                                                                            | Str [optional] |
| *product *           | NRML - Normal, CNC - Cash and Carry, MIS - MIS, INTRADAY - INTRADAY, <br/>CO - Cover Order, BO - Bracket Order | Str [optional] |
| *pf*                 | Default Value - “N”                                                                                            | Str [optional] |
| *price *             |                                                                                                                | Str [optional] |
| *order_typ*          | L - Limit, MKT Market, SL Stop loss limit, SL-M Stop loss market                                               | Str            |
| *quantity *          |                                                                                                                | Str            |
| *validity*           | Validity of the order - DAY, IOC                                                                               | Str            |
| *trigger_price*      |                                                                                                                | Str            |
| *trading_symmbol*    |                                                                                                                | Str            |
| *transaction_type*   | B(Buy), S(Sell)                                                                                                | Str            |
| *tag*                | Tag for this order                                                                                             | Str [optional] |


### Return type

**object**

### Sample response

```python
{
    'stat': 'Ok',
    'nOrdNo': '230120000017243',
    'stCode': 200
}

```
### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details


| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | Order placed successfully                    | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)




