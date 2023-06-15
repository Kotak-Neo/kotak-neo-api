# neo_api_client.scrip_search

# **Scrip Search**

# Search for the Scrip details from Scrip master file
# exchange_segment is mandatory option to pass and remaining parameters are optional
# Client will be able to view the scrip details fetched from the ScripMaster Files.

client.search_scrip(exchange_segment = "nse_cm", symbol = "YESBANK",  expiry = "", option_type = "", strike_price = "")

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


Example Response:success : If scrip details found
                [
                  { 
                    "instrument_token": "11915", 
                    "trading_symbol": "YESBANK-EQ", 
                    "exchange_segment": "nse_cm", 
                    "series": "EQ", 
                    "scrip_name": "YES BANK LTD", 
                    "option_type": "", 
                    "expiry_date": "", 
                    "strick_price": "", 
                    "tick_size": "", 
                    "lot_size": "", 
                    "exchange": "NSE", 
                    "segment": "CASH", 
                    "multiplier": "-1", 
                    "precision": "2", 
                    "instrument_type": "", 
                  }
                ] 


Response Structure: error: If scrip details not found in scrip file
                   { 
                       "status": "not_ok", 
                       "msg": "No matched records have been found in the given exchange_segment!", 
                   }