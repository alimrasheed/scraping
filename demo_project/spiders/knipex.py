# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import TestItem
from scrapy.http import FormRequest


class AstroSpider(scrapy.Spider):
    #name = 'knipex'

    def start_requests(self):
        urls= ['https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1299&groupID=1320&artID=20540',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1299&groupID=1301&artID=48',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1299&groupID=1305&artID=3927',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1299&groupID=1307&artID=3946',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1299&groupID=1307&artID=3962',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1363&groupID=1383&artID=932',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1363&groupID=2036&artID=32631',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1363&groupID=1392&artID=1001',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1813&groupID=2015&artID=32451',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1363&groupID=2374&artID=34773',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1470&artID=2210',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1470&artID=2218',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1470&artID=2228',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1470&artID=34167',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1472&artID=2248',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1472&artID=2261',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1472&artID=2285',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1472&artID=2294',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1473&artID=2380',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1367&groupID=1474&artID=20528',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1500&artID=35338',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1500&artID=34171',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1500&artID=30062',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1500&artID=2939',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1500&artID=2959',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=2175&artID=34161',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1501&artID=3006',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1501&artID=3021',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1501&artID=3041',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1506&artID=3214',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1368&groupID=1506&artID=3238',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1457&artID=1894',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1457&artID=1904',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1457&artID=1940',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1457&artID=1948',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1458&artID=1977',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1365&groupID=1458&artID=2013',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1336&groupID=1345&artID=1099',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1336&groupID=1346&artID=1157',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1555&artID=1181',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1336&groupID=1346&artID=1213',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1534&artID=93',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1535&artID=97',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1373&groupID=1422&artID=212',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&isMobile=',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=2068&artID=32632',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1557&artID=2340',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1557&artID=2353',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1333&artID=3601',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1324&groupID=1513&artID=3610',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1431&artID=3572',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1431&artID=3592',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1432&artID=3596',
        'https://www.knipex.com/index.php?id=1216&L=1&page=art_detail&isMobile=&parentID=1371&groupID=1435&artID=3638',]
        for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        relative_url = response.xpath('//img[@class="prod_zoom"]/@src').extract_first()
        absolute_url = response.urljoin(relative_url)
        ean = response.css("tr:nth-child(2) td").css("::text").get()
        handle = response.css("tr:nth-child(3) td").css("::text").extract_first()

        loader = ItemLoader(item=TestItem(), selector=response)

        #loader.add_value('img_url', relative_url)
        loader.add_value('img', absolute_url)
        loader.add_value('EAN', ean)
        loader.add_value('Handle', handle)

        yield loader.load_item()