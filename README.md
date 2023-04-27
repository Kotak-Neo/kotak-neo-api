# Neo Sdk Python Development

- API version: 1.0.1
- Package version: 1.1.0

## Requirements.

Python 2.7+ and 3.0+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install -e ""
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

#Complete login and generate session token
client.session_2fa(OTP="")

client.place_order(order_type = "N", instrument_token = 727, transaction_type = "BUY",\
                   quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                   tag = "string", validity = "GFD", variety = "REGULAR")
						
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

# Get Margin required for Equity orders. 

# Get Positions
client.positions()

# Get Quote details. 
instrument_tokens = [{"instrument_token": "6533", "exchange_segment": "nse_cm"},
    {"instrument_token": "6542", "exchange_segment": "nse_cm"},
    {"instrument_token": "6543", "exchange_segment": "nse_cm"},
    {"instrument_token": "6545", "exchange_segment": "nse_cm"}]

# quote_type can be market_depth, ohlc, ltp, 52w, circuit_limits, scrip_details
# By Default quote_type is set as None that means you will get the complete data.
# Quotes api can be accessed without completing login by passing session_token, sid and server_id 
client.quotes(instrument_tokens = instrument_tokens, quote_type="", isIndex=True, 
              callback=on_message, session_token="", sid="",server_id="")

#Terminate user's Session
client.logout()
```

