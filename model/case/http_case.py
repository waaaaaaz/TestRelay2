# coding: utf-8

import json
from copy import deepcopy

from base import Base
from test_relay.common.http import HttpLibrary


class HttpCase(Base):

    def __init__(self, case_unit, params):
        super(HttpCase, self).__init__(case_unit, params)
        print(self.case_unit["request"])
        self.request_headers = self.case_unit["request"]["headers"]
        self.request_url = self.case_unit["request"]["url"]
        self.request_method = self.case_unit["request"]["method"]
        if "payload" in self.case_unit["request"].keys():
            self.request_payload = self.case_unit["request"]["payload"]
        else:
            self.request_payload = None
        self.response = self.__response()
        print (self.response)
        self.response_status_code = self.response[0]
        if "dynamic_params" in self.case_unit.keys():
            self.dynamic_params_pattern = self.case_unit["dynamic_params"]
            self.dynamic_params = self.__dynamic_params()
        if "assert" in self.case_unit.keys():
            self.assert_pattern = self.case_unit["assert"]

    def case_assert(self):
        if "status_code" in self.assert_pattern.keys():
            assert self.response_status_code == self.assert_pattern["status_code"]
        if "check" in self.assert_pattern.keys():
            print self.desc
            for k, v in self.assert_pattern["check"].items():
                print k
                print v
                if not isinstance(v, basestring):
                    assert self.__check_jpath_value(k) == v
                else:
                    if not v.startswith("{*"):
                        if v.isdigit():
                            assert self.__check_jpath_value(k) == int(v)
                        else:
                            assert self.__check_jpath_value(k) == v

    def __check_jpath_value(self, check_key_as_jpath):
        response = json.loads(deepcopy(self.response[2]))
        return self.jpath_value(response, check_key_as_jpath)

    def db_assert(self):
        pass

    def exe(self):
        self.case_assert()
        self.db_assert()

    def __dynamic_params(self):
        dynamic_params = {}
        print self.response[2]
        response = json.loads(self.response[2])
        for k, v in self.dynamic_params_pattern.items():
            dynamic_params[k] = self.jpath_value(response, v)
        return dynamic_params

    def get_params(self):
        params = deepcopy(self.params)
        for k, v in self.dynamic_params.items():
            params[k] = v
        return params

    def __response(self):
        http_client = HttpLibrary()
        return http_client \
            .build_headers(self.request_headers) \
            .build_payload(self.request_payload) \
            .build_url(self.request_url) \
            .request(self.request_method)
