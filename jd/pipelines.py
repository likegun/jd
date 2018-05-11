# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bootstrap.ConnectToMongodb import client

db = client.scrapy

class JdPipeline(object):
    def process_item(self, item, spider):
        return item

class InsertIntoMongodbPipeline(object):
    def process_item(self, item, spider):
        db.jdItems.insert_one({
            'pics': item['pics'],
            'price': item['price'],
            'name': item['name'],
            'commentCount': item['commentCount'],
            'shopUrl': item['shopUrl'],
            'shopName': item['shopName']
        })
        return item