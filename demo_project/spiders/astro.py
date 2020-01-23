# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import TestItem


class AstroSpider(scrapy.Spider):
    name = 'astro'
    
    def start_requests(self):

        urls = ['https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1534&artID=93',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1535&artID=97',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1373&groupID=1422&artID=212',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=2068&artID=32632',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1557&artID=2340',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1557&artID=2353',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1333&artID=3601',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1513&artID=3610',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1431&artID=3572',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1431&artID=3592',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1432&artID=3596',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1435&artID=3638',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1336&groupID=1346&artID=1213',
        
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        #item = TestItem()

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