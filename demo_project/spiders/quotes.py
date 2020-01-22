# -*- coding: utf-8 -*-
import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        all_div_quotes = response.xpath("//div[@class='quote']")

        items = QuoteItem()

        for quotes in all_div_quotes:
            text = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tags = quotes.css(".tag::text").extract()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items
