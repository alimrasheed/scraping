# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import TestItem
from scrapy.http import FormRequest


class AstroSpider(scrapy.Spider):
    name = 'knipex' 

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
                yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):

        relative_url = response.xpath('//img[@class="prod_zoom"]/@src').extract_first()
        absolute_url = response.urljoin(relative_url)
        no = response.xpath("//*[contains(th, 'No.')]/td/text()").extract()
        ean = response.xpath("//*[contains(th, 'EAN')]/td/text()").extract()
        plier = response.xpath("//*[contains(th, 'Pliers')]/td/text()").extract()
        handle = response.xpath("//*[contains(th, 'Handles')]/td/text()").extract()
        roa = response.xpath("//*[contains(th, 'Range of Application')]/td/text()").extract()
        cap = response.xpath("//*[contains(th, 'Capacity')]/td/text()").extract()
        awg = response.xpath("//*[contains(th, 'AWG')]/td/text()").extract()
        noc = response.xpath("//*[contains(th, 'Number of crimping positions')]/td/text()").extract()
        length = response.xpath('//*[@alt="Length"]/../../td/text()').extract()
        weight = response.xpath('//*[@alt="Net weight"]/../../td/text()').extract()
        stripping_cap = response.xpath("//*[contains(th, 'Stripping capacities in square millimetres')]/td/text()").extract()
        head = response.xpath("//*[contains(th, 'Head ')]/td/text()").extract()
        c1 = response.xpath("//*[@alt='Cutting capacity copper cable, multiple-stranded (diameter)']/../../td/text()").extract()
        c2 = response.xpath("//*[@alt='Cutting capacity copper cable, multiple-stranded']/../../td/text()").extract()
        stripping_cap_dia = response.xpath("//*[contains(th, 'Stripping capacities (diameter) ')]/td/text()").extract()
        capacity_square = response.xpath("//*[contains(th, 'Capacity square')]/td/text()").extract()
        Capacity_triangular = response.xpath("//*[contains(th, 'Capacity triangular')]/td/text()").extract()
        Capacity_double_bit_key = response.xpath("//*[contains(th, 'Capacity double-bit key')]/td/text()").extract()
        Capacity_half_moon = response.xpath("//*[contains(th, 'Capacity half-moon')]/td/text()").extract()
        Capacity_step_like_square = response.xpath("//*[contains(th, 'Capacity step-like square')]/td/text()").extract()
        Stripping_capacities = response.xpath("//*[contains(th, 'Stripping capacities ')]/td/text()").extract()
        Stripping_capacities_round_cable = response.xpath("//*[contains(th, 'Stripping capacities round cable (diameter) ')]/td/text()").extract()
        Wire_stripping_value_for_conductors_and_strands = response.xpath('//*[contains(th, "Stripping capacities round cable (diameter) ")]/td/text()').extract()
        Wire_stripping_value_for_data_cable = response.xpath("//*[contains(th, 'Wire stripping value for data cable')]/td/text()").extract()        
        Stripping_capacities_for_coax_cable = response.xpath("//*[contains(th, 'Stripping capacities for coax cable (diameter) ')]/td/text()").extract()
        Cutting_capacities_soft_wire = response.xpath("//*[contains(th, 'Cutting capacities soft wire (diameter)')]/td/text()").extract()
        Cutting_capacities_medium_hard_wire = response.xpath("//*[contains(th, 'Cutting capacities medium hard wire (diameter)')]/td/text()").extract()
        Cutting_capacities_hard_wire = response.xpath("//*[contains(th, 'Cutting capacities hard wire (diameter)')]/td/text()").extract()
        Cutting_edge_length_mm	= response.xpath("//*[contains(th, 'Cutting edge length mm')]/td/text()").extract()
        B1 = response.xpath("//*[contains(th, 'B1')]/td/text()").extract()
        B2 = response.xpath("//*[contains(th, 'B2')]/td/text()").extract()
        B3 = response.xpath("//*[contains(th, 'B3')]/td/text()").extract()
        Capacities_for_nuts1 = response.xpath(".//*[@alt='Capacities for nuts']/../../td/text()").extract()
        Capacities_for_nuts2 = response.xpath(".//*[@alt='Capacities for nuts']/../../td/text()").extract()
        Capacity_for_pipes_inches = response.xpath(".//*[@alt='Capacity for pipes, inches (diameter)']/../../td/text()").extract()
        Capacity_for_pipes_diameter = response.xpath('.//*[@alt="Capacities for pipes (diameter)"]/../../td/text()').extract()
        Style1 = response.xpath(".//*[contains(th, 'Style')]/td/text()").extract()
        Style2 = response.xpath(".//*[contains(th, 'Style')]/td/text()").extract()
        Size_of_bore = response.xpath("//*[contains(th, 'Size of bore')]/td/text()").extract()
        Tips_diameter = response.xpath("//*[contains(th, 'Tips (diameter)')]/td/text()").extract()
        L3 = response.xpath("//*[contains(th, 'L3')]/td/text()").extract()
        T1 = response.xpath("//*[contains(th, 'T1')]/td/text()").extract()
        W3 = response.xpath("//*[contains(th, 'W3')]/td/text()").extract()
        W4 = response.xpath("//*[contains(th, 'W4')]/td/text()").extract()
        T2 = response.xpath("//*[contains(th, 'T2')]/td/text()").extract()
        Insulation_standard = response.xpath("//*[contains(th, 'Insulation standard')]/td/text()").extract()	
        Nominal_size = response.xpath("//*[contains(th, 'Nominal size')]/td/text()").extract()
        L4 = response.xpath("//*[contains(th, 'L4')]/td/text()").extract()
        dimension_angle = response.xpath("//*[@alt='Dimensions angle']/../../td/text()").extract()
        Blade_length = response.xpath("//*[contains(th, 'Blade length')]/td/text()").extract()
        Radius = response.xpath("//*[contains(th, 'Radius')]/td/text()").extract() 
        
        
        loader = ItemLoader(item=TestItem(), selector=response)

        #loader.add_value('img_url', relative_url)
        loader.add_value('img', absolute_url)
        loader.add_value('No', no)
        loader.add_value('EAN', ean)
        loader.add_value('Pliers', plier)
        loader.add_value('Handles', handle)
        loader.add_value('Range_of_Application', roa)
        loader.add_value('Capacity', cap)
        loader.add_value('AWG', awg)
        loader.add_value('No_of_crimping_positions', noc)
        loader.add_value('Length', length)
        loader.add_value('Weight', weight)
        loader.add_value('Stripping_capacities_sq_mm',stripping_cap)
        loader.add_value('Head', head)
        loader.add_value('Cutting_capacity_copper_cable_multiple_stranded_diameter',c1)
        loader.add_value('Cutting_capacity_copper_cable_multiple_stranded', c2)
        loader.add_value('Stripping_capacities_diameter', stripping_cap_dia)
        loader.add_value('Capacity_square', capacity_square)
        loader.add_value('Capacity_triangular', Capacity_triangular)        
        loader.add_value('Capacity_double_bit_key', Capacity_double_bit_key)
        loader.add_value('Capacity_half_moon', Capacity_half_moon)
        loader.add_value('Capacity_step_like_square', Capacity_step_like_square)
        loader.add_value('Stripping_capacities',Stripping_capacities)
        loader.add_value('Stripping_capacities_round_cable',Stripping_capacities_round_cable)
        loader.add_value('Wire_stripping_value_for_conductors_and_strands',Wire_stripping_value_for_conductors_and_strands)
        loader.add_value('Wire_stripping_value_for_data_cable',Wire_stripping_value_for_data_cable)
        loader.add_value('Stripping_capacities_for_coax_cable',Stripping_capacities_for_coax_cable)
        loader.add_value('Cutting_capacities_soft_wire', Cutting_capacities_soft_wire)
        loader.add_value('Cutting_capacities_medium_hard_wire',Cutting_capacities_medium_hard_wire)
        loader.add_value('Cutting_capacities_hard_wire',Cutting_capacities_hard_wire)
        loader.add_value('Cutting_edge_length_mm', Cutting_edge_length_mm)
        loader.add_value('B1', B1)
        loader.add_value('B2', B2)
        loader.add_value('B3', B3)
        loader.add_value('Capacities_for_nuts1',Capacities_for_nuts1)
        loader.add_value('Capacities_for_nuts2',Capacities_for_nuts2)
        loader.add_value('Capacity_for_pipes_inches', Capacity_for_pipes_inches)
        loader.add_value('Capacity_for_pipes_diameter', Capacity_for_pipes_diameter)
        loader.add_value('Style1', Style1)
        loader.add_value('Style2', Style2)
        loader.add_value('Size_of_bore', Size_of_bore)
        loader.add_value('Tips_diameter', Tips_diameter)
        loader.add_value('L3', L3)
        loader.add_value('T1', T1)
        loader.add_value('W3', W3)
        loader.add_value('W4', W4)
        loader.add_value('T2', T2)
        loader.add_value('L4', L4)
        loader.add_value('Insulation_standard', Insulation_standard)
        loader.add_value('Nominal_size', Nominal_size)
        loader.add_value('dimension_angle',dimension_angle)
        loader.add_value('Blade_length', Blade_length)
        loader.add_value('Radius', Radius)



        
        yield loader.load_item()