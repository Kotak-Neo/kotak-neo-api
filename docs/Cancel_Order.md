# **cancel_order**
> object cancel_order(order_id)

Cancel an order

# Method 1
client.cancel_order(order_id = "")

# Method 2 (Delayed)
This is delay type, if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further

client.cancel_order(order_id = "", isVerify="True")

### Example


```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Cancel an order
    client.cancel_order(order_id = "")
except Exception as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters
| Name        | Type  | Description         |
|-------------|-------|---------------------|
| *order_id*  | str   | Order ID to cancel. |

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
