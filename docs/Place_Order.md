# neo_api_client.place_order


# **Place Order**

# The place_order function is used to submit a new order using the NEO API . It takes several parameters to define the order details and performs validations before placing the order.
 
client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                    transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None) 
  
    '''
        Parameters:
    
        exchange_segment (string): The exchange segment where the order should be placed.
        product (string): The type of product for the order.
        price (float): The price at which the order should be executed.
        order_type (string): The type of order (e.g., "LIMIT", "MARKET", "STOP_LIMIT").
        quantity (int): The quantity of the product to buy or sell.
        validity (string): The validity of the order (e.g., "DAY", "IOC", "GTC").
        trading_symbol (string): The trading symbol of the product.
        transaction_type (string): The type of transaction (e.g., "BUY", "SELL").
        amo (string, optional): Flag indicating if the order is an After Market Order (AMO). Defaults to "NO".
        disclosed_quantity (string, optional): The quantity to be disclosed to the market. Defaults to "0".
        market_protection (string, optional): Flag indicating if market protection is enabled. Defaults to "0".
        pf (string, optional): Flag indicating if the order is a portfolio order. Defaults to "N".
        trigger_price (string, optional): The trigger price for the order. Defaults to "0".
        tag (any, optional): Additional information or tags for the order. Defaults to None.
    '''

Example Response:
                {
                'stat': 'Ok',
                'nOrdNo': '230120000017243',
                'stCode': 200
                }