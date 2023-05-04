import json

import requests
from neo_api_client import rest
from neo_api_client import req_data_validation


class LoginAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        self.base64_token = api_client.configuration.base64_token
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def session_init(self):
        """
        Initialize a session by sending a POST request to the specified URL with OAuth2 token.

        :param URL: The URL to send the POST request to
        :type URL: str
        :return: The response from the REST client's request
        :rtype: requests.Response
        """
        header_params = {'Authorization': "Basic " + self.base64_token}
        body_params = {
            "grant_type": "client_credentials",
        }
        URL = self.api_client.configuration.get_domain(session_init=True) + "oauth2/token"
        session_init = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        if session_init.ok:
            json_resp = json.loads(session_init.text)
            self.api_client.configuration.bearer_token = json_resp.get("access_token")
            return json_resp
        else:
            return json.dumps({"data": {"Code": session_init.status_code, "Message": "Error occurred to initialise the "
                                                                                     "session"}})

    def generate_view_token(self, password, mobilenumber=None, userid=None, pan=None):
        """
        This function generates a view token for a given mobile number and password.

        Args:
            URL (str): Base URL of the API.
            mobileNumber (str): Mobile number of the user.
            password (str): Password of the user.

        Returns:
            dict: API response with a view token.
            :param password:
            :param pan:
            :param userid:
            :param mobilenumber:
        """
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        body_params = req_data_validation.login_params_validation(mobilenumber=mobilenumber, userid=userid, pan=pan)
        body_params["password"] = password
        self.api_client.configuration.login_params = body_params
        URL = self.api_client.configuration.get_url_details("view_token")
        generate_view_token = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        if 200 <= generate_view_token.status_code <= 299:
            view_token_json_resp = json.loads(generate_view_token.text)
            if mobilenumber and not mobilenumber.startswith("+"):
                view_token_json_resp["message"] = "since no country code found we have appended +91 as the default " \
                                                  "country code. Please change it to the correct code if your mobile " \
                                                  "number is not of indian number "
            self.api_client.configuration.view_token = view_token_json_resp.get("data").get("token")
            self.api_client.configuration.sid = view_token_json_resp.get("data").get("sid")
            return view_token_json_resp
        else:
            view_token_json_resp = json.loads(generate_view_token.text)
            if mobilenumber and not mobilenumber.startswith("+"):
                view_token_json_resp["Note"] = "since no country code found we have appended +91 as the default " \
                                               "country code. Please change it to the correct code if your mobile " \
                                               "number is not of indian number "
            return view_token_json_resp

    def generate_otp(self):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        userId = self.api_client.configuration.extract_userid(self.api_client.configuration.view_token)
        body_params = {
            "userId": userId,
            "sendEmail": True,
            "isWhitelisted": True
        }
        URL = self.api_client.configuration.get_url_details("generate_otp")
        output_fo = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        return output_fo.text

    def login_2fa(self, OTP):
        params = self.api_client.configuration.login_params
        body_params = {}
        if 'mobileNumber' in params and len(str(OTP)) == 6:
            body_params['mobileNumber'] = str(params['mobileNumber'])
            body_params['mpin'] = str(OTP)
        elif 'pan' in params and len(str(OTP)) == 6:
            body_params['pan'] = str(params['pan'])
            body_params['mpin'] = str(OTP)
        else:
            body_params['userId'] = str(self.api_client.configuration.userId)
            body_params['otp'] = str(OTP)
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "sid": self.api_client.configuration.sid,
                         "Auth": self.api_client.configuration.view_token}
        URL = self.api_client.configuration.get_url_details("edit_token")
        login_resp = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        edit_token_json_resp = json.loads(login_resp.text)
        if 'error' not in edit_token_json_resp:
            self.api_client.configuration.edit_token = edit_token_json_resp.get("data").get("token")
            self.api_client.configuration.edit_sid = edit_token_json_resp.get("data").get("sid")
            self.api_client.configuration.edit_rid = edit_token_json_resp.get("data").get("rid")
            self.api_client.configuration.serverId = edit_token_json_resp.get("data").get("hsServerId")
        return edit_token_json_resp
