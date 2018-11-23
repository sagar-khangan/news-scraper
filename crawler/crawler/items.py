# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):

    raw = scrapy.Field()
    url = scrapy.Field()
    short_title = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
