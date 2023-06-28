# **Order_Report**

## Method 1
Get all traded order details
```python
client.trade_report()
```

## Method 2 
Get details of a particular order using order_id
```python
client.trade_report(order_id = "")
```

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Get all trade details
    client.trade_report()
    # Get particular traded details using order_id
    client.trade_report(order_id="")    
except Exception as e:
    print("Exception when trade report API->trade_report: %s\n" % e)
```

### Parameters
| Name        | Type  | Description |
|-------------|-------|-------------|
| *order_id*  | str   | Order ID.   |

### Return type

**object**

### Sample response

```json
{
    "stat": "Ok",
    "stCode": 200,
    "data": [
                    {
                      "exOrdId": "1000000000109874",
                      "brkClnt": "NA",
                      "cstFrm": "C",
                      "actId": "TESTYA24",
                      "rmk": "--",
                      "fldQty": 5,
                      "flDt": "21-Jun-2022",
                      "avgPrc": "658.70",
                      "ordSrc": "null",
                      "algId": "NA",
                      "prcTp": "MKT",
                      "prod": "CNC",
                      "exTm": "21-Jun-2022 14:30:38",
                      "nReqId": "1",
                      "exSeg": "nse_cm",
                      "trdSym": "AXISBANK-EQ",
                      "GuiOrdId": "SMCS_xcwlNEK4",
                      "flLeg": 1,
                      "rptTp": "fill",
                      "usrId": "TESTY1124A",
                      "hsUpTm": "2022/06/21 15:08:47",
                      "ordGenTp": "--",
                      "flId": "42857",
                      "flTm": "14:30:38",
                      "trnsTp": "B",
                      "nOrdNo": "220621000000085",
                      "algCat": "NA",
                      "ordDur": "DAY",
                      "boeSec": 1655802038,
                      "stkPrc": "0.00",
                      "sym": "AXISBANK",
                      "multiplier": "1",
                      "precision": "2",
                      "expDt": "NA",
                      "tok": "5900",
                      "genNum": "1",
                      "series": "EQ",
                      "prcNum": "1",
                      "genDen": "1",
                      "brdLtQty": 1,
                      "exp": "--",
                      "lotSz": "1",
                      "minQty": 0,
                      "optTp": "XX",
                      "prcDen": "1"
                    },
                    {
                      "exOrdId": "1000000000107980",
                      "brkClnt": "NA",
                      "cstFrm": "C",
                      "actId": "TESTYA24",
                      "rmk": "--",
                      "fldQty": 2,
                      "flDt": "21-Jun-2022",
                      "avgPrc": "641.00",
                      "ordSrc": "null",
                      "algId": "NA",
                      "prcTp": "MKT",
                      "prod": "CNC",
                      "exTm": "21-Jun-2022 14:21:07",
                      "nReqId": "1",
                      "exSeg": "nse_cm",
                      "trdSym": "AXISBANK-EQ",
                      "GuiOrdId": "SMCS_edg9l5UO",
                      "flLeg": 1,
                      "rptTp": "fill",
                      "usrId": "TESTY1124A",
                      "hsUpTm": "2022/06/21 15:08:47",
                      "ordGenTp": "--",
                      "flId": "41349",
                      "flTm": "14:21:07",
                      "trnsTp": "B",
                      "nOrdNo": "220621000000077",
                      "algCat": "NA",
                      "ordDur": "DAY",
                      "boeSec": 1655801467,
                      "stkPrc": "0.00",
                      "sym": "AXISBANK",
                      "multiplier": "1",
                      "precision": "2",
                      "expDt": "NA",
                      "tok": "5900",
                      "genNum": "1",
                      "series": "EQ",
                      "prcNum": "1",
                      "genDen": "1",
                      "brdLtQty": 1,
                      "exp": "--",
                      "lotSz": "1",
                      "minQty": 0,
                      "optTp": "XX",
                      "prcDen": "1"
                    },
                    {
                      "exOrdId": "1000000000096753",
                      "brkClnt": "NA",
                      "cstFrm": "C",
                      "actId": "TESTYA24",
                      "rmk": "--",
                      "fldQty": 1,
                      "flDt": "21-Jun-2022",
                      "avgPrc": "644.65",
                      "ordSrc": "null",
                      "algId": "NA",
                      "prcTp": "MKT",
                      "prod": "CNC",
                      "exTm": "21-Jun-2022 14:07:50",
                      "nReqId": "1",
                      "exSeg": "nse_cm",
                      "trdSym": "AXISBANK-EQ",
                      "GuiOrdId": "SMCS_kAeDQgi1",
                      "flLeg": 1,
                      "rptTp": "fill",
                      "usrId": "TESTY1124A",
                      "hsUpTm": "2022/06/21 15:08:47",
                      "ordGenTp": "--",
                      "flId": "35790",
                      "flTm": "14:07:50",
                      "trnsTp": "B",
                      "nOrdNo": "220621000000062",
                      "algCat": "NA",
                      "ordDur": "DAY",
                      "boeSec": 1655800670,
                      "stkPrc": "0.00",
                      "sym": "AXISBANK",
                      "multiplier": "1",
                      "precision": "2",
                      "expDt": "NA",
                      "tok": "5900",
                      "genNum": "1",
                      "series": "EQ",
                      "prcNum": "1",
                      "genDen": "1",
                      "brdLtQty": 1,
                      "exp": "--",
                      "lotSz": "1",
                      "minQty": 0,
                      "optTp": "XX",
                      "prcDen": "1"
                    }
                  ]
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  | Response headers |
|-------------|----------------------------------------------|------------------|
| *200*       | ok                                           | -                |
| *400*       | Invalid or missing input parameters          | -                |
| *403*       | Invalid session, please re-login to continue | -                |
| *429*       | Too many requests to the API                 | -                |
| *500*       | Unexpected error                             | -                |
| *502*       | Not able to communicate with OMS             | -                |
| *503*       | Trade API service is unavailable             | -                |
| *504*       | Gateway timeout, trade API is unreachable    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
