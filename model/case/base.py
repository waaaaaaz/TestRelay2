# coding: utf-8

from abc import abstractmethod, ABCMeta
from copy import deepcopy
import re
import json
import jsonpath_rw_ext as jp


class Base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, case_unit, params):
        self.params = params
        self.case_unit = self.__replace_params(case_unit)
        self.desc = self.case_unit["desc"]
        self.type = self.case_unit["type"]
        self.dynamic_params = {}

    def __replace_params(self, case_unit):

        str_case_unit = json.dumps(case_unit)

        pattern_prefix = "{{"
        pattern_suffix = "}}"
        pattern = pattern_prefix + "(.*?)" + pattern_suffix
        compiled = re.compile(pattern, re.S)
        items = list(set(re.findall(compiled, str_case_unit)))
        str_updated = deepcopy(str_case_unit)

        for i in items:
            if i in self.params.keys():
                if isinstance(self.params[i], int):
                    str_updated = re.sub(pattern_prefix + i + pattern_suffix,
                                         str(self.params[i]), str_updated)
                else:
                    if i == "cookie":
                        str_updated = re.sub(pattern_prefix + i + pattern_suffix,
                                             self.params[i].replace('"', '\\"'), str_updated)
                    else:
                        str_updated = re.sub(pattern_prefix + i + pattern_suffix,
                                             self.params[i], str_updated)

        return json.loads(str_updated)

    def jpath_value(self, payload, path_expression):
        r = jp.match1(path_expression, payload)
        return r

    def get_params(self):
        raise NotImplementedError

    def exe(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass
