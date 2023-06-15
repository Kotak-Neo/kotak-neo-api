# neo_api_client.cancel_order

# Cancel an order 

# Cancels an order with the given `order_id` using the NEO API.

# Method 1
client.cancel_order(order_id = "")

# Method 2 (Delayed)
# This is delay type. if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further
client.cancel_order(order_id = "", isVerify=True)

 """

            Args: order_id (str): The ID of the order to cancel.
            amo (str, optional): Default is "NO" for no amount specified.
            isVerify (bool, optional): Whether to verify the cancellation. Default is False.
            "If isVerify is True, we will first check the status of the given order. If the order status is not
             'rejected', 'cancelled', 'traded', or 'completed', we will proceed to cancel the order using the
             cancel_order function. Otherwise, we will display the order status to the user instead."

            Raises:
                ValueError: If the `order_id` is not a valid input.
                Exception: If there was an error cancelling the order.

            Returns:
                The Status of given order id.
"""

Example Response:
                {
                'stat': 'Ok',
                'nOrdNo': '230120000017243',
                'stCode': 200
                }