import json
import asyncio
import neo_api_client
from neo_api_client.api_client import ApiClient
from neo_api_client.exceptions import ApiException, ApiValueError
from . import req_data_validation, settings


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
                 on_message=None, on_error=None, on_close=None, on_open=None):
        """
        Initializes the class and sets up the necessary configurations for the API client.

        Parameters:
        environment (str): The environment has to pass by user to connect 'UAT' or 'LIVE'.
        consumer_key (str, optional): The consumer key used for authentication. Defaults to None.
        consumer_secret (str, optional): The consumer secret used for authentication. Defaults to None.
        username (str, optional): The username for the API. Defaults to None.
        password (str, optional): The password for the API. Defaults to None.

        Updates:
        self.configuration: sets the configuration object using the provided consumer key, consumer secret, username, password, and host.
        self.consumer_key: sets the consumer key from the configuration object.
        self.consumer_secret: sets the consumer secret from the configuration object.
        self.api_client: sets the API client using the configuration object.
        self.configuration.token: sets the bearer token obtained from the API response.

        Raises:
        ApiException: if the session initiation fails.
        """
        if not access_token:
            req_data_validation.validate_configuration(consumer_key, consumer_secret)
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

    def login(self, password, mobilenumber=None, userid=None, pan=None):
        """
        Logs in to the system by generating a view token using the provided mobile number and password.
        Generates an OTP (One-Time Password) for the user's session.

        Parameters:
        mobileNumber (str): The mobile number of the user.
        password (str): The password of the user.

        Returns:
        None

        Updates:
        self.configuration.view_token: sets the view token obtained from the API response.
        self.configuration.sid: sets the sid obtained from the API response.
        """
        if not mobilenumber and not userid and not pan:
            error = {
                'error': [{'code': '10300', 'message': 'Validation Errors! Any of Mobile Number, User Id and Pan has '
                                                       'to pass as part of login'}]}
            return error

        view_token = neo_api_client.LoginAPI(self.api_client).generate_view_token(password, mobilenumber=mobilenumber,
                                                                                  userid=userid, pan=pan)
        print(view_token)
        if "error" not in view_token:
            gen_otp = neo_api_client.LoginAPI(self.api_client).generate_otp()
            print(gen_otp)

    def session_2fa(self, OTP):
        """
        Logs in using two-factor authentication (2FA) with the provided OTP (One-Time Password).

        Parameters:
        OTP (str): The one-time password for the 2FA process.

        Returns:
        None

        Updates:
        self.configuration.edit_token: sets the edit token obtained from the API response.
        self.configuration.edit_sid: sets the sid obtained from the API response.
        self.configuration.edit_rid: sets the rid obtained from the API response.
        self.configuration.serverId: sets the server id obtained from the API response.
        """
        edit_token = neo_api_client.LoginAPI(self.api_client).login_2fa(OTP)
        print(edit_token)

    def place_order(self, exchange_segment, product, price, order_type, quantity, validity, trading_symbol,
                    transaction_type, amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None):
        req_data_validation.place_order_validation(exchange_segment, product, price, order_type, quantity, validity,
                                                   trading_symbol, transaction_type)

        exchange_segment = settings.exchange_segment[exchange_segment]
        product = settings.product[product]
        order_type = settings.order_type[order_type]
        place_order = neo_api_client.OrderAPI(self.api_client).order_placing(exchange_segment=exchange_segment,
                                                                             product=product, price=price,
                                                                             order_type=order_type, quantity=quantity,
                                                                             validity=validity,
                                                                             trading_symbol=trading_symbol,
                                                                             transaction_type=transaction_type, amo=amo,
                                                                             disclosed_quantity=disclosed_quantity,
                                                                             market_protection=market_protection, pf=pf,
                                                                             trigger_price=trigger_price, tag=tag)

        print("Place Order OutCome ", place_order)

    def cancel_order(self, order_id, amo="NO", isVerify=False):
        req_data_validation.cancel_order_validation(order_id)

        try:
            cancel_order = neo_api_client.OrderAPI(self.api_client).order_cancelling(order_id=order_id,
                                                                                     isVerify=isVerify, amo=amo)
            print("[CANCEL ORD RESP]: ", cancel_order)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def order_book(self):
        try:
            order_list = neo_api_client.OrderReportAPI(self.api_client).ordered_books()
            print("[ORDER BOOK RESP]: ", order_list)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def order_history(self, order_id):
        req_data_validation.order_history_validation(order_id)
        try:
            history_list = neo_api_client.OrderHistoryAPI(self.api_client).ordered_history(order_id=order_id)
            print("[ORDER HISTORY RESP]:  ", history_list)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def trade_report(self, order_id=None):
        try:
            filtered_trades = neo_api_client.TradeReportAPI(self.api_client).trading_report(order_id=order_id)
            print("[TRADE RESP]: ", filtered_trades)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def modify_order(self, order_id, price, order_type, quantity, validity, instrument_token=None,
                     exchange_segment=None, product=None, trading_symbol=None, transaction_type=None,
                     trigger_price="0", dd="NA", market_protection="0", disclosed_quantity="0",
                     filled_quantity="0"):
        if order_id and instrument_token and exchange_segment and product and trading_symbol:
            exchange_segment = settings.exchange_segment[exchange_segment]
            product = settings.product[product]
            order_type = settings.order_type[order_type]
            try:
                quick_modify = neo_api_client.ModifyOrder(self.api_client). \
                    quick_modification(order_id=order_id, price=price, order_type=order_type, quantity=quantity,
                                       validity=validity, instrument_token=instrument_token, product=product,
                                       exchange_segment=exchange_segment, trading_symbol=trading_symbol,
                                       transaction_type=transaction_type, trigger_price=trigger_price,
                                       dd=dd, market_protection=market_protection,
                                       disclosed_quantity=disclosed_quantity,
                                       filled_quantity=filled_quantity)
                print("Response For Modify Order", quick_modify)
            except Exception:
                print("Exception has been occurred while connecting to API")
        elif order_id and not instrument_token and not exchange_segment and not trading_symbol:
            try:
                modify_order = neo_api_client.ModifyOrder(self.api_client).modification_with_orderid(
                    order_id=order_id, price=price, order_type=order_type, quantity=quantity,
                    validity=validity, instrument_token=instrument_token, product=product,
                    exchange_segment=exchange_segment, trading_symbol=trading_symbol,
                    transaction_type=transaction_type, trigger_price=trigger_price,
                    dd=dd, market_protection=market_protection, disclosed_quantity=disclosed_quantity,
                    filled_quantity=filled_quantity)
                print("Response For Modify Order", modify_order)

            except Exception:
                print("Exception has been occurred while connecting to API")

        else:
            raise ValueError("Order ID is Mandate if we need to proceed further!")

    async def async_quote(self, instrument_tokens, callback, quote_type, isIndex, session_token,
                          sid, server_id, on_error):
        instrument_tokens = json.loads(instrument_tokens)
        print("INst Tokens ", type(instrument_tokens))
        print("INst Tokens ", instrument_tokens)
        if not instrument_tokens:
            raise ValueError("Without instrument_tokens it's hard to subscribe with None values")

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

        self.NeoWebSocket.get_quotes(instrument_tokens=instrument_tokens, quote_type=quote_type, callback=callback,
                                     isIndex=isIndex)

    def quotes(self, instrument_tokens, callback, quote_type=None, isIndex=False, session_token=None, sid=None,
               server_id=None, on_error=None):
        asyncio.run(
            self.async_quote(instrument_tokens, callback, quote_type=quote_type, isIndex=isIndex,
                             session_token=session_token, sid=sid,
                             server_id=server_id, on_error=on_error))

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

    def __on_message(self, message):
        print('[NEO_API]: "In-side NeoAPI Class')
        if self.on_message:
            self.on_message(message)

    async def async_subscribe(self, instrument_tokens, isIndex=False, isDepth=False):
        self.configuration.edit_token = "HELLO SAMPLE"
        self.configuration.edit_sid = "SAMPLE"
        self.configuration.serverId = "server21"
        if self.configuration.edit_token and self.configuration.edit_sid:
            if not self.NeoWebSocket:
                self.NeoWebSocket = neo_api_client.NeoWebSocket(self.configuration.edit_sid,
                                                                self.configuration.edit_token,
                                                                self.configuration.serverId)

            self.NeoWebSocket.get_live_feed(instrument_tokens=instrument_tokens, onmessage=self.__on_message,
                                            onerror=self.__on_error, onclose=self.__on_close,
                                            onopen=self.__on_open, isIndex=isIndex, isDepth=isDepth)
        else:
            raise ValueError("Please complete the Login Flow to Subscribe the Scrips")

    def subscribe(self, instrument_tokens, isIndex=False, isDepth=False):
        asyncio.run(self.async_subscribe(instrument_tokens, isIndex=isIndex, isDepth=isDepth))

    async def async_un_subscribe(self, instrument_tokens, isIndex, isDepth):
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

    def un_subscribe(self, instrument_tokens, isIndex=False, isDepth=False):
        asyncio.run(self.async_un_subscribe(instrument_tokens, isIndex=isIndex, isDepth=isDepth))

    def positions(self):
        try:
            position_list = neo_api_client.PositionsAPI(self.api_client).position_init()
            print("Positions:", position_list)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def holdings(self):
        try:
            portfolio_list = neo_api_client.PortfolioAPI(self.api_client).portfolio_holdings()
            print("Portfolio Holdings:", portfolio_list)
        except Exception as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")

    def margin_required(self, exchange_segment, price, order_type, product, quantity, instrument_token,
                        transaction_type,
                        trigger_price=None, broker_name="KOTAK", branch_id="ONLINE", stop_loss_type=None,
                        stop_loss_value=None, square_off_type=None, square_off_value=None, trailing_stop_loss=None,
                        trailing_sl_value=None):

        req_data_validation.margin_validation(exchange_segment, price, order_type, product, quantity, instrument_token,
                                              transaction_type)

        exchange_segment = settings.exchange_segment[exchange_segment]
        product = settings.product[product]
        order_type = settings.order_type[order_type]
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
        print("Margin OutCome ", margin_required)
