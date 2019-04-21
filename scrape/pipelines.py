# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrape.settings import mongo_host, mongo_port, \
    mongo_user, mongo_passwd, \
    mongo_db_name, mongo_db_collection


class ScrapePipeline(object):

    def __init__(self):
        client = pymongo.MongoClient("mongodb://%s:%s@%s:%d/admin" % (mongo_user, mongo_passwd, mongo_host, mongo_port))
        db = client[mongo_db_name]
        self.post = db[mongo_db_collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
