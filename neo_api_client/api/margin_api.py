import json
from neo_api_client import rest
from neo_api_client.exceptions import ApiException


class MarginAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def margin_init(self, exchange_segment, price, order_type, product, quantity, instrument_token, transaction_type,
                    trigger_price, broker_name, branch_id, stop_loss_type, stop_loss_value,
                    square_off_type, square_off_value, trailing_stop_loss, trailing_sl_value):

        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
                         "accept": "application/json",
                         "Content-Type": "application/x-www-form-urlencoded"}

        body_params = {"exSeg": exchange_segment, "prc": price, "prcTp": order_type, "prod": product, "qty": quantity,
                       "tok": instrument_token, "trnsTp": transaction_type, "trgPrc": trigger_price,
                       "brkName": broker_name, "brnchId": branch_id, "slAbsOrTks": stop_loss_type,
                       "slVal": stop_loss_value, "sqrOffAbsOrTks": square_off_type, "sqrOffVal": square_off_value,
                       "trailSL": trailing_stop_loss, "tSLTks": trailing_sl_value}

        query_params = {"sId": self.api_client.configuration.serverId}

        try:
            URL = self.api_client.configuration.get_url_details("margin")
            margin_resp = self.rest_client.request(
                url=URL, method='POST',
                query_params=query_params,
                headers=header_params,
                body=body_params
            )

            return {"data": json.loads(margin_resp.text)}

        except ApiException as ex:
            return {"error": ex}
