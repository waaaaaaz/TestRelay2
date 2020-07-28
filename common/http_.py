# coding: utf-8

import requests

from mapping.http_method import HTTP_METHOD


class HttpLibrary(object):

    def __init__(self):
        self.headers = {'content-type': 'application/json;charset=UTF-8'}
        self.payload = {}
        self.url = None

    def build_headers(self, headers):
        for k, v in headers.items():
            self.headers[k] = v
        return self

    def build_payload(self, payload):
        if payload is None:
            return self
        if isinstance(payload, dict):
            for k, v in payload.items():
                self.payload[k] = v
            return self
        if isinstance(payload, list):
            self.payload = payload
            return self

    def build_url(self, url_str):
        self.url = url_str
        return self

    def request(self, method_str):
        func_name = HTTP_METHOD[method_str.lower()]
        return getattr(self, func_name)()

    def get_request(self):
        response = requests.get(url=self.url, headers=self.headers,params=self.payload)
        return response.status_code, response.headers, response.text

    def post_request(self):
        response = requests.post(url=self.url, json=self.payload, headers=self.headers)
        return response.status_code, response.headers, response.text

    def post_text_request(self):
        response = requests.post(url=self.url, data=self.payload, headers=self.headers)
        return response.status_code, response.headers, response.text

    def put_request(self):
        response = requests.put(url=self.url, json=self.payload, headers=self.headers)
        return response.status_code, response.headers, response.text

    def delete_request(self):
        response = requests.delete(url=self.url, json=self.payload, headers=self.headers)
        return response.status_code, response.headers, response.text
