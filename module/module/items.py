# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InfoItem(scrapy.Item):
    okr = scrapy.Field()
    napryam = scrapy.Field()
    allCount = scrapy.Field()
    budgetCount = scrapy.Field();
    mark = scrapy.Field()
