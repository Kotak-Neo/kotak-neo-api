from __future__ import absolute_import

import json
import logging
import six
import base64
import jwt
from neo_api_client.exceptions import ApiValueError
from neo_api_client.urls import SESSION_UAT_BASE_URL, SESSION_PROD_BASE_URL, UAT_BASE_URL, PROD_BASE_URL
from neo_api_client.settings import UAT_URL, PROD_URL, neo_fin_key, live_fin_key


class NeoUtility:
    """
        Project configuration (or) Params to be passed here
    """

    def __init__(self, consumer_key=None, consumer_secret=None, host=None, access_token=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.host = host
        self.base64_token = self.convert_base64()
        self.bearer_token = access_token
        self.view_token = None
        self.sid = None
        self.userId = None
        self.edit_token = None
        self.edit_sid = None
        self.edit_rid = None
        self.serverId = None

    def convert_base64(self):
        """The Base64 Token Generation.
        This function will generate the Base64 Token this will be used to generate the Bearer Token.
        Return the Token in a String Format
        """
        base64_string = str(self.consumer_key) + ":" + str(self.consumer_secret)
        base64_token = base64_string.encode("ascii")
        base64_bytes = base64.b64encode(base64_token)
        final_base64_token = base64_bytes.decode("ascii")
        return final_base64_token

    def extract_userid(self, view_token):
        if not view_token:
            raise ApiValueError(
                "View Token hasn't been Generated Kindly Call the Login Function and Try to Generate OTP")
        decode_jwt = jwt.decode(view_token, options={"verify_signature": False})
        userid = decode_jwt.get("sub")
        self.userId = userid
        return userid

    def get_domain(self, session_init=False):
        host_list = ["prod", "uat"]
        if self.host.lower().strip() in host_list:
            if session_init:
                if self.host.lower().strip() == 'prod':
                    base_url = SESSION_PROD_BASE_URL
                else:
                    base_url = SESSION_UAT_BASE_URL
            else:
                if self.host.lower().strip() == 'prod':
                    base_url = PROD_BASE_URL
                else:
                    base_url = UAT_BASE_URL

            return base_url
        else:
            raise ApiValueError("Either UAT or PROD in Environment accepted")

    def get_url_details(self, api_info):
        domain_info = self.get_domain()
        if self.host.lower().strip() == 'prod':
            domain_info += PROD_URL.get(api_info)
        else:
            domain_info += UAT_URL.get(api_info)

        return domain_info

    def get_neo_fin_key(self):
        if self.host.lower().strip() == 'prod':
            fin_key = live_fin_key
        else:
            fin_key = neo_fin_key

        return fin_key
