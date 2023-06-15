# neo_api_client.trade_report


# **Trade Report**

# Get Trade Book
client.trade_report()

# Get Detailed Trade Report for specific order id. 
client.trade_report(order_id = "")


    """
            Retrieves a filtered list of trades using the NEO API.

            Args:
                order_id (str): An optional string representing the order ID to filter trades by. If not provided,
                    all trades will be returned.

            Raises:
                Exception: If there was an error retrieving the trade report.

            Returns:
                Json object of all trades/filtered items.
    """

Example Response:
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
                      "ordSrc": null,
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
                      "ordSrc": null,
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
                      "ordSrc": null,
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