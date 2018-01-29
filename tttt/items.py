# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TtttItem(scrapy.Item):
    # define the fields for your item here like:
    positionName = scrapy.Field()
    positionType = scrapy.Field()
    positionCount = scrapy.Field()
    positionLoction = scrapy.Field()
    positionTime = scrapy.Field()
    positionLink = scrapy.Field()
