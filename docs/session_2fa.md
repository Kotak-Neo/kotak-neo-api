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

| Name           | Description                                                        | Type   |
|----------------|--------------------------------------------------------------------|--------|
| *mobilenumber* | Your registered mobile number Eg: "+919999996708"                  | Str    |
| *pan*          | Your PAN number Eg: “DUMMY1234A”                                   | Str    |
| *password*     | Your trading password                                              | Str    |
| *otp*          | The 4-digit code you receive on registered mobile number           | Str    | 

Note: You can pass your 6 digit mpin instead of otp as well to complete the 2fa login. For example, `client.session_2fa("123456")`

### Return type

object

### Sample response

```json
{
  "data": {"token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2ODc1NDUwMDAsImp0aSI6ImFlOTYyMGMyLWIyZWItNDM2Zi04NWViLTU3NDhlYzBhNzY5NyIsImlhdCI6MTY4NzUxNDIyOCwiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6ImZmZmMyMDgyLTdiMTktNGFkOC1iY2Q5LTdiNWM0NWZhMzZhZiIsInVjYyI6IllSSUowIiwibmFwIjoiSExQUEs4OTM2TCIsImZldGNoY2FjaGluZ3J1bGUiOjAsImNhdGVnb3Jpc2F0aW9uIjoiIn0.Epq8jKxbXVQTvcSlW7GIVSmtAvWr_Zt0riRKN8zUh2Wvn6XGkiQRY5Ts1hIbcnJ0s2Jclh6Ig4C6UFz_P_Ar4dhcQf-x4EV8FtuKz1-HAnjwXZ_OTHn4Xrlq7tcpouGT9dbi4nt38UYcab9iMnEiMgtqQxbz042ub1WqrZEWABiZ2kOBBaksHmgEKsTe2iqNwa4fN-DoItqFhOu6DkcPz90lb1JmAbovwpu7TqOK30bHcjIJjDKQKBlHuw9_4ZbuAb4wSdQQwXxYYyXOZGM_HLIjinwnYJpxRpeG5eQigNkXO-VcyC9dA3u0MI5S5wtzyYQ_jEACiJew7ayM6l2KtQ",
  "sid": "a34f0165-8cac-4f84-a4ea-234adb713214",
  "rid": "0ae50f5d-ae07-4114-bdda-a27de1785573",
  "hsServerId": "server3",
  "isUserPwdExpired": "False",
  "caches": {
	  "baskets": "1687334141",
   "lastUpdatedTS": "1687353420",
   "multiplewatchlists": "1683352919",
   "techchartpreferences": "1683528608"},
  "ucc": "YRIJ0",
  "greetingName": "SHASHWAT",
  "isTrialAccount": "False",
  "dataCenter": "gdc",
  "searchAPIKey": ""}
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
