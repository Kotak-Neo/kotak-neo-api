import requests
from neo_api_client import rest


class PortfolioAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def portfolio_holdings(self):
        header_params = {
            'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            'accept': '*/*'
        }
        params = {"sId": self.api_client.configuration.serverId}

        URL = self.api_client.configuration.get_url_details("holdings")

        try:
            portfolio_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=params,
                headers=header_params
            )
            return portfolio_report.json()
        except requests.exceptions.RequestException as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")
