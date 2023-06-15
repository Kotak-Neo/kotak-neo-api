# neo_api_client.modify_order


# **Modify Order**

# Modify an order 

# Method 1 quick method 
client.modify_order(instrument_token = "11915", exchange_segment = "nse_cm", product = "NRML", price = "15", order_type = "L", quantity= "1", validity = "DAY", trading_symbol = "YESBANK-EQ", transaction_type = "B", order_id = "230327000000089")

# Method 2 delayed method
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")

        """
            There are 2 ways to modify the order one is bypassing all the parameters and another one is
            pass the order_id based on that we will take the values from order book and updated the latest details

            Modify an existing order with new values for its parameters.

            Args:
                amo: (str, optional): Default sets to NO. Override with 'YES' if you want to pass amo
                order_id (int): The unique identifier of the order to be modified.
                price (float): The new price for the order.
                order_type (str): The new order type for the order.
                quantity (int): The new quantity of the order.
                validity (str): The new validity for the order.
                instrument_token (int, optional): The unique identifier of the instrument. Defaults to None.
                exchange_segment (str, optional): The exchange segment of the order. Defaults to None.
                product (str, optional): The product type for the order. Defaults to None.
                trading_symbol (str, optional): The trading symbol of the order. Defaults to None.
                transaction_type (str, optional): The transaction type for the order. Defaults to None.
                trigger_price (float, optional): The new trigger price for the order. Defaults to "0".
                dd (str, optional): The new disclosed quantity for the order. Defaults to "NA".
                market_protection (str, optional): The new market protection for the order. Defaults to "0".
                disclosed_quantity (str, optional): The new disclosed quantity for the order. Defaults to "0".
                filled_quantity (str, optional): The new filled quantity for the order. Defaults to "0".

            Raises:
                ValueError: If order ID is not provided.

            Returns:
                The Status of the Given Order ID modification
        """

Example Response:
                {
                  "stat": "Ok",
                  "nOrdNo": "220621000000097",
                  "stCode": 200
                }
                
