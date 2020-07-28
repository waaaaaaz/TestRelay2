# coding: utf-8

import time

from base import Base


class WaitCase(Base):

    def __init__(self, case_unit, params):
        super(WaitCase, self).__init__(case_unit, params)
        self.duration = self.case_unit["duration"]

    def exe(self):
        # print "准备等待10秒钟"
        time.sleep(self.duration)

    def get_params(self):
        return self.params

