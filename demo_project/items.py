# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

#For knipex

class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #img_url = scrapy.Field()
    img = scrapy.Field()
    EAN = scrapy.Field()
    Handle = scrapy.Field()


#For Astro
class AstroItem(scrapy.Item):
    product_image = scrapy.Field()
    product_name = scrapy.Field(
        output_processor = TakeFirst()
    )