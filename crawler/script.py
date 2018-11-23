import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())

process.crawl('newscrawl', domain=sys.argv[1])
process.start()
