import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import QuoteItem

class GoodReads(scrapy.Spider):
    name = 'goodreads'

    def requests(self):

        url = 'https://www.goodreads.com/quotes/page=2'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=QuoteItem, selector=quote, response=response)
            loader.add_xpath('text', ".//div[@class='quoteText']")
            loader.add_xpath('author', ".//div[@class='quoteText']/child::a")
            loader.add_xpath('text', ".//div[@class='greyText smallText left']")
            yield loader.load_item()

