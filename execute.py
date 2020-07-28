# coding: utf-8

from multiprocessing import Pool
from copy import deepcopy

from test_relay.setting import *
from test_relay.model.suite import Suite
from test_relay.timing import Timing


class Execute(object):

    def __init__(self, sys, env, tags_list, case_list):
        self.sys = sys
        self.env = env
        self.tags_list = tags_list
        self.case_list = case_list
        self.global_params = self.__get_global_params()
        self.__timing = Timing()
        self.execute_id = "exe_id_" + self.__timing.current_time_id()


    def __get_global_params(self):
        pattern = self.sys.upper() + "_" + self.env.upper() + "_"
        cookie_pattern = "COOKIE"
        global_params = {}
        for k, v in globals().items():
            if k.startswith(pattern):
                print (k)
                if k.endswith(cookie_pattern):
                    global_params[k.split(pattern)[1].lower()] = v.replace('"', '\"')
                    print (v.replace('"', '\"'))
                else:
                    global_params[k.split(pattern)[1].lower()] = v
        return global_params

    def __concurrency(self, size):
        pool = Pool(processes=size)
        pool.apply(self.__execute_one_case, self.case_list)
        pool.close()
        pool.join()

    def __execute_one_case(self, case_file):
        global_params = deepcopy(self.global_params)
        tags_list = deepcopy(self.tags_list)
        test_suite = Suite(case_file, global_params, tags_list)
        test_suite.exe()

    def test(self):
        for case_file in self.case_list:
            self.__execute_one_case(case_file)

