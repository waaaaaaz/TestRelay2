# coding: utf-8

import yaml
import os


class TXT(object):

    def __init__(self):
        pass

    @staticmethod
    def read_json_file(case_file):
        with open(case_file, 'r') as f:
            json_string = f.read()
            return yaml.safe_load(json_string)

    @staticmethod
    def make_dir(_dir):
        if not os.path.exists(_dir):
            os.makedirs(_dir)
