# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import TestItem
from scrapy.http import FormRequest


class AstroSpider(scrapy.Spider):
    name = 'astro'

    start_urls= ['https://www.knipex.com/index.php?id=1216&L=1&isMobile=']

    def parse(self, response):
        #item = TestItem()
        module_list = ['97 33 01',
'97 51 10',
'97 52 36',
'97 53 04',
'97 53 14',
'11 02 0160',
'12 62 180',
'13 82 200',
'16 40 150',
'00 11 01',
'16 95 01 SB',
'68 01 160',
'68 01 180',
'68 01 200',
'68 01 280',
'70 01 125',
'70 01 160',
'70 02 160',
'70 02 180',
'71 01 200',
'71 72 460',
'86 01 250',
'86 03 125',
'86 03 150',
'86 03 180',
'86 03 250',
'86 03 400',
'87 01 150',
'87 01 180',
'87 01 250',
'88 01 250',
'88 01 300',
'48 11 J1',
'48 11 J2',
'48 21 J21',
'48 21 J31',
'49 11 A2',
'49 21 A21',
'25 02 160',
'26 12 200',
'26 16 200',
'26 22 200',
'03 01 0180',
'03 02 0180',
'09 02 0240',
'98 52',
'98 55',
'00 21 20',
'03 06 0180',
'03 06 0200',
'11 06 0160',
'13 86 200',
'70 06 160',
'70 06 180',
'95 16 165',
'95 16 200',
'95 11 165',
'95 12 165',
'95 12 200',
'95 31 250',]
        for li in module_list:         
            return FormRequest.from_response(response=response, formcss="form", formdata={
                'search-mini':li
            }, callback = self.after_search)

    def after_search(self, response):

        relative_url = response.xpath('//img[@class="prod_zoom"]/@src').extract_first()
        absolute_url = response.urljoin(relative_url)
        ean = response.css("tr:nth-child(2) td").css("::text").get()
        handle = response.css("tr:nth-child(3) td").css("::text").extract_first()
        blade_length = response.css("tr:nth-child(5) td").css("::text").extract_first()

        loader = ItemLoader(item=TestItem(), selector=response)

        loader.add_value('img_url', relative_url)
        loader.add_value('img', absolute_url)
        loader.add_value('EAN', ean)
        loader.add_value('Handle', handle)
        loader.add_value('Blade_length', blade_length)

        yield loader.load_item()