# **session_2fa**
> object session_2fa(OTP=""")
Generate final Session Token

Method to generate final session token for the user

### Example


```python
from neo_api_client import NeoAPI

client = NeoAPI(consumer_key="",consumer_secret="",environment='uat')
				
try:
    # Login using password
    client.login(mobilenumber="", password="")
    
    # Generate final Session Token
    client.session_2fa(OTP="")
	
except Exception as e:
    print("Exception when calling SessionApi->session_2fa: %s\n" % e)
```

### Parameters

### Parameters

| Name           | Description            | Type |
|----------------|------------------------|------|
| *mobilenumber* | Eg: "+919999999908"    | Str  |
| *userid*       | Eg: “asfdywgsiqwjnskm” | Str  |
| *pan*          | Eg: “AVRFT7865T”       | Str  |
| *password*     |                        |      |
| *otp*          |                        |      |

### Return type

object

### Sample response

```python
{
  "data": {
    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2NTU4MDY1MzksImp0aSI6ImU2YWVkMzUxLTI0MzAtNDNhNi04ZGFjLWM3Zjg3MGQwNzJhZiIsImlhdCI6MTY1NTgwMjkzOSwiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6IlRFU1RZQTI0IiwiZmV0Y2hjYWNoaW5ncnVsZSI6MCwiY2F0ZWdvcmlzYXRpb24iOiIifQ.Leq2OMYd-5ezEmG3czEMJxpgkrVmmXMBFJcbOUIeN5ZFFcWT2Ta-fZsyedEcEo4ge8-RP1d0xOMn_xydjw85zBu0zy8eQGmKxZA9kPutQ-tDOdAW_lUBYIbmidZvvZ2FFU5uspFV0fZBHsvaGqDJzEmB6w5n5Rf26IEnyGwQFBtSM1VcihOr13ZvurRFlrnA-x7_r5oi2wweEC7IrhLn6dMc0U8xtHkirYL9NCN_qd0Zcw8HVlM9d2_D_Zg7E-G2zmhlYEUPGHbPYPCQB0dPx4-qyL_TJvJHTqtja0tdpcApUtTiprQHLp5fCwWoa6O4s-SRqVOh3Z0fvIRga2vO1Q",
    "sid": "b3ebb6af-7205-43e9-8513-189472393cab",
    "rid": "a9fe0821-6849-4c68-a083-ddc92d61e060",
    "hsServerId": "server1",
    "caches": {
      "lastUpdatedTS": "1654684389",
      "multiplewatchlists": "1654684389",
      "watchlist": "1638271224"
    },
    "ucc": "TESTYA24",
    "greetingName": "string"
  }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               | Response headers |
|-------------|-------------------------------------------|------------------|
| *200*       | User session validated successfully       | -                |
| *400*       | Invalid or missing input parameters       | -                |
| *401*       | Verify resource and path of the request   | -                |
| *429*       | Too many requests to the API              | -                |
| *500*       | Unexpected error                          | -                |
| *502*       | Not able to communicate with OMS          | -                |
| *503*       | Trade API service is unavailable          | -                |
| *504*       | Gateway timeout, trade API is unreachable | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
