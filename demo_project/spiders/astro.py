# -*- coding: utf-8 -*-
import scrapy
from ..items import AstroItem
from scrapy.loader import ItemLoader


class AstroSpider(scrapy.Spider):
    name = 'astro'

    def start_requests(self):

        urls = ['https://www.astrotools.com/air-tools/drills-screwdriviers/3-8-reversible-air-drill-1-800rpm.html/',
        'https://www.astrotools.com/1-2-extra-heavy-duty-reversible-air-drill-500rpm.html/',
        'https://www.astrotools.com/industrial-1-4-air-die-grinder.html/',
        'https://www.astrotools.com/1-2-air-ratchet-wrench-50ft-lb-torque.html/',
        'https://www.astrotools.com/1-2-super-duty-impact-wrench-twin-hammer.html/',
        'https://www.astrotools.com/1-heavy-duty-air-impact-wrench-with-2-anvil.html/',
        'https://www.astrotools.com/1-heavy-duty-air-impact-wrench-with-6-anvil.html/',
        'https://www.astrotools.com/onyx-heavy-duty-long-barrel-air-hammer-with-4pc-chisels-250mm.html/',
        'https://www.astrotools.com/needle-scaler-flux-hammer-combo-4-400-blows-per-minute.html/'
        ]
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        loader = ItemLoader(item=AstroItem(), selector=response)
        url = response.xpath("/html/body/div[2]/div[1]/div[1]/img/@src")
        name = response.xpath('//*[@id="maincontent"]/div[1]/h1/span/text()').get()
        loader.add_value('product_image', url)
        loader.add_value('product_name', name)
        yield loader.load_item()