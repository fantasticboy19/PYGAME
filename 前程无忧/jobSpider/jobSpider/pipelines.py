# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient as mc
from jobSpider.settings import *

class JobspiderPipeline(object):
    def __init__(self):
        self.host = MONGO_HOST
        self.port = MONGO_PORT
        self.client = mc(self.host, self.port)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def process_item(self, item, spider):
        if not isinstance(item, dict):
            item = dict(item)
        self.collection.insert_one(item)
        return item
