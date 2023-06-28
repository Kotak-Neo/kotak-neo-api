# **Login**
This is the first step of 2FA login. Authenticate your mobile number(or PAN) and password to generate a view token.

```python
client.login(mobilenumber="", password = "")
```

### Example


```python
from neo_api_client import NeoAPI

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment="uat")

try:
    # Login using password
    client.login(mobilenumber=" ", password=" ")
    
except Exception as e:
    print("Exception when calling SessionApi->login: %s\n" % e)
```
### Parameters

| Name           | Description                                                        | Type   |
|----------------|--------------------------------------------------------------------|--------|
| *mobilenumber* | Your registered mobile number Eg: "+919999996708"                  | Str    |
| *pan*          | Your PAN number Eg: “DUMMY1234A”                                   | Str    |
| *password*     | Your trading password                                              | Str    |

### Return type

object

### Sample response
```json
{
        "data": {
        "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJWaWV3Il0sImV4cCI6MTY4Nzk3NzAwMCwianRpIjoiYzgyMzY2NjAtODkyNy00NzQ0LTk5YmQtMTAyNmRkYTA3MzUzIiwiaWF0IjoxNjg3OTQ2NDQyLCJpc3MiOiJsb2dpbi1zZXJ2aWNlIiwic3ViIjoiYTRlOGE5YzAtZmYyZi0xMWViLTlhMDMtMDI0MmFjMTMwMDAzIiwidWNjIjoiRDIwMTQiLCJuYXAiOiJEVU1NWTExMDVBIiwiZmV0Y2hjYWNoaW5ncnVsZSI6MCwiY2F0ZWdvcmlzYXRpb24iOiIifQ.PRDxhHjdAD2Z_hl3BF_-72l2uds5TzlAEyk57v9BgSnlUZrZ6S9khLi4l8Nfz1zNvwYHqwMPe4Gto6sXnbzbwim-U5c5dDey1hklLTD3kAb6y3bqSR-JcpdvpSGQQ6JVkxckKs_4qDgKEY-0qwnF6jtpB2D_CV0LCKMXfYWNBadZW9-cLLZkIc_C8n6DksyLQF2BWXbTUl6fEb9zSW7GYqI40YLB0q-FZgrOR7dfb3mNtJ4R4oQbeKf0GmR726JWcd3iOqVfFIzHUJvAeVu8FrjWEJfkxjPWf71BU5d_YAUYgtHvRxCweetuZqwa2HNN9xHTsNqr6FJdo3W4lhMp1g",
        "sid": "8f8cd1ab-46e6-41cc-9bdd-9412c5fd4fb7",
        "rid": "69404582-871b-4de8-8fdd-e3e6a5e15bbf",
        "hsServerId": "server2",
        "isUserPwdExpired": false,
        "caches": {
        "baskets": "1687845385",
        "lastUpdatedTS": "1687845385",
        "multiplewatchlists": "1683352919",
        "techchartpreferences": "1683528608"
        },
        "ucc": "ABCD0",
        "greetingName": "DUMMY",
        "isTrialAccount": false,
        "dataCenter": "gdc",
        "searchAPIKey": ""
        }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | User session validated successfully       |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
