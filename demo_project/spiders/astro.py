# -*- coding: utf-8 -*-
import scrapy


class AstroSpider(scrapy.Spider):
    name = 'astro'
    allowed_domains = ['http://www.astrotools.com/']
    start_urls = ['http://http://www.astrotools.com//']

    def parse(self, response):
        pass
