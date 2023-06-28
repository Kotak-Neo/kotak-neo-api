# **Scrip_Search**
Get the scrip details

```python
client.search_scrip(exchange_segment = "", symbol = "",  expiry = "", option_type = "", strike_price = "")
```

### Example

```python
from neo_api_client import NeoAPI

#First initialize session and generate session token

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment=" ")
client.login(mobilenumber=" ", password=" ")
client.session_2fa("")

try:
    # get scrip search details for particular exchange segment
    client.search_scrip(exchange_segment = "nse_cm", symbol = "YESBANK",  expiry = "", option_type = "", strike_price = "")
except Exception as e:
    print("Exception when calling scrip search api->scrip_search: %s\n" % e)

```
### Parameters

| Name                | Description                     | Type           |
|---------------------|---------------------------------|----------------|
| *exchange_segment*  |                                 | Str            |
| *symbol*            |                                 | Str            |
| *expiry*            | User can search multiple expiry - DDMMMYYYY, ex. 28JUN2023 | Str [optional] |
| *option_type*       | User can search option_type - CE/PE     | Str [optional] |
| *strike_price*      | User can search strike_price - For ex. 45000, 40000-45000, >40000, <45000   | Str [optional] |


### Return type

**object**

### Sample response

```json
{
"pSymbol": 11915,
"pGroup": "EQ",
"pExchSeg": "nse_cm",
"pInstType": null,
"pSymbolName": "YESBANK",
"pTrdSymbol": "YESBANK-EQ",
"pOptionType": null,
"pScripRefKey": "YESBANK",
"pISIN": "INE528G01035",
"pAssetCode": null,
"pSubGroup": null,
"pCombinedSymbol": null,
"pDesc": "YES BANK LIMITED",
"pAmcCode": null,
"pContractId": null,
"dTickSize": 5,
"lLotSize": 1,
"lExpiryDate": -1,
"lMultiplier": -1,
"lPrecision": 2,
"dStrikePrice;": -1,
"pExchange": "NSE",
"pInstName": null,
"pExpiryDate": null,
"pIssueDate": 805593600.0,
"pMaturityDate": null,
"pListingDate": 805593600.0,
"pNoDelStartDate": 0.0,
"pNoDelEndDate": 0.0,
"pBookClsStartDate": 1244246400.0,
"pBookClsEndDate": 1244764800.0,
"pRecordDate": 0.0,
"pCreditRating": "12.85-19.25",
"pReAdminDate": 0.0,
"pExpulsionDate": 0.0,
"pLocalUpdateTime": 1372357889.0,
"pDeliveryUnits": null,
"pPriceUnits": null,
"pLastTradingDate": null,
"pTenderPeridEndDate": null,
"pTenderPeridStartDate": null,
"pSellVarMargin": null,
"pBuyVarMargin": null,
"pInstrumentInfo": null,
"pRemarksText": null,
"pSegment": "CASH",
"pNav": null,
"pNavDate": null,
"pMfAmt": null,
"pSipSecurity": null,
"pFaceValue": 200.0,
"pTrdUnits": null,
"pExerciseStartDate": null,
"pExerciseEndDate": null,
"pElmMargin": 0.0,
"pVarMargin": 20.0,
"pTotProposedLimitValue": null,
"pScripBasePrice": null,
"pSettlementType": "T+1",
"pCurrectionTime": 315513000.0,
"iPermittedToTrade": 0,
"iBoardLotQty": 1,
"iMaxOrderSize": 6210995,
"iLotSize": 1,
"dOpenInterest": 0,
"dHighPriceRange": 1925.0,
"dLowPriceRange": 1285.0,
"dPriceNum": 1,
"dGenDen": 1,
"dGenNum": 1,
"dPriceQuatation": 0,
"dIssuerate": 0,
"dPriceDen": 1,
"dWarningQty": 0,
"dIssueCapital": 28754600000.0,
"dExposureMargin": 0,
"dMinRedemptionQty": 0,
"lFreezeQty": 6210995
}

```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | ok                                           |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
