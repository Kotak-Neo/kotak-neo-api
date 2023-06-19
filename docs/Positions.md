# **positions**
> object positions()

Get's positions.

### Example

```python

from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    client.positions("")
except Exception as e:
    print("Exception when calling PositionsApi->positions: %s\n" % e)
```

### Return type

**object**

### Sample response
```python
{
    "stat": "Ok",
    "stCode": 200,
    "data": [
              {
                "buyAmt": "2625.00",
                "cfSellAmt": "0.00",
                "prod": "NRML",
                "exSeg": "nse_fo",
                "sqrFlg": "Y",
                "actId": "PRS2206",
                "cfBuyQty": "0",
                "cfSellQty": "0",
                "tok": "53179",
                "flBuyQty": "25",
                "flSellQty": "25",
                "sellAmt": "2625.00",
                "posFlg": "true",
                "cfBuyAmt": "0.00",
                "stkPrc": "0.00",
                "trdSym": "BANKNIFTY21JULFUT",
                "sym": "BANKNIFTY",
                "expDt": "29 Jul, 2021",
                "type": "FUTIDX",
                "series": "XX",
                "brdLtQty": "25",
                "exp": "1627569000",
                "optTp": "XX",
                "genNum": "1",
                "genDen": "1",
                "prcNum": "1",
                "prcDen": "1",
                "lotSz": "25",
                "multiplier": "1",
                "precision": "2",
                "hsUpTm": "2021/07/13 18:34:44"        
              }
            ]
}

```

### HTTP request headers

 - **Accept**: application/json


### HTTP response details
| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | Gets the Positoin data for a client account  | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |
