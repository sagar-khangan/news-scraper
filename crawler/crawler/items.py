import scrapy


class CrawlerItem(scrapy.Item):

    """
    Scrapped Item fields to be extracted

    """
    raw = scrapy.Field()
    url = scrapy.Field()
    short_title = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    domain = scrapy.Field()
