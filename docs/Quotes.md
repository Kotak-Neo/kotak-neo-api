# neo_api_client.quotes


# **Quotes**

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

Example Response:
                { 
                    "instrument_token": "11915", 
                    "trading_symbol": "YESBANK-EQ", 
                    "exchange_segment": "nse_cm", 
                    "last_trade_time": "19/01/2023 12:34:46", 
                    "ltp": "20.15", 
                    "last_traded_quantity": "8", 
                    "total_buy_quantity": "0", 
                    "total_sell_quantity": "20", 
                    "volume": "79640780", 
                    "average_price": "20.15", 
                    "oi": "0", 
                    "change": "-0.20", 
                    "net_change_percentage": "-0.98", 
                    "lower_circuit_limit": "16.15", 
                    "upper_circuit_limit": "24.15", 
                    "52week_high": "24.75", 
                    "52week_low": "12.10", 
                    "ohlc":
                          { 
                            "open": "20.25", 
                            "high": "21.00", 
                            "low": "19.50", 
                            "close": "20.50", 
                          },
                            "depth": 
                                   { "buy": 
                                            [ 
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "",
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              },
                                              { 
                                                "price": "", 
                                                "quantity": "", 
                                                "orders": "" 
                                              }, 
                                            ],
                                            "sell": 
                                                [ 
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  },
                                                  { 
                                                    "price": "", 
                                                    "quantity": "", 
                                                    "orders": "" 
                                                  }, 
                                                ] 
                                   }
                }
