import scrapy
#import sys
#sys.path.append('/home/alim/PycharmProjects/amazon/amazon/amazon')
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%211000%2Cn%3A28&page=2&qid=1579712266&ref=lp_28_pg_2'
        ]

    def parse(self, response):

        items = AmazonItem()

        title = response.css('.a-color-base.a-text-normal').extract_first()
        author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract_first()
        price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract_first()
        image_link = response.css('.s-image').css('::text').extract_first()

        items['title'] = title
        items['author'] = author
        items['price'] = price
        items['image_link'] = image_link
        
        yield items