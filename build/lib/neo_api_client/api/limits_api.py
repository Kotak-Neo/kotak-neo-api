import requests
from neo_api_client import rest
from neo_api_client.exceptions import ApiException


class LimitsAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def limit_init(self, segment=None, exchange=None, product=None):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
                         "accept": "application/json",
                         "Content-Type": "application/x-www-form-urlencoded"
                         }

        query_params = {"sId": self.api_client.configuration.serverId}

        body_params = {"seg": segment, "exch": exchange, "prod": product}

        URL = self.api_client.configuration.get_url_details("limits")

        try:
            limits_report = self.rest_client.request(
                url=URL, method='POST',
                query_params=query_params,
                headers=header_params,
                body=body_params
            )
            return limits_report.json()
        except ApiException as ex:
            return {"error": ex}
