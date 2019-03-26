#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy;
from module.items import *

class TestSpider (scrapy.Spider):
  name='TestSpider'
  start_urls=['https://abit-poisk.org.ua/rate2010/univer/234']

  def parse(self, response):
    trs = response.css('tr')

    for tr in trs:
      it = InfoItem()
      it['okr'] = tr.css(':nth-child(1)::text').get().strip()
      it['napryam'] = tr.css(':nth-child(2)::text').get().strip()
      it['allCount'] = tr.css(':nth-child(4)::text').get().strip()
      it['budgetCount'] = tr.css(':nth-child(5)::text').get().strip()
      it['mark'] = tr.css(':nth-child(6)::text').get().strip()
      yield it