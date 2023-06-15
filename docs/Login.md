# neo_api_client.NeoAPI

# **session_init**

from neo_api_client import NeoAPI

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)
    
# on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server

client = NeoAPI(consumer_key="", consumer_secret="", 
                environment='uat', on_message=on_message, on_error=on_error, on_close=None, on_open=None)


    """
        Initializes the class and sets up the necessary configurations for the API client.
    
        Parameters:
        environment (str): The environment has to pass by user to connect 'UAT' or 'LIVE'.
        access_token (str, optional): The access token used for authentication. Defaults to None.
        consumer_key (str, optional): The consumer key used for authentication. Defaults to None.
        consumer_secret (str, optional): The consumer secret used for authentication. Defaults to None.
        on_message (function, optional): The function to be called when a message is received. Defaults to None.
        on_error (function, optional): The function to be called when an error occurs. Defaults to None.
        on_close (function, optional): The function to be called when the connection is closed. Defaults to None.
        on_open (function, optional): The function to be called when the connection is established. Defaults to None.
    
        Updates:
        self.on_message: sets the callback function for incoming messages for Websocket.
        self.on_error: sets the callback function for errors for Websocket.
        self.on_close: sets the callback function for connection close events for Websocket.
        self.on_open: sets the callback function for connection open events for Websocket.
    
        Raises:
        ApiException: if the session initiation fails.
    """
