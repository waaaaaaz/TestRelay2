# coding: utf-8

from base import Base


class MySQLCase(Base):

    def __init__(self, case_unit, params):
        super(MySQLCase, self).__init__(case_unit, params)

    def exe(self):
        pass

    def get_params(self):
        pass



