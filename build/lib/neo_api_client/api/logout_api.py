from neo_api_client import rest
from neo_api_client.exceptions import ApiException


class LogoutAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def logging_out(self):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "accept": "application/json",
                         "Content-Type": "application/x-www-form-urlencoded"}

        URL = self.api_client.configuration.get_url_details("logout")

        try:
            logout_report = self.rest_client.request(
                url=URL, method='POST',
                headers=header_params
            )
            return {"data": logout_report.text}
        except ApiException as ex:
            return {"error": ex}
