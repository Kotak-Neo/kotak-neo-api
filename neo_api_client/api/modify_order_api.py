import neo_api_client
from neo_api_client import rest
from neo_api_client.exceptions import ApiException


class ModifyOrder(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def quick_modification(self, order_id, price, order_type, quantity, validity, instrument_token,
                           exchange_segment, product, trading_symbol, transaction_type, trigger_price,
                           dd, market_protection, disclosed_quantity, filled_quantity):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
                         "Content-Type": "application/x-www-form-urlencoded"}

        body_params = {"tk": instrument_token, "mp": market_protection, "pc": product, "dd": dd,
                       "dq": disclosed_quantity, "vd": validity, "ts": trading_symbol, "tt": transaction_type,
                       "pr": price, "pt": order_type, "fq": filled_quantity,
                       "tp": trigger_price, "qt": quantity, "no": order_id, "es": exchange_segment}

        query_params = {"sId": self.api_client.configuration.serverId}
        try:
            URL = self.api_client.configuration.get_url_details("modify_order")
            orders_resp = self.rest_client.request(
                url=URL, method='POST',
                query_params=query_params,
                headers=header_params,
                body=body_params
            )

            return {"data": orders_resp.text}

        except ApiException as ex:
            return {"error": ex}

    def modification_with_orderid(self, order_id, price, order_type, quantity, validity, instrument_token,
                                  exchange_segment, product, trading_symbol, transaction_type, trigger_price,
                                  dd, market_protection, disclosed_quantity, filled_quantity):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
                         "Content-Type": "application/x-www-form-urlencoded"}

        order_book_resp = neo_api_client.OrderReportAPI(self.api_client).ordered_books()
        if "data" not in order_book_resp:
            return {"Message": "There is no Data in the Order Book"}
        else:
            for item in order_book_resp["data"]:
                if item["nOrdNo"] == order_id:
                    if item["ordSt"] in ["rejected", "cancelled", "complete", "traded"]:
                        if item["ordSt"] == 'complete':
                            item["ordSt"] = 'Traded'
                        return {"Error": "The Given Order Status is " + str(item["ordSt"]) +
                                         ", So we can't proceed further",
                                "Reason": item["rejRsn"]}
                    else:
                        trading_symbol = trading_symbol or item['trdSym']
                        instrument_token = instrument_token or item['tok']
                        product = product or item['prod']
                        transaction_type = transaction_type or item['trnsTp']
                        exchange_segment = exchange_segment or item['exSeg']
                        if trigger_price != "0":
                            trigger_price = trigger_price
                        else:
                            trigger_price = item['trgPrc']

                        body_params = {
                            "tk": instrument_token,
                            "mp": market_protection,
                            "pc": product,
                            "dd": dd,
                            "dq": disclosed_quantity,
                            "vd": validity,
                            "ts": trading_symbol,
                            "tt": transaction_type,
                            "pr": price,
                            "pt": order_type,
                            "fq": filled_quantity,
                            "tp": trigger_price,
                            "qt": quantity,
                            "no": order_id,
                            "es": exchange_segment,
                        }
                        query_params = {"sId": self.api_client.configuration.serverId}
                        try:
                            URL = self.api_client.configuration.get_url_details("modify_order")
                            orders_resp = self.rest_client.request(
                                url=URL, method='POST',
                                query_params=query_params,
                                headers=header_params,
                                body=body_params
                            )
                            return orders_resp.json()

                        except ApiException as ex:
                            return {"error": ex}
            else:
                return {"Message": f"The Given Order Number is {order_id} and it is not matching with anyOrder of "
                                   f"the orders"}
