# Kotak Neo Python SDK Development

- API version: 1.0.1
- Package version: 1.1.0

## Requirements.

Python 2.7+ and 3.0+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install "git+https://github.com/Kotak-Neo/kotak-neo-api.git#egg=neo_api_client"
```
(you may need to run `pip` with root permission: `sudo pip install -e "`)

Then import the package:
```python
import neo_api_client
```

### Setuptools

Install via [Setuptools]

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neo_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then refer to the sample code below for various API requests:

```python
from neo_api_client import NeoAPI
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)
    
#on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
client = NeoAPI(consumer_key="", consumer_secret="", 
                environment='uat', on_message=on_message, on_error=on_error, on_close=None, on_open=None)

# Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# Also this will generate the OTP to complete 2FA
client.login(mobilenumber="+919999999999", password="XXXX")

# Complete login and generate session token
client.session_2fa(OTP="")

# Once 2FA has you can place the order by using below function
client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                    transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None)
						
# Modify an order
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")

# Cancel an order
client.cancel_order(order_id = "")

# This is delay type. if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further
client.cancel_order(order_id = "", isVerify=True)

# Get Order Book
client.order_report()

# Get Trade Book
client.trade_report()

# Get Detailed Trade Report for specific order id. 
client.trade_report(order_id = "")

# Get Positions
client.positions()

# Get Portfolio Holdings
client.holdings()

# Get Limits
client.limits(segment="", exchange="", product="")

# Get Margin required for Equity orders. 
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")

# Get Scrip Master CSV file
client.scrip_master()

# Get Scrip Master CSV file for specific Exchange Segment. 
client.scrip_master(exchange_segment = "")

# Search for the Scrip details from Scrip master file
# exchange_segment is mandatory option to pass and remaining parameters are optional
client.search_scrip(exchange_segment="cde_fo", symbol="", expiry="", option_type="",
                    strike_price="")

# Get Quote details. 
instrument_tokens = [{"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""}]

# quote_type can be market_depth, ohlc, ltp, 52w, circuit_limits, scrip_details
# By Default quote_type is set as None that means you will get the complete data.
# Quotes api can be accessed without completing login by passing session_token, sid and server_id 
client.quotes(instrument_tokens = instrument_tokens, quote_type="", isIndex=False, 
              callback=on_message, session_token="", sid="",server_id="")

# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
client.un_subscribe(instrument_tokens=instrument_tokens)

#Order Feed 
client.subscribe_to_orderfeed()
#Terminate user's Session
client.logout()
```
## Documentation for API Endpoints

| Class | Method                                                  | Description |
|-------|---------------------------------------------------------| -------------|
| *LoginAPI* | [**neo_api_client.NeoAPI**](docs/Login.md#session_init) | Initialise Session|

