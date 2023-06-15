# neo_api_client.subscribe & neo_api_client.un_subscribe


# **Live Feed Subscription & Un_Subscription**

# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
client.un_subscribe(instrument_tokens=instrument_tokens)

#Order Feed 
client.subscribe_to_orderfeed()

        """
            Subscribe to live feeds for the given instrument tokens.

            Args:
                instrument_tokens (List): A JSON-encoded list of instrument tokens to subscribe to.
                isIndex (bool): Whether the instrument is an index. Default is False.
                isDepth (bool): Whether to subscribe to depth data. Default is False.

            Raises:
                ValueError: If the login flow is not completed.

            Returns:
                Live Feed from the socket

            The function establishes a WebSocket connection to the trading platform and subscribes to live feeds for the specified instrument tokens. When a new feed is received, the function's internal callback functions are called with the feed data as their arguments. If an error occurs, the on_error function is called with the error message as its argument.
        """