import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.log import logger


if __name__ == '__main__':
    try:
        process = CrawlerProcess(get_project_settings())
        logger.info("Processing domain '%s' ... " % (sys.argv[1]))
        process.crawl('newscrawl', domain=sys.argv[1])
        process.start()
        logger.info("Processing completed ...")
    except Exception as e:
        logger.exception("Exception {} occured ...".format(e))
