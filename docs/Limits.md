# **Limits**
Get RMS Limits details of your demat account

```python
client.limits()
```

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment=" ")
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    client.limits(segment="ALL", exchange="ALL",product="ALL")
except Exception as e:
    print("Exception when calling Limits->limits: %s\n" % e)
```

### Parameters
| Name        | Description                                 | Type           | 
|-------------|---------------------------------------------|----------------|
| *segment*   | CASH, CUR, FO, ALL (Default value - ALL)    | str [Optional] | 
| *exchange*  | NSE, BSE, ALL (Default value - ALL)         | str [Optional] | 
| *product*   | CNC, MIS, NRML, ALL (Default value - ALL)   | str [Optional] | 
 

### Return type

**object**

### Sample response

```json
{
                "AddPreExpMrgnMisPrsnt": "0.00",
                "CurExpMrgnNrmlPrsnt": "0.00",
                "CurPremiumNrmlPrsnt": "0.00",
                "RmsPayOutAmt": "0.00",
                "AdhocMargin": "0.00",
                "MrgnScrpBsktCncPrsnt": "0.00",
                "FoPremiumMisPrsnt": "17995.00",
                "tid": "server21_2816",
                "MrgnVarNrmlPrsnt": "0.00",
                "AmountUtilizedPrsnt": "0.00",
                "SplMrgnMisPrsnt": "0.00",
                "CurSpanMrgnNrmlPrsnt": "0.00",
                "SlbmVarElm": "0.00",
                "AuxRmsCollateral": "0.00",
                "FoUnRlsMtomPrsnt": "0.00",
                "AuxNotionalCash": "0.00",
                "AuxAdhocMargin": "0.00",
                "DaneLimit": "0.00",
                "RmsMutualFundAmt": "0.00",
                "RmsPayInAmt": "0.00",
                "CurPremiumMisPrsnt": "0.00",
                "SlbmLimit": "0.00",
                "MarginWarningPrcntPrsnt": "1.45",
                "MrgnVarMisPrsnt": "0.00",
                "CurRlsMtomPrsnt": "0.00",
                "ExposureMarginPrsnt": "7740.95",
                "NfospreadBenefit": "0.00",
                "stCode": 200,
                "CollateralValue": "10000000.00",
                "AddMrgnNrmlPrsnt": "0.00",
                "RmsCollateralMult": "1.00",
                "CncMrgnVarPrsnt": "0.00",
                "BoardLotLimit": "2000",
                "ComRlsMtomPrsnt": "0.00",
                "MarginVarPrsnt": "0.00",
                "DeliveryMarginPresent": "0.00",
                "RmsCollateral": "0.00",
                "ComExpsrMrgnMisPrsnt": "0.00",
                "CollateralValueMult": "1.00",
                "FoSpanrgnMisPrsnt": "58881.00",
                "Category": "CLIENT_MTF",
                "CurUnRlsMtomPrsnt": "0.00",
                "SpanMarginPrsnt": "58881.00",
                "CncSellcrdPresent": "0.00",
                "Collateral": "0.00",
                "MrgnScrpBsktNrmlPrsnt": "0.00",
                "UnrealizedMtomPrsnt": "0.00",
                "MrgnScrpBsktMisPrsnt": "0.00",
                "RealizedMtomPrsnt": "59268.70",
                "MtomWarningPrcntPrsnt": "0.00",
                "ComSpanMrgnNrmlPrsnt": "0.00",
                "DeliveryMrgnNrmlPrsnt": "0.00",
                "AdhocLimitMult": "1.00",
                "FoPremiumNrmlPrsnt": "0.00",
                "SpecialMarginPrsnt": "0.00",
                "SplMrgnNrmlPrsnt": "0.00",
                "MtomSquareOffWarningPrcntPrsnt": "0.00",
                "MarginUsedPrsnt": "188025.01",
                "FoRlsMtomPrsnt": "59265.00",
                "stat": "Ok",
                "NationalCashMult": "1.00",
                "FoSpanrgnNrmlPrsnt": "0.00",
                "AmtUntilizedPrsnt": "0.00",
                "PremiumPrsnt": "17995.00",
                "AddMrgnMisPrsnt": "0.00",
                "DeliveryMrgnMisPrsnt": "0.00",
                "SlbmMtom": "0.00",
                "CdsSpreadBenefit": "0.00",
                "ComExpsrMrgnNrmlPrsnt": "0.00",
                "FoExpMrgnNrmlPrsnt": "0.00",
                "BrokeragePrsnt": "1.86",
                "CashUnRlsMtomPrsnt": "0.00",
                "AddPreExpMrgnNrmlPrsnt": "0.00",
                "CurSpanMrgnMisPrsnt": "0.00",
                "ComUnRlsMtomPrsnt": "0.00",
                "CashRlsMtomPrsnt": "6.20",
                "NotionalCash": "0.00",
                "CurExpMrgnMisPrsnt": "0.00",
                "MarginUsed": "188025.01",
                "LendingFee": "0.00",
                "Net": "9811974.99",
                "TenderMrgnMisPrsnt": "0.00",
                "FoExpMrgnMisPrsnt": "7740.95",
                "TenderMrgnNrmlPrsnt": "0.00",
                "MarginScripBasketPrsnt": "0.00",
                "ComSpanMrgnMisPrsnt": "0.00"
}
```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Gets the Limits data for a client account    |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
