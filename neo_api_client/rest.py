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
        assert method in ['GET','POST','PUT','DELETE','HEAD','OPTIONS','PATCH']

        headers = headers or {}

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
        
        #add query_params if any required
        if query_param:
            url += '?' + urlencode(query_param)

        request_body = {}

        json_in_content = re.search('json',headers['Content-Type'],re.IGNORECASE)
        urlencoding_in_content = re.search('x-www-form-urlencoded',headers['Content-Type'],re.IGNORECASE)

        if json_in_content and body:
            request_body = json.dumps(body)
        elif urlencoding_in_content and body:
            request_body['jData'] = json.dumps(body)
        elif not json_in_content and not urlencoding_in_content:
            raise ValueError('Expected json/x-www-form-urlencoded in Content-Type')

        
        response = requests.request(method,url,headers=headers,data=request_body)
        return response
        


