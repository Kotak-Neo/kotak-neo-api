# **Order_Report & Order_History**

## Order_Report-<br/>
Get all order details<br/>
```python
client.order_report()
```

## Order_History-<br/>
Get details of a particular order<br/>
```python
client.order_history(order_id = "")
```

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment=" ")
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # Get all order details
    client.order_report()
    # Get particular details using order_id
    client.order_history()    
except Exception as e:
    print("Exception when order report API->order_report: %s\n" % e)
```

### Parameters
| Name        | Description | Type  |
|-------------|-------------|-------|
| *order_id*  | Order ID    | str   |

### Return type

**object**

### Sample response

```json
{

        "stat": "Ok",
        "stCode": 200,
        "data": [
                    {
                      "brkClnt": "--",
                      "ordValDt": "NA",
                      "exUsrInfo": "NA",
                      "mfdBy": "NA",
                      "vendorCode": "",
                      "rmk": "--",
                      "odCrt": "NA",
                      "ordSrc": "ADMINCPPAPI_MOB",
                      "sipInd": "NA",
                      "prc": "0.00",
                      "prcTp": "MKT",
                      "cnlQty": 0,
                      "uSec": "364529",
                      "classification": "0",
                      "mktPro": "0.00",
                      "ordEntTm": "--",
                      "reqId": "1",
                      "qty": 1,
                      "unFldSz": 0,
                      "mktProPct": "--",
                      "exOrdId": "NA",
                      "dscQty": 0,
                      "expDt": "NA",
                      "trgPrc": "0.00",
                      "tok": "11536",
                      "symOrdId": "NA",
                      "fldQty": 0,
                      "ordDtTm": "21-Jun-2022 14:49:32",
                      "avgPrc": "0.00",
                      "algId": "NA",
                      "stat": "Ok",
                      "prod": "CNC",
                      "exSeg": "nse_cm",
                      "GuiOrdId": "1655803172-359607-TESTY1124A-ADMINAPI",
                      "usrId": "TESTY1124A",
                      "rptTp": "NA",
                      "exCfmTm": "--",
                      "hsUpTm": "2022/06/21 14:55:28",
                      "ordGenTp": "NA",
                      "vldt": "DAY",
                      "tckSz": "0.05",
                      "ordSt": "rejected",
                      "trnsTp": "B",
                      "refLmtPrc": 0,
                      "coPct": 0,
                      "nOrdNo": "292837000456098",
                      "ordAutSt": "NA",
                      "rejRsn": "RMS:Rule: Check circuit limit including square off order exceeds  for entity account-TESTYA24 across exchange across segment across product ",
                      "boeSec": 1655803172,
                      "expDtSsb": "--",
                      "dscQtyPct": "0",
                      "stkPrc": "0.00",
                      "sym": "TCS",
                      "trdSym": "TCS-EQ",
                      "multiplier": "1",
                      "precision": "2",
                      "noMktProFlg": "0.00",
                      "genNum": "1",
                      "series": "EQ",
                      "prcNum": "1",
                      "genDen": "1",
                      "brdLtQty": "1",
                      "mktProFlg": "0.00",
                      "defMktProV": "0.00",
                      "lotSz": "1",
                      "minQty": 0,
                      "optTp": "XX",
                      "prcDen": "1"
                    },
                    {
                      "brkClnt": "--",
                      "ordValDt": "NA",
                      "exUsrInfo": "NA",
                      "mfdBy": "NA",
                      "vendorCode": "",
                      "rmk": "--",
                      "odCrt": "NA",
                      "ordSrc": "ADMINCPPAPI_MOB",
                      "sipInd": "NA",
                      "prc": "0.00",
                      "prcTp": "MKT",
                      "cnlQty": 0,
                      "uSec": "379164",
                      "classification": "0",
                      "mktPro": "0.00",
                      "ordEntTm": "--",
                      "reqId": "1",
                      "qty": 1,
                      "unFldSz": 0,
                      "mktProPct": "--",
                      "exOrdId": "NA",
                      "dscQty": 0,
                      "expDt": "NA",
                      "trgPrc": "0.00",
                      "tok": "11536",
                      "symOrdId": "NA",
                      "fldQty": 0,
                      "ordDtTm": "21-Jun-2022 14:48:39",
                      "avgPrc": "0.00",
                      "algId": "NA",
                      "stat": "Ok",
                      "prod": "CNC",
                      "exSeg": "nse_cm",
                      "GuiOrdId": "1655803119-377269-TESTY1124A-ADMINAPI",
                      "usrId": "TESTY1124A",
                      "rptTp": "NA",
                      "exCfmTm": "--",
                      "hsUpTm": "2022/06/21 14:55:28",
                      "ordGenTp": "NA",
                      "vldt": "DAY",
                      "tckSz": "0.05",
                      "ordSt": "rejected",
                      "trnsTp": "B",
                      "refLmtPrc": 0,
                      "coPct": 0,
                      "nOrdNo": "220287600096097",
                      "ordAutSt": "NA",
                      "rejRsn": "RMS:Rule: Check circuit limit including square off order exceeds  for entity account-TESTYA24 across exchange across segment across product ",
                      "boeSec": 1655803119,
                      "expDtSsb": "--",
                      "dscQtyPct": "0",
                      "stkPrc": "0.00",
                      "sym": "TCS",
                      "trdSym": "TCS-EQ",
                      "multiplier": "1",
                      "precision": "2",
                      "noMktProFlg": "0.00",
                      "genNum": "1",
                      "series": "EQ",
                      "prcNum": "1",
                      "genDen": "1",
                      "brdLtQty": "1",
                      "mktProFlg": "0.00",
                      "defMktProV": "0.00",
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
| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Order canceled successfully                  |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
