import scrapy
from scrapy.loader import ItemLoader
import sys
sys.path.append('/home/alim/virtual_workspace/demo_project/demo_project')
from ..items import QuoteItem


class GoodReadsSpider(scrapy.Spider):
    #identity
    name="goodreads"

    start_urls= [
        'https://www.goodreads.com/quotes?page=1'
    ]

    #Response
    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            loader= ItemLoader(item=QuoteItem(), selector=quote, response=response)
            loader.add_xpath('text', ".//div[@class='quoteText']/text()[1]")
            loader.add_xpath('author', ".//div[@class='quoteText']/child::span/text()[1]")
            loader.add_xpath('tags', ".//div[@class='greyText smallText left']/a/text()")
            yield loader.load_item()
            
    
        next_page = response.css("a.next_page::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)