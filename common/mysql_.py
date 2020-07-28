# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.sql import text


class MySQLLibrary(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(MySQLLibrary, cls).__new__(cls)
        return cls._instance

    def __init__(self, mysql_connection):
        self.engine = create_engine(mysql_connection, encoding="utf-8", echo=run_debug.debug)
        self.conn = self.engine.connect()

    def execute(self, sql_str):
        sql = text(sql_str)
        # print("数据库查询语句：")
        # print(sql)
        result = self.conn.execute(sql)
        if sql_str.lower().startswith("select"):
            row = result.fetchone()
            # print("查询数据库的结果，取第1行记录显示.....")
            # print(row)
            # 数据库写入耗时，有可能暂时取不到值，导致 case 失败
            assert row
            for rst in row:
                # print(rst)
                return rst
            # return result.fetchall()[0][0]
        else:
            return None
