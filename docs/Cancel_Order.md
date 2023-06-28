# **Cancel_Order**
Cancel an order

## Method 1 - Quick Method
```python
client.cancel_order(order_id = "")
```

## Method 2 - Delayed Method
This method checks the order status first and then cancels the order if it is open.<br/>
```python
client.cancel_order(order_id = "", isVerify=True)
```

### Example


```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment=" ")
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Cancel an order
    client.cancel_order(order_id = "")
except Exception as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters
| Name        | Description         | Type      |
|-------------|---------------------|-----------|
| *order_id*  | Order ID to cancel | str       | 
| *isVerify*  | Flag to check the status of order (Delayed method) | boolean   |
| *amo*       | After market order - YES, NO (optional, Default Value - NO) | str   |

### Return type

**object**

### Sample response

```json
{
    "stat": "Ok",
    "nOrdNo": "230120000017243",
    "stCode": 200
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | Order canceled successfully                  | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
