from crawler import settings
from readability.readability import Document


class CrawlerPipeline(object):

    def process_item(self, item, spider):
        response = item['raw']
        html = response.body
        item['short_title'] = Document(html).short_title()
        item['summary'] = Document(html).summary()
        item['title'] = Document(html).title()
        item['category'] = response.xpath(settings.CATEGORY_PATTERN).extract_first()
        item['content'] = Document(html).content()
        item['author'] = response.xpath(settings.AUTHOR_PATTERN).extract_first()
        del item['raw']
        return item
