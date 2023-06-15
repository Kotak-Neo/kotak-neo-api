# neo_api_client.positions

# **Positions**

# Get Positions using the NEO API
client.positions()

        """
            Retrieves a list of positions using the NEO API.

            Raises:
                    Exception: If there was an error retrieving the positions.

            Returns:
                    A list of positions.
        """
Example Response:
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
                            "brdLtQty": 25,
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