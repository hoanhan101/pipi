"""
    publisher.py - Publisher pushs sensor reading to PiHub 
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/09/18
"""

import requests

from config import url

class Publisher():
    def __init__(self, host=url):
        """
        Initialize a Publisher object.

        Params:
            host <str>: Target hostname

        Return:
            None
        """
        self.host = host

    def get(self, endpoint):
        """
        Call GET for a specific endpoint.

        Params:
            endpoint <str>: Endpoint

        Return:
            None
        """
        r_get = requests.get('{}/{}'.format(self.host, endpoint))
        print(r_get.status_code)
        print(r_get.json())

    def publish(self, endpoint, payload):
        """
        Publish sensors reading to a specific endpoint.

        Params:
            endpoint <str>: Endpoint
            payload <str>: Data payload

        Return:
            None
        """
        r_post = requests.post('{}/{}'.format(self.host, endpoint), json=payload)
        print(r_post.status_code)
        print(r_post.json())
