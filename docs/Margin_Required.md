# neo_api_client.margin_required

# **Margin Required**

# Get Margin required for Equity orders. 
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")


        """
            Calculates the margin required for a given trade using the NEO API.

            Args:
                exchange_segment (str): A string representing the exchange segment for the trade.
                price (float): The price at which to execute the trade.
                order_type (str): A string representing the type of order to place.
                product (str): A string representing the product type for the trade.
                quantity (float): The quantity to trade.
                instrument_token (int): The instrument token of the stock to trade.
                transaction_type (str): A string representing the type of transaction to perform.
                trigger_price (float, optional): The trigger price for the trade.
                broker_name (str, optional): The name of the broker to use. Defaults to "KOTAK".
                branch_id (str, optional): The ID of the branch to use. Defaults to "ONLINE".
                stop_loss_type (str, optional): The type of stop loss to use.
                stop_loss_value (float, optional): The value for the stop loss.
                square_off_type (str, optional): The type of square off to use.
                square_off_value (float, optional): The value for the square off.
                trailing_stop_loss (str, optional): The type of trailing stop loss to use.
                trailing_sl_value (float, optional): The value for the trailing stop loss.

            Raises:
                 Exception: If there was an error calculating the margin.

            Returns:
                 The calculated margin required for the trade.

        """

Example Response:
                {
                    'data': 
                    {
                        'avlCash': '104.96', 
                        'insufFund': '12520.04', 
                        'stat': 'Ok', 
                        'totMrgnUsd': '12625.00', 
                        'mrgnUsd': '0.00', 
                        'reqdMrgn': '12625.00', 
                        'avlMrgn': '104.96', 
                        'stCode': 200, 
                        'tid': 'server2_2330220', 
                        'ordMrgn': '12625.00', 
                        'rmsVldtd': 78
                    }
                }

                