import requests
from neo_api_client import rest


class TradeReportAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def trading_report(self, order_id):
        header_params = {
            'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
            "accept": "application/json"
        }
        query_params = {"sId": self.api_client.configuration.serverId}
        URL = self.api_client.configuration.get_url_details("trade_report")
        try:
            trade_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=query_params,
                headers=header_params
            ).json()

            if order_id:
                output_json = {}
                if 'data' in trade_report:
                    output_json['tid'] = trade_report['tid']
                    output_json['stat'] = trade_report['stat']
                    output_json['stCode'] = trade_report['stCode']
                    for item in trade_report['data']:
                        if item['nOrdNo'] == order_id:
                            output_json["data"] = item
                    return output_json
                else:
                    return {"Message": "There is no trades available with the given order id"}
            else:
                return trade_report
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
