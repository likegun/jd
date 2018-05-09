# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommodityItem(scrapy.Item):
    pics = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    commentCount = scrapy.Field()
    shopUrl = scrapy.Field()
    shopName = scrapy.Field()
    pass
