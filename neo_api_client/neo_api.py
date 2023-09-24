import inspect
import json
import asyncio
import neo_api_client
from neo_api_client.api_client import ApiClient
from neo_api_client.exceptions import ApiException, ApiValueError


class NeoAPI:
    """
        A class representing the NeoAPI, which is a client API for the Neo banking platform.

        The `NeoAPI` class provides methods to initialize the API client, log in to the platform, generate OTP, and perform 2FA authentication.

        Attributes:
            environment (str): The environment for the API client.
            configuration (neo_api_client.Configuration): The configuration for the API client.
            consumer_key (str): The consumer key for the API client.
            consumer_secret (str): The consumer secret for the API client.
            username (str): The username for the API client.
            password (str): The password for the API client.
            api_client (ApiClient): The API client instance.

        Methods:
            __init__(consumer_key=None, consumer_secret=None, host='uat', username=None, password=None):
                Initializes the `NeoAPI` instance with the given consumer key, consumer secret, host, username, and password.
                Validates the configuration and creates an API client instance.

            login(mobileNumber, password):
                Logs in to the platform using the given mobile number and password.
                Sets the view token, SID, and server ID in the configuration.

            generateOTP():
                Generates an OTP for 2FA authentication.

            session_2fa(OTP):
                Performs 2FA authentication using the given OTP.
                Sets the edit token, SID, RID, and server ID in the configuration.
    """

    def __init__(self, environment="uat", access_token=None, consumer_key=None, consumer_secret=None,
                 on_message=None, on_error=None, on_close=None, on_open=None, neo_fin_key=None):
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
        if not access_token:
            neo_api_client.req_data_validation.validate_configuration(consumer_key, consumer_secret)
            self.configuration = neo_api_client.NeoUtility(consumer_key=consumer_key, consumer_secret=consumer_secret,
                                                           host=environment)
            self.api_client = ApiClient(self.configuration)
            try:
                session_init = neo_api_client.LoginAPI(self.api_client).session_init()
                print(json.dumps({"data": session_init}))
            except ApiException as ex:
                error = ex
        elif access_token:
            self.configuration = neo_api_client.NeoUtility(access_token=access_token, host=environment)
            self.api_client = ApiClient(self.configuration)

        self.NeoWebSocket = None
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.on_open = on_open
        self.configuration.neo_fin_key = neo_fin_key

    def login(self, password=None, mobilenumber=None, userid=None, pan=None, mpin=None):
        """
        Logs in to the system by generating a view token using the provided mobile number and password.
        Generates an OTP (One-Time Password) for the user's session.

        Parameters:
        password (str): The password of the user.
        mobilenumber (str, optional): The mobile number of the user. Defaults to None.
        userid (str, optional): The user ID of the user. Defaults to None.
        pan (str, optional): The PAN (Permanent Account Number) of the user. Defaults to None.
        Either of pan/mobilenumber/userid has to pass to login

        Returns:
            {'data': {'token': '','sid': '', 'rid': '', 'hsServerId': '',isUserPwdExpired': , 'caches': {
        'baskets': '', 'lastUpdatedTS': '', 'multiplewatchlists': '', 'techchartpreferences': ''}, 'ucc': '',
        'greetingName': '', 'isTrialAccount': , 'dataCenter': '', 'searchAPIKey': ''}}


        Updates:
        view_token: sets the view token obtained from the API response.
        sid: sets the sid obtained from the API response.

        Raises:
        ApiException: if the view token or OTP generation fails.
        """
        if not mobilenumber and not userid and not pan:
            error = {
                'error': [{'code': '10300', 'message': 'Validation Errors! Any of Mobile Number, User Id and Pan has '
                                                       'to pass as part of login'}]}
            return error

        view_token = neo_api_client.LoginAPI(self.api_client).generate_view_token(password=password, mobilenumber=mobilenumber,
                                                                                  userid=userid, pan=pan, mpin=mpin)
        if "error" not in view_token:
            gen_otp = neo_api_client.LoginAPI(self.api_client).generate_otp()
            # print(gen_otp)
        else:
            gen_otp = {'error': [{'code': '10522', 'message': 'Issues while generating OTP! Try to login again.'}]}
        return view_token

    def session_2fa(self, OTP):
        """
            Establishes a session with the API using the provided OTP.

            Parameters:
            OTP (str): The one-time password (OTP) for the user's session.

            Returns: {'data': {'token': '', 'sid': '', 'rid': '', 'hsServerId': '', 'isUserPwdExpired': False,
            'caches': {'baskets': '', 'lastUpdatedTS': '', 'multiplewatchlists': '', 'techchartpreferences': ''},
            'ucc': '', 'greetingName': '', 'isTrialAccount': False, 'dataCenter': '', 'searchAPIKey': ''}}

            Updates:
            edit_token: sets the edit token obtained from the API response.
        """
        edit_token = neo_api_client.LoginAPI(self.api_client).login_2fa(OTP)
        return edit_token

    def place_order(self, exchange_segment, product, price, order_type, quantity, validity, trading_symbol,
                    transaction_type, amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None):
        """
            Places an order on the specified exchange segment and product, for a given trading symbol, transaction type,
            order type, quantity, and price.

            Parameters:
            exchange_segment (str): The exchange segment (e.g. "NSECM", "BSECM", "NSEFO", etc.)
            product (str): The product type (e.g. "CNC", "MIS", "NRML", etc.)
            price (float): The price of the order
            order_type (str): The order type (e.g. "LIMIT", "MARKET", etc.)
            quantity (int): The quantity of the order
            validity (str): The validity of the order (e.g. "DAY", "IOC", etc.)
            trading_symbol (str): The trading symbol of the stock
            transaction_type (str): The transaction type (e.g. "BUY", "SELL", etc.)
            amo (str, optional): Flag to indicate whether it is an AMO order. Defaults to "NO".
            disclosed_quantity (str, optional): Disclosed quantity for the order. Defaults to "0".
            market_protection (str, optional): Flag to indicate whether market protection is enabled. Defaults to "0".
            pf (str, optional): Flag to indicate whether the order is a Portfolio order. Defaults to "N".
            trigger_price (str, optional): Trigger price for Stop Loss orders. Defaults to "0".
            tag (str, optional): Optional tag to be added to the order. Defaults to None.

            Returns:
            Success/Failure Response from the API

        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                neo_api_client.req_data_validation.place_order_validation(exchange_segment, product, price, order_type,
                                                                          quantity, validity,
                                                                          trading_symbol, transaction_type)

                exchange_segment = neo_api_client.settings.exchange_segment[exchange_segment]
                product = neo_api_client.settings.product[product]
                order_type = neo_api_client.settings.order_type[order_type]
                place_order = neo_api_client.OrderAPI(self.api_client).order_placing(exchange_segment=exchange_segment,
                                                                                     product=product, price=price,
                                                                                     order_type=order_type, quantity=quantity,
                                                                                     validity=validity,
                                                                                     trading_symbol=trading_symbol,
                                                                                     transaction_type=transaction_type, amo=amo,
                                                                                     disclosed_quantity=disclosed_quantity,
                                                                                     market_protection=market_protection, pf=pf,
                                                                                     trigger_price=trigger_price, tag=tag)

                return place_order
            except Exception as e:
                return {'Error': e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def cancel_order(self, order_id, amo="NO", isVerify=False):
        """
            Cancels an order with the given `order_id` using the NEO API.

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
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                neo_api_client.req_data_validation.cancel_order_validation(order_id)
                cancel_order = neo_api_client.OrderAPI(self.api_client).order_cancelling(order_id=order_id,
                                                                                         isVerify=isVerify, amo=amo)
                return cancel_order
            except Exception as e:
                return {'Error': e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def order_report(self):
        """
            Retrieves a list of orders in the order book using the NEO API.

            Raises:
                Exception: If there was an error retrieving the order book.

            Returns:
                Json object of Orders.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                order_list = neo_api_client.OrderReportAPI(self.api_client).ordered_books()
                return order_list
            except Exception as e:
                return {'Error': e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def order_history(self, order_id):
        """
            Retrieves the order history for a given order ID using the NEO API.

            Args:
                order_id (str): A string representing the order ID to retrieve the history for.

            Raises:
                Exception: If there was an error retrieving the order history.

            Returns:
                Json object with the give order_id.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                neo_api_client.req_data_validation.order_history_validation(order_id)
                history_list = neo_api_client.OrderHistoryAPI(self.api_client).ordered_history(order_id=order_id)
                return history_list
            except Exception as e:
                return {'Error': e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def trade_report(self, order_id=None):
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
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                filtered_trades = neo_api_client.TradeReportAPI(self.api_client).trading_report(order_id=order_id)
                return filtered_trades
            except Exception as e:
                return {'Error': e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def modify_order(self, order_id, price, order_type, quantity, validity, instrument_token=None,
                     exchange_segment=None, product=None, trading_symbol=None, transaction_type=None,
                     trigger_price="0", dd="NA", market_protection="0", disclosed_quantity="0",
                     filled_quantity="0", amo='NO'):
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
        if self.configuration.edit_token and self.configuration.edit_sid:
            if order_id and instrument_token and exchange_segment and product and trading_symbol:
                exchange_segment = neo_api_client.settings.exchange_segment[exchange_segment]
                product = neo_api_client.settings.product[product]
                order_type = neo_api_client.settings.order_type[order_type]
                try:
                    quick_modify = neo_api_client.ModifyOrder(self.api_client). \
                        quick_modification(order_id=order_id, price=price, order_type=order_type, quantity=quantity,
                                           validity=validity, instrument_token=instrument_token, product=product,
                                           exchange_segment=exchange_segment, trading_symbol=trading_symbol,
                                           transaction_type=transaction_type, trigger_price=trigger_price,
                                           dd=dd, market_protection=market_protection,
                                           disclosed_quantity=disclosed_quantity,
                                           filled_quantity=filled_quantity, amo=amo)
                    return quick_modify
                except Exception:
                    return {'Error': "Exception has been occurred while connecting to API"}
            elif order_id and not instrument_token and not exchange_segment and not trading_symbol:
                try:
                    modify_order = neo_api_client.ModifyOrder(self.api_client).modification_with_orderid(
                        order_id=order_id, price=price, order_type=order_type, quantity=quantity,
                        validity=validity, instrument_token=instrument_token, product=product,
                        exchange_segment=exchange_segment, trading_symbol=trading_symbol,
                        transaction_type=transaction_type, trigger_price=trigger_price,
                        dd=dd, market_protection=market_protection, disclosed_quantity=disclosed_quantity,
                        filled_quantity=filled_quantity, amo=amo)
                    return modify_order

                except Exception:
                    return {'Error': "Exception has been occurred while connecting to API"}

            else:
                raise ValueError("Order ID is Mandate if we need to proceed further!")
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def positions(self):
        """
            Retrieves a list of positions using the NEO API.

            Raises:
                    Exception: If there was an error retrieving the positions.

            Returns:
                    A list of positions.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                position_list = neo_api_client.PositionsAPI(self.api_client).position_init()
                return position_list
            except Exception as e:
                return {"Error": e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def holdings(self):
        """
            Retrieves the current holdings for the portfolio using the NEO API.

            Raises:
                 Exception: If there was an error retrieving the holdings.

            Returns:
                 A list of portfolio holding objects.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                portfolio_list = neo_api_client.PortfolioAPI(self.api_client).portfolio_holdings()
                return portfolio_list
            except Exception as e:
                return {"Error": e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def margin_required(self, exchange_segment, price, order_type, product, quantity, instrument_token,
                        transaction_type,
                        trigger_price=None, broker_name="KOTAK", branch_id="ONLINE", stop_loss_type=None,
                        stop_loss_value=None, square_off_type=None, square_off_value=None, trailing_stop_loss=None,
                        trailing_sl_value=None):
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
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                neo_api_client.req_data_validation.margin_validation(exchange_segment, price, order_type, product, quantity,
                                                                     instrument_token,
                                                                     transaction_type)

                exchange_segment = neo_api_client.settings.exchange_segment[exchange_segment]
                product = neo_api_client.settings.product[product]
                order_type = neo_api_client.settings.order_type[order_type]
                margin_required = neo_api_client.MarginAPI(self.api_client).margin_init(exchange_segment=exchange_segment,
                                                                                        price=price, order_type=order_type,
                                                                                        product=product, quantity=quantity,
                                                                                        instrument_token=instrument_token,
                                                                                        transaction_type=transaction_type,
                                                                                        trigger_price=trigger_price,
                                                                                        broker_name=broker_name,
                                                                                        branch_id=branch_id,
                                                                                        stop_loss_type=stop_loss_type,
                                                                                        stop_loss_value=stop_loss_value,
                                                                                        square_off_type=square_off_type,
                                                                                        square_off_value=square_off_value,
                                                                                        trailing_stop_loss=trailing_stop_loss,
                                                                                        trailing_sl_value=trailing_sl_value)
                return margin_required
            except Exception as e:
                return {"Error": e}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def scrip_master(self, exchange_segment=None):
        """
        Retrieves the list of scrips available in the given exchange segment using the NEO API.

        Args:
            exchange_segment (str): A string representing the exchange segment to retrieve the list of scrips from.

        Raises:
            Exception: If there was an error retrieving the list of scrips.

        Returns:
            A list of scrips available in the given exchange segment.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                scrip_list = neo_api_client.ScripMasterAPI(self.api_client).scrip_master_init(
                    exchange_segment=exchange_segment)
                return scrip_list
            except Exception as e:
                return {"Error": 'Exchange Segment is not available'}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def limits(self, segment="ALL", exchange="ALL", product="ALL"):
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
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                neo_api_client.req_data_validation.limits_validation(segment, exchange, product)

                limits_list = neo_api_client.LimitsAPI(self.api_client).limit_init(segment=segment, exchange=exchange,
                                                                                   product=product)
                return limits_list
            except Exception as e:
                return {"Error": e, "message": 'Exchange Segment is not available'}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def search_scrip(self, exchange_segment, symbol="", expiry=None, option_type=None, strike_price=None,
                     ignore_50multiple=True):
        """
            Search for a scrip based on the given parameters.

            Args:
                exchange_segment (str): The exchange segment to search in. This argument is mandatory.
                symbol (str): The symbol to search for. This argument is optional.
                expiry (str): The expiry date to search for, in the format YYYYMM. This argument is optional.
                option_type (str): The option type to search for (either "CE" or "PE"). This argument is optional.
                strike_price (str): The strike price to search for. This argument is optional.
                ignore_50multiple (bool): Whether to ignore strike prices that are not multiples of 50. This argument is optional.

            Returns:
                dict: A dictionary containing information about the scrip. If there was an error, the dictionary will contain an "error"
                key with a list of error messages.

        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            if not exchange_segment:
                error = {
                    'error': [{'code': '10300', 'message': 'Validation Errors! Exchange Segment is Mandate to proceed '
                                                           'further'}]}
                return error
            try:
                exchange_segment = neo_api_client.settings.exchange_segment[exchange_segment]
                symbol = str(symbol).lower()
                scrip_list = neo_api_client.ScripSearch(self.api_client).scrip_search(exchange_segment=exchange_segment,
                                                                                      symbol=symbol, expiry=expiry,
                                                                                      option_type=option_type,
                                                                                      strike_price=strike_price,
                                                                                      ignore_50multiple=ignore_50multiple)
                return scrip_list
            except Exception as e:
                return {"Error": e, "message": 'Exchange Segment is not available'}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def quotes(self, instrument_tokens, quote_type=None, isIndex=False, session_token=None, sid=None,
               server_id=None, on_error=None):
        """
            Subscribe to real-time quotes for the given instrument tokens.

            Args:
                instrument_tokens (List): A JSON-encoded list of instrument tokens to subscribe to.
                quote_type (str): The type of quote to subscribe to.
                isIndex (bool): Whether the instrument is an index.
                session_token (str): The session token to use for authentication. This argument is optional if the login has been completed.
                sid (str): The session ID to use for authentication. This argument is mandatory if the session token is passed as input.
                server_id (str): The server ID to use for authentication. This argument is mandatory if the session token is passed as input.
                on_error (callable): A callback function to be called whenever an error occurs.

            Returns:
                JSON-encoded list of Quotes information

            Raises:
                ValueError: If the instrument tokens are not provided, or if the session token and SID are not provided when there is no Login.
        """
        if not instrument_tokens:
            raise ValueError("Without instrument_tokens it's hard to subscribe with None values")

        if len(instrument_tokens) > 100:
            # print({'Error': "Error", 'message': "Tokens must be less than 100"})
            return {'Error': "Error", 'message': "Tokens must be less than 100"}

        if not session_token and not self.configuration.edit_token:
            raise ValueError("Error! Login or pass the Session Token and SID")

        if session_token and not sid:
            raise ValueError("Kindly pass the SID token to proceed further")

        if self.configuration.edit_token and self.configuration.edit_sid:
            session_token = self.configuration.edit_token
            sid = self.configuration.edit_sid
            server_id = self.configuration.serverId

        if not self.NeoWebSocket:
            self.NeoWebSocket = neo_api_client.NeoWebSocket(sid, session_token, server_id)

        response = {}

        def callback(message):
            nonlocal response
            response = {'message': message}

        self.NeoWebSocket.get_quotes(instrument_tokens=instrument_tokens, quote_type=quote_type, isIndex=isIndex,
                                     callback=callback)

        if not response:
            pass

        return response

    def __on_open(self):
        if self.on_open:
            self.on_open("The Session has been Opened!")

    def __on_close(self):
        # print("[Socket]: Disconnected Demo Func !")
        if self.on_close:
            self.on_close("The Session has been Closed!")

    def __on_error(self, error):
        print("[Socket]: Error !")
        if self.on_error:
            self.on_error(error)

    def on_message(self, message):
        # print('[NEO_API]: "In-side NeoAPI Class')
        if self.on_message:
            self.on_message(message)

    def subscribe(self, instrument_tokens, isIndex=False, isDepth=False):
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
        if self.configuration.edit_token and self.configuration.edit_sid:
            if not self.NeoWebSocket:
                self.NeoWebSocket = neo_api_client.NeoWebSocket(self.configuration.edit_sid,
                                                                self.configuration.edit_token,
                                                                self.configuration.serverId)

            self.NeoWebSocket.get_live_feed(instrument_tokens=instrument_tokens, onmessage=self.__on_message,
                                            onerror=self.__on_error, onclose=self.__on_close,
                                            onopen=self.__on_open, isIndex=isIndex, isDepth=isDepth)
        else:
            print("Please complete the Login Flow to Subscribe the Scrips")

    def un_subscribe(self, instrument_tokens, isIndex=False, isDepth=False):
        if self.configuration.edit_token and self.configuration.edit_sid:
            if not self.NeoWebSocket:
                self.NeoWebSocket = neo_api_client.NeoWebSocket(self.configuration.edit_sid,
                                                                self.configuration.edit_token,
                                                                self.configuration.serverId)

            self.NeoWebSocket.un_subscribe_list(instrument_tokens=instrument_tokens, onmessage=self.__on_message,
                                                isIndex=isIndex, isDepth=isDepth)
            print("The Data has been Un-Subscribed")
        else:
            raise ValueError("Please complete the Login Flow to Un_Subscribe the Scrips")

    def help(self, function_name=None):
        class_name = NeoAPI.__name__
        try:
            if function_name is None:
                print(neo_api_client.settings.help_functions)
            else:
                function_name = str(function_name).strip()
                if function_name == "socket":
                    function_name = "subscribe"
                obj = getattr(NeoAPI, function_name, None)
                if obj is None:
                    print(f"{function_name} is not a valid function name.")
                else:
                    sig = inspect.signature(obj)
                    arg_desc = ', '.join([f"{param.name}: {param.annotation}" for param in sig.parameters.values()])
                    print(f"{class_name}.{function_name}({arg_desc}): {obj.__doc__}")
        except Exception as e:
            return {'Error': "Some Exception while connecting to help, Try after some time!", 'message': e}

    def logout(self):
        """
        Logs out the user from the NEO API.

        Raises:
            Exception: If there was an error logging out.

        Returns:
            None.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            try:
                log_off = neo_api_client.LogoutAPI(self.api_client).logging_out()
                self.configuration.bearer_token = None
                self.configuration.edit_sid = None
                self.configuration.edit_token = None
                return {"State": "OK", "message": "You have been successfully logged out"}

            except Exception as e:
                return {"State": "NOT_OK", "message": "Some Exception with the Logout Functionality"}
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}

    def subscribe_to_orderfeed(self):
        """
            Subscribe To OrderFeed

            Raises:
                Exception: If the user hasn't completes his 2FA.

            Returns:
                Order Feed information.
        """
        if self.configuration.edit_token and self.configuration.edit_sid:
            url = "wss://lhsi.kotaksecurities.com/realtime?sId="
            neo_api_client.ConnectHSM().hsm_connection(url=url, token=self.configuration.edit_token,
                                                       sid=self.configuration.edit_sid,
                                                       server_id=self.configuration.serverId)
        else:
            return {"Error Message": "Complete the 2fa process before accessing this application"}
