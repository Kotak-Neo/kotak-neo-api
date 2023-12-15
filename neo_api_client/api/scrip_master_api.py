from neo_api_client import rest
from neo_api_client import settings
from neo_api_client.exceptions import ApiException


class ScripMasterAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def scrip_master_init(self, exchange_segment=None):
        URL = self.rest_client.configuration.get_url_details("scrip_master")
        header_params = {'Authorization': "Bearer " + self.rest_client.configuration.bearer_token}

        try:
            scrip_report = self.rest_client.request(url=URL, method='GET', headers=header_params).json()["data"]
            if exchange_segment:
                exchange_segment = settings.exchange_segment[exchange_segment]
                exchange_segment_csv = [file for file in scrip_report["filesPaths"] if exchange_segment.lower() in file.lower()]
                if exchange_segment_csv:
                    return exchange_segment_csv[0]
                else:
                    return {"Error": "Exchange segment not found"}
            return scrip_report
        except ApiException as ex:
            return {"error": ex}
