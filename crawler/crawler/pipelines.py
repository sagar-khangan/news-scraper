from crawler import settings
from readability.readability import Document
import pymongo
from scrapy.log import logger
import tldextract

class CrawlerPipeline(object):

    def process_item(self, item, spider):
        logger.info("Extracting content for %s" %item['url'])
        response = item['raw']
        html = response.body
        item['short_title'] = Document(html).short_title()
        item['summary'] = Document(html).summary()
        item['title'] = Document(html).title()
        item['category'] = response.xpath(settings.CATEGORY_PATTERN).extract_first()
        item['content'] = Document(html).content()
        item['author'] = response.xpath(settings.AUTHOR_PATTERN).extract_first()
        item['domain'] = '.'.join(tldextract.extract(response.url)[-2:])
        del item['raw']
        return item



class MongoPipeline(object):

    collection_name = settings.MONGO_COLLECTION

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,ssl=True)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        logger.info("Inserting %s into MongoDB" % item['url'])
        self.db[self.collection_name].insert_one(dict(item))
        return item

