import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import CrawlerItem


class NewsSpider(scrapy.spiders.Spider):
    name = "news"
    start_url = []

    """
    Spider to save html of link
    
    """

    def __init__(self,*args,**kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.start_url = kwargs.get('domain')

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


class NewsCrawlSpider(CrawlSpider):
    """
    Spider to crawl websites

    """
    name = "newscrawl"
    start_urls = []

    rules = (

        # Rules to crawl only specific paths
        Rule(LinkExtractor(allow=('news',)), callback='parse_item'),
        Rule(LinkExtractor(allow=('weather',)), callback='parse_item'),
        Rule(LinkExtractor(allow=('travel',)), callback='parse_item'),
        Rule(LinkExtractor(allow=('science',)), callback='parse_item'),
        Rule(LinkExtractor(allow=('fashion',)), callback='parse_item'),

        # Rule to crawl all links
        # Rule(LinkExtractor(allow=(r".*",)), callback='parse_item'),
    )

    def __init__(self,*args,**kwargs):

        super(NewsCrawlSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('domain')]

    def parse_item(self, response):
        self.logger.info('Response for page %s', response.url)
        item = CrawlerItem()
        item['url'] = response.url
        item['raw'] = response
        return item
