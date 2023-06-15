# neo_api_client.limits

# **Limits**

# Get Limits details using the NEO API

client.limits(segment="", exchange="", product="")

    """
        Retrieves the limits available for the given segment, exchange and product using the NEO API.

        Args:
            segment (str): A string representing the segment for which limits are to be retrieved. Default value is "ALL".
            exchange (str): A string representing the exchange for which limits are to be retrieved. Default value is "ALL".
            product (str): A string representing the product for which limits are to be retrieved. Default value is "ALL".

        Raises:
            Exception: If there was an error retrieving the limits.

        Returns:
            A list of limits available for the given segment, exchange and product.
    """

Example Response:
                {
                  "AddPreExpMrgnMisPrsnt": "0.00",
                  "CurExpMrgnNrmlPrsnt": "0.00",
                  "CurPremiumNrmlPrsnt": "0.00",
                  "RmsPayOutAmt": "0.00",
                  "AdhocMargin": "0.00",
                  "MrgnScrpBsktCncPrsnt": "0.00",
                  "FoPremiumMisPrsnt": "0.00",
                  "MrgnVarNrmlPrsnt": "0.00",
                  "AmountUtilizedPrsnt": "0.00",
                  "SplMrgnMisPrsnt": "0.00",
                  "CurSpanMrgnNrmlPrsnt": "0.00",
                  "AuxRmsCollateral": "0.00",
                  "FoUnRlsMtomPrsnt": "0.00",
                  "AuxNotionalCash": "0.00",
                  "AuxAdhocMargin": "0.00",
                  "DaneLimit": "0.00",
                  "RmsPayInAmt": "0.00",
                  "CurPremiumMisPrsnt": "0.00",
                  "MarginWarningPrcntPrsnt": "0.00",
                  "MrgnVarMisPrsnt": "0.00",
                  "CurRlsMtomPrsnt": "0.00",
                  "ExposureMarginPrsnt": "0.00",
                  "NfospreadBenefit": "0.00",
                  "stCode": 200,
                  "CollateralValue": "0.00",
                  "AddMrgnNrmlPrsnt": "0.00",
                  "RmsCollateralMult": "0.00",
                  "CncMrgnVarPrsnt": "0.00",
                  "BoardLotLimit": "0",
                  "ComRlsMtomPrsnt": "0.00",
                  "MarginVarPrsnt": "0.00",
                  "DeliveryMarginPresent": "0.00",
                  "RmsCollateral": "0.00",
                  "ComExpsrMrgnMisPrsnt": "0.00",
                  "CollateralValueMult": "0.00",
                  "FoSpanrgnMisPrsnt": "0.00",
                  "Category": "CLIENT",
                  "CurUnRlsMtomPrsnt": "0.00",
                  "SpanMarginPrsnt": "0.00",
                  "CncSellcrdPresent": "0.00",
                  "Collateral": "0.00",
                  "MrgnScrpBsktNrmlPrsnt": "0.00",
                  "UnrealizedMtomPrsnt": "0.00",
                  "MrgnScrpBsktMisPrsnt": "0.00",
                  "RealizedMtomPrsnt": "0.00",
                  "MtomWarningPrcntPrsnt": "0.00",
                  "ComSpanMrgnNrmlPrsnt": "0.00",
                  "DeliveryMrgnNrmlPrsnt": "0.00",
                  "AdhocLimitMult": "0.00",
                  "FoPremiumNrmlPrsnt": "0.00",
                  "SpecialMarginPrsnt": "0.00",
                  "SplMrgnNrmlPrsnt": "0.00",
                  "MtomSquareOffWarningPrcntPrsnt": "0.00",
                  "MarginUsedPrsnt": "0.00",
                  "FoRlsMtomPrsnt": "0.00",
                  "stat": "Ok",
                  "NationalCashMult": "0.00",
                  "FoSpanrgnNrmlPrsnt": "0.00",
                  "AmtUntilizedPrsnt": "0.00",
                  "PremiumPrsnt": "0.00",
                  "AddMrgnMisPrsnt": "0.00",
                  "DeliveryMrgnMisPrsnt": "0.00",
                  "CdsSpreadBenefit": "0.00",
                  "ComExpsrMrgnNrmlPrsnt": "0.00",
                  "FoExpMrgnNrmlPrsnt": "0.00",
                  "BrokeragePrsnt": "0.00",
                  "CashUnRlsMtomPrsnt": "0.00",
                  "AddPreExpMrgnNrmlPrsnt": "0.00",
                  "CurSpanMrgnMisPrsnt": "0.00",
                  "ComUnRlsMtomPrsnt": "0.00",
                  "CashRlsMtomPrsnt": "0.00",
                  "NotionalCash": "0.00",
                  "CurExpMrgnMisPrsnt": "0.00",
                  "MarginUsed": "0.00",
                  "Net": "0.00",
                  "TenderMrgnMisPrsnt": "0.00",
                  "FoExpMrgnMisPrsnt": "0.00",
                  "TenderMrgnNrmlPrsnt": "0.00",
                  "MarginScripBasketPrsnt": "0.00",
                  "ComSpanMrgnMisPrsnt": "0.00"
                }