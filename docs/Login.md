# **login**
> object login(password=""", mobilenumber=None, userid=None, pan=None)

Login using Userid

Authenticate userid and password to generate one time token.

### Example


```python
from neo_api_client import NeoAPI
client = NeoAPI(consumer_key="",consumer_secret="",environment='uat')
try:
    # Login using password
    client.login(mobilenumber="", password="")
except Exception as e:
    print("Exception when calling SessionApi->login: %s\n" % e)
```
### Parameters

| Name           | Description                                                        | Type   |
|----------------|--------------------------------------------------------------------|--------|
| *mobilenumber* | Eg: "+919999999908"                                                | Str    |
| *userid*       | Eg: “asfdywgsiqwjnskm”                                             | Str    |
| *pan*          | Eg: “AVRFT7865T”                                                   | Str    |
| *End points*   | https://gw-napi.kotaksecurities.com/login/1.0/login/v2/validate    | Live   |
| *End points*   | https://nsbxapi-gw.kotaksecurities.com/api/1.0/login/v2/validate   | UAT    |

### Return type

object

### Sample response
```python
{
  "data": {
    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJWaWV3Il0sImV4cCI6MTY1NTgwNjMyOCwianRpIjoiNjFjMmE4MTUtMzQ0ZS00YWMwLThiZmEtZTVjYmFiNzAyNmEzIiwiaWF0IjoxNjU1ODAyNzI4LCJpc3MiOiJsb2dpbi1zZXJ2aWNlIiwic3ViIjoiVEVTVFlBMjQiLCJmZXRjaGNhY2hpbmdydWxlIjowLCJjYXRlZ29yaXNhdGlvbiI6IiJ9.bgui3u2Rw75RfIgCVH2dBV7YJ6xq0Y-BKiZ2ukzZF1NlDFsVQ1EYqK6Mpn8juwN6pLHHBaMQh4RiGtufcu5IxDQtzka-kSyL_7KAYMatKZECCxerETsjNCdNw6u0CIvt9X9T1RNztrBpkKDxwmxlw6RKJireISX9698z4fLykziO9lEpbd0aGJRfvZ4c3e9-gQ4i1TKg_WEXDwKU9oVcTSHJqQGjL7b5l90kbDUvfDtt3MPfoyNhetDsR-8GC5-N9uPViLGwtJXNJLh_HBL0jHC-yNgxYLSqJddqrsI-lv2nurwmu_pOGqh14pO1ohP4rw9CfJnFvFvRwH--vUiH2w",
    "sid": "ebd3c21a-5174-4db1-9454-d9afd94d7340",
    "rid": "23835a76-9b50-4842-a343-0dbabeb20a8f",
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