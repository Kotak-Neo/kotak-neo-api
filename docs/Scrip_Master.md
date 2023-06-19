# **Scrip Master**
> object scrip_master()
> 
# Get Scrip Master CSV file

### Example

```python

from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    client.scrip_master("")
except Exception as e:
    print("Exception when calling Scrip Master Api->scrip_master: %s\n" % e)
```

### Return type

**object**

### HTTP request headers

 - **Accept**: application/json


### HTTP response details
| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | Ok                                           | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |



