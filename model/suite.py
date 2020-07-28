# coding: utf-8

from copy import deepcopy
import importlib

from test_relay.timing import Timing
from test_relay.txt import TXT
from test_relay.mapping.case_class import CASE_CLASS_MAPPING


class Suite(object):

    def __init__(self, case_file, global_params, tags_list):
        self.global_params = global_params
        self.exe_tags = tags_list
        self.raw_case = TXT.read_json_file(case_file)
        self.name = self.raw_case['name']
        self.desc = self.raw_case['desc']
        self.case_tags = self.raw_case['tag']
        self.__timing = Timing()
        self.time_suffix = self.__timing.current_time_suffix()
        self.params = self.__update_params()
        self.e2e = self.raw_case['e2e']

    def __update_params(self):
        params = deepcopy(self.global_params)
        for k, v in self.raw_case['session_params'].items():
            params[k] = v

        for k, v in self.raw_case['session_suffix_params'].items():
            params[k] = v + self.time_suffix

        return params

    def __case_class(self, case_type):
        module_name = "TestRelay2.0.model.case"
        new_module = importlib.import_module(module_name, package=None)
        class_ = getattr(new_module, CASE_CLASS_MAPPING[case_type])
        return class_

    def exe(self):
        # print self.exe_tags
        if self.exe_tags is None:
            params = deepcopy(self.params)
            for e in self.e2e:
                case_type = e["type"]
                case = self.__case_class(case_type)(e, params)
                case.exe()
                params = case.get_params()
        print ("done")


if __name__ == "__main__":
    file = "/Users/wangchao99/Code/meituan/nlp/qa/TestRelay2.0/test_suite/demo_01.json"
    p = {"test": "test"}
    t = {"tag": "tag"}
    s = Suite(file, p, t)
