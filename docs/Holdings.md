# **Holdings**
Current holdings in the portfolio

```python
client.holdings("")
```

### Example

```python

from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    client.holdings("")
except Exception as e:
    print("Exception when calling Holdings->holdings: %s\n" % e)
```

### Return type

**object**

### Sample response
```json
{
      "data": [
                    {
                      "symbol": "YESBANK",
                      "displaySymbol": "YESBANK",
                      "averagePrice": 21.1225,
                      "quantity": 4,
                      "exchangeSegment": "nse_cm",
                      "exchangeIdentifier": "11915",
                      "holdingCost": 84.49,
                      "mktValue": 79,
                      "scripId": "dade08eae3d978dcb31940b6da2cfbab4ab395d3",
                      "instrumentToken": 7169,
                      "instrumentType": "Equity",
                      "isAlternateScrip": "false",
                      "closingPrice": 19.75
                    },
                    {
                      "symbol": "YESBANK",
                      "displaySymbol": "YESBANK",
                      "averagePrice": 21.1225,
                      "quantity": 4,
                      "exchangeSegment": "bse_cm",
                      "exchangeIdentifier": "532648",
                      "holdingCost": 84.49,
                      "mktValue": 79,
                      "scripId": "40297c23c30022e35db0e59e7ca3a30c7a5c6906",
                      "instrumentToken": 7168,
                      "instrumentType": "Equity",
                      "isAlternateScrip": "true",
                      "closingPrice": 19.75
                    },
                    {
                      "symbol": "CESC",
                      "displaySymbol": "CESC",
                      "averagePrice": 80.01,
                      "quantity": 2,
                      "exchangeSegment": "nse_cm",
                      "exchangeIdentifier": "628",
                      "holdingCost": 160.02,
                      "mktValue": 147.6,
                      "scripId": "fb94935fb38a1dd7f87c52e562d6756636fcb7f3",
                      "instrumentToken": 955,
                      "instrumentType": "Equity",
                      "isAlternateScrip": "false",
                      "closingPrice": 73.8
                    },
                    {
                      "symbol": "CESC",
                      "displaySymbol": "CESC",
                      "averagePrice": 80.01,
                      "quantity": 2,
                      "exchangeSegment": "bse_cm",
                      "exchangeIdentifier": "500084",
                      "holdingCost": 160.02,
                      "mktValue": 147.6,
                      "scripId": "22995f58a180b89e279e9d74df05545bc7fd02c9",
                      "instrumentToken": 954,
                      "instrumentType": "Equity",
                      "isAlternateScrip": "true",
                      "closingPrice": 73.8
                    }
                ]
}           

```

### HTTP request headers

 - **Accept**: application/json


### HTTP response details
| Status Code | Description                                           | Response headers |
|-------------|-------------------------------------------------------|------------------|
| *200*       | Gets the Portfolio holdings data for a client account | -                |
| *400*       | Invalid or missing input parameters                   | -                |
| *403*       | Invalid session, please re-login to continue          | -                |
| *429*       | Too many requests to the API                          | -                |
| *500*       | Unexpected error                                      | -                |
| *502*       | Not able to communicate with OMS                      | -                |
| *503*       | Trade API service is unavailable                      | -                |
| *504*       | Gateway timeout, trade API is unreachable             | -                |
