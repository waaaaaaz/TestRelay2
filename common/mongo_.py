# coding: utf-8

import pymongo


class MongoLibrary(object):
    def __init__(self, mongo_connection, db, collection):
        self.client = pymongo.MongoClient(mongo_connection)
        self.db = self.client[db]
        self.col = self.db[collection]

    def execute(self, query, single, display=None):
        if single:
            return self.__find_one(query, display)
        else:
            return self.__find(query, display)

    def __find(self, query, display):
        query_result = []
        result = self.col.find(query, display)
        for i in result:
            query_result.append(i)
        return query_result

    def __find_one(self, query, display):
        return self.col.find_one(query, display)
