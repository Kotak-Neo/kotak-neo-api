from __future__ import absolute_import

import json
import logging
import re
import requests
from six.moves.urllib.parse import urlencode
from neo_api_client.exceptions import ApiException


class RESTClientObject(object):
    """REST API Client

    This class is a client to perform requests to a REST API.

    Attributes:
        configuration (dict): configuration for the API client
    """

    def __init__(self, configuration):
        """
        Initialize the API client with a configuration dictionary.

        :param configuration: dictionary of configuration parameters
        """
        self.configuration = configuration

    def request(self, method, url, query_params=None, headers=None,
                body=None):
        """Perform a request to the REST API

        This method performs a request to the REST API using the provided parameters.

        :param method: HTTP request method (e.g. GET, POST, PUT)
        :param url: URL for the API endpoint
        :param query_params: (optional) query parameters for the API endpoint
        :param headers: (optional) headers for the API request
        :param body: (optional) request body for the API request
        :return: response from the API
        :raises: ApiException in case of a request error
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        headers = headers or {}

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            if method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body is not None:
                        request_body = json.dumps(body)
                    response = requests.post(url=url, headers=headers, data=request_body)
                elif re.search('x-www-form-urlencoded', headers['Content-Type'], re.IGNORECASE):
                    request_body = {}
                    if body is not None:
                        request_body["jData"] = json.dumps(body)
                    response = requests.post(url=url, headers=headers, data=request_body)
                else:
                    msg = """In-Valid Content-Type in the Header Parameters"""
                    raise ApiException(status=0, reason=msg)
            elif method in ['GET']:
                if query_params:
                    url += '?' + urlencode(query_params)
                response = requests.get(url=url, headers=headers)
            else:
                msg = """Cannot call the API with the provided HTTP Method"""
                raise ApiException(status=0, reason=msg)
        except Exception as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        # if not 200 <= response.status_code <= 299:
        #     raise ApiException(status=response.status_code, reason=response.reason, body=response.text)
        return response


