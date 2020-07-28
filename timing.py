# coding: utf-8

from datetime import datetime
import time


class Timing(object):
    LogFormat = "%Y%m%d-%H%M%S"
    OutputFormat = "%Y%m%d%H%M%S"

    def __init__(self):
        self.current_time = datetime.now()

    def current_time_suffix(self):
        return self.current_time.strftime("_%Y%m%d_%H%M%S")

    def current_time_id(self):
        return self.current_time.strftime("%Y%m%d%H%M%S")

    def current_time(self):
        return self.current_time.strftime("%Y-%m-%d %H:%M:%S")

    def current_date(self):
        return self.current_time.strftime("%Y%m%d")

    @staticmethod
    def get_current_time_for_log():
        return time.strftime(Timing.LogFormat, time.localtime(time.time()))

    def get_current_time_for_output(self):
        return time.strftime(self.OutputFormat, time.localtime(time.time()))

    def get_current_time(self):
        return time.time()
