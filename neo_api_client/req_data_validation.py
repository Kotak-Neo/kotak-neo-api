import json
from neo_api_client.exceptions import ApiValueError
from neo_api_client.settings import exchange_segment_allowed_values, product_allowed_values, \
    order_type_allowed_values, segment_limits, exchange_limits, product_limits


def login_params_validation(mobilenumber=None, userid=None, pan=None, mpin=None, password=None):
    out_dict = {}
    if mobilenumber:
        if not isinstance(mobilenumber, str):
            raise ValueError("Input must be in String Format")
        # if len(mobilenumber) == 12:
        #     mobilenumber = "+" + str(mobilenumber)
        #     login_params_validation(mobilenumber=mobilenumber)
        # if len(mobilenumber) > 10 and len(mobilenumber) == 13:
        #     if not mobilenumber.startswith("+91"):
        #         raise ValueError("Expecting Mobile Number with country will starts with +91")
        #     else:
        #         mobilenumber = mobilenumber
        # if len(mobilenumber) < 10:
        #     Exception({'error': [{'code': '10300', 'message': 'Validation Errors'}]})
        if len(mobilenumber) == 10:
            mobilenumber = "+91" + str(mobilenumber)
        # else:
        #     raise ValueError(
        #         "Input Number length must be 13(with country code (+91)) or 10(Without Country Code), "
        #         "must be accepted")
        out_dict["mobileNumber"] = mobilenumber
    elif pan:
        pan = pan.upper()
        if not isinstance(pan, str):
            error = {
                'error': [{'code': '10300', 'message': 'Validation Errors! Input must be in String Format'}]}
            return error
        if len(pan) != 10:
            error = {
                'error': [{'code': '10300', 'message': 'Validation Errors! Length of PAN should be 10'}]}
            return error
        if not pan[:5].isalpha() or not pan[5:9].isdigit() or not pan[9].isalpha():
            error = {
                'error': [{'code': '10300', 'message': 'Validation Errors! Give PAN Number is Not Valid'}]}
            return error
        out_dict["pan"] = pan
    elif userid:
        out_dict["userid"] = userid
    else:
        error = {
            'error': [{'code': '10300', 'message': 'Validation Errors! Pass any of Mobile Number, User ID  or Pan'}]}
        return error

    if mpin:
        out_dict["mpin"] = mpin
    elif password:
        out_dict["password"] = password
    return out_dict


def validate_configuration(consumer_key, consumer_secret):
    if not consumer_key:
        raise ApiValueError(
            "Please provide the Consumer Key parameter while creating NeoTradeAPI object. Without Consumer Key "
            "the API cannot be accessed.")
    if not consumer_secret:
        raise ApiValueError(
            "Please provide the Consumer Secret parameter while creating NeoTradeAPI object. Without Consumer "
            "Secret the API cannot be accessed.")


def place_order_validation(exchange_segment, product, price, order_type, quantity, validity, trading_symbol,
                           transaction_type, amo=None, disclosed_quantity=None, market_protection=None, pf=None,
                           trigger_price=None, tag=None):
    # Exchange Segment validation
    if not isinstance(exchange_segment, str):
        raise ApiValueError("Exchange segment must be a string.")
    if exchange_segment not in exchange_segment_allowed_values:
        raise ApiValueError("Invalid exchange segment. Allowed values are NSE or nse_cm, BSE or bse_cm, NFO or nse_fo, "
                            "BFO or bse_fo, CDS or cde_fo, BCD or bcs_fo.")

    # Product validation
    if not isinstance(product, str):
        raise ApiValueError("Product must be a string.")
    if product not in product_allowed_values:
        raise ApiValueError("Invalid product. Allowed values are  NRML or Normal, CNC or Cash and Carry, MIS, "
                            "INTRADAY, CO or Cover order, BO or Bracket Order.")

    # Price validation
    if not isinstance(price, str):
        raise ApiValueError("Price must be a string.")

    # Order type validation
    if not isinstance(order_type, str):
        raise ApiValueError("Order type must be a string.")
    if order_type not in order_type_allowed_values:
        raise ApiValueError("Invalid order type. Allowed values are L or Limit, MKT or Market, SL or Stop loss limit,"
                            "SL-M or Stop loss market, SP or Spread, 2L or Tow leg, 3L or Three Leg.")

    # Quantity validation
    if not isinstance(quantity, str):
        raise ApiValueError("Quantity must be an string.")

    # Validity validation
    if not isinstance(validity, str):
        raise ApiValueError("Validity must be a string.")
    if validity not in ["DAY", "IOC"]:
        raise ApiValueError("Invalid validity. Allowed values are DAY, IOC.")

    # Trading symbol validation
    if not isinstance(trading_symbol, str):
        raise ApiValueError("Trading symbol must be a string.")

    # Transaction type validation
    if not isinstance(transaction_type, str):
        raise ApiValueError("Transaction type must be a string.")
    if transaction_type not in ["B", "S", "Buy", "Sell"]:
        raise ApiValueError("Invalid transaction type. Allowed values are B or Buy, S or Sell.")

    # AMO validation
    if amo is not None:
        if not isinstance(amo, str):
            raise ApiValueError("AMO must be a string.")

    # Disclosed Quantity validation
    if disclosed_quantity is not None:
        if not isinstance(disclosed_quantity, str):
            raise ApiValueError("disclosed_quantity must be a string.")

    # Market_protection validation
    if market_protection is not None:
        if not isinstance(market_protection, str):
            raise ApiValueError("market_protection must be a string.")

    # pf validation
    if pf is not None:
        if not isinstance(pf, str):
            raise ApiValueError("pf must be a string.")

    # trigger_price validation
    if trigger_price is not None:
        if not isinstance(trigger_price, str):
            raise ApiValueError("trigger_price must be a string.")

    # Tag validation
    if tag is not None:
        if not isinstance(tag, str):
            raise ApiValueError("tag must be a string.")


def cancel_order_validation(order_id, amo=None):
    if not isinstance(order_id, str) or not bool(order_id.strip()):
        raise ValueError("order_id parameter must be a non-empty string")

    # AMO validation
    if amo is not None:
        if not isinstance(amo, str):
            raise ApiValueError("AMO must be a string.")


def order_history_validation(order_id):
    if not isinstance(order_id, str):
        raise ValueError("order_id parameter must be a non-empty string")


def margin_validation(exchange_segment, price, order_type, product, quantity, instrument_token, transaction_type,
                      trigger_price=None):
    # Exchange Segment validation
    if not isinstance(exchange_segment, str):
        raise ApiValueError("Exchange segment must be a string.")
    if exchange_segment not in exchange_segment_allowed_values:
        raise ApiValueError("Invalid exchange segment. Allowed values are NSE or nse_cm, BSE or bse_cm, NFO or nse_fo, "
                            "BFO or bse_fo, CDS or cde_fo, BCD or bcs_fo.")

    # Product validation
    if not isinstance(product, str):
        raise ApiValueError("Product must be a string.")
    if product not in product_allowed_values:
        raise ApiValueError("Invalid product. Allowed values are  NRML or Normal, CNC or Cash and Carry, MIS, "
                            "INTRADAY, CO or Cover order, BO or Bracket Order.")

    # Price validation
    if not isinstance(price, str):
        raise ApiValueError("Price must be a string.")

    # Order type validation
    if not isinstance(order_type, str):
        raise ApiValueError("Order type must be a string.")
    if order_type not in order_type_allowed_values:
        raise ApiValueError("Invalid order type. Allowed values are L or Limit, MKT or Market, SL or Stop loss limit,"
                            "SL-M or Stop loss market, SP or Spread, 2L or Tow leg, 3L or Three Leg.")

    # Quantity validation
    if not isinstance(quantity, str):
        raise ApiValueError("Quantity must be an string.")

    # Instrument_token validation
    if not isinstance(instrument_token, str):
        raise ApiValueError("Instrument token must be a string.")

    # Transaction type validation
    if not isinstance(transaction_type, str):
        raise ApiValueError("Transaction type must be a string.")
    if transaction_type not in ["B", "S", "Buy", "Sell", "sell", "buy"]:
        raise ApiValueError("Invalid transaction type. Allowed values are B or Buy, S or Sell.")

    # trigger_price validation
    if trigger_price is not None:
        if not isinstance(trigger_price, str):
            raise ApiValueError("trigger_price must be a string.")


def limits_validation(segment, exchange, product):
    #  Segment validation
    if not isinstance(segment, str):
        raise ApiValueError("Segment must be a string.")
    if segment not in segment_limits:
        raise ApiValueError("Invalid segment. Allowed values are CASH, CUR, FO, ALL")

    #  Exchange validation
    if not isinstance(exchange, str):
        raise ApiValueError("Exchange must be a string.")
    if exchange not in exchange_limits:
        raise ApiValueError("Invalid Exchange. Allowed values are NSE, BSE, ALL")

    #  Product validation
    if not isinstance(product, str):
        raise ApiValueError("Product must be a string.")
    if product not in product_limits:
        raise ApiValueError("Invalid Product. Allowed values are CNC, MIS, NRML, ALL")
