# neo_api_client.holdings


# **Holdings**

# Get Portfolio Holdings
client.holdings()

        """
            Retrieves the current holdings for the portfolio using the NEO API.

            Raises:
                 Exception: If there was an error retrieving the holdings.

            Returns:
                 A list of portfolio holding objects.
        """

Example Response:
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
                      "isAlternateScrip": false,
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
                      "isAlternateScrip": true,
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
                      "isAlternateScrip": false,
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
                      "isAlternateScrip": true,
                      "closingPrice": 73.8
                    },
                    {
                      "symbol": "GPIL",
                      "displaySymbol": "GPIL",
                      "averagePrice": 280.4275,
                      "quantity": 4,
                      "exchangeSegment": "nse_cm",
                      "exchangeIdentifier": "13409",
                      "holdingCost": 1121.71,
                      "mktValue": 1629.4,
                      "scripId": "5960fc030a164a0af93334089dc9cf2a8896594e",
                      "instrumentToken": 7964,
                      "instrumentType": "Equity",
                      "isAlternateScrip": false,
                      "closingPrice": 407.35
                    },
                    {
                      "symbol": "GPIL",
                      "displaySymbol": "GPIL",
                      "averagePrice": 280.4275,
                      "quantity": 4,
                      "exchangeSegment": "bse_cm",
                      "exchangeIdentifier": "532734",
                      "holdingCost": 1121.71,
                      "mktValue": 1629.4,
                      "scripId": "21a74b89385b75997f4c19891074f5e1a538bf49",
                      "instrumentToken": 7963,
                      "instrumentType": "Equity",
                      "isAlternateScrip": true,
                      "closingPrice": 407.35
                    }
                  ]
                }