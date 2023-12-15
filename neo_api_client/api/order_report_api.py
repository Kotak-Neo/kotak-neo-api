import requests
from neo_api_client import rest


class OrderReportAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def ordered_books(self):
        header_params = {
            'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
            "Sid": self.api_client.configuration.edit_sid,
            "Auth": self.api_client.configuration.edit_token,
            "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
            "accept": "application/json"
        }
        query_params = {"sId": self.api_client.configuration.serverId}

        URL = self.api_client.configuration.get_url_details("order_book")

        try:
            order_report = self.rest_client.request(
                url=URL, method='GET',
                query_params=query_params,
                headers=header_params
            )
            return order_report.json()
        except requests.exceptions.RequestException as e:
            # handle any exceptions that might be raised here
            print(f"Error occurred: {e}")
