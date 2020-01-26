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
    No = scrapy.Field()
    EAN = scrapy.Field()
    Pliers = scrapy.Field()
    Handles = scrapy.Field()
    Range_of_Application = scrapy.Field()
    Capacity = scrapy.Field()
    AWG = scrapy.Field()
    No_of_crimping_positions = scrapy.Field()
    Length = scrapy.Field()
    Weight = scrapy.Field()
    Stripping_capacities_sq_mm = scrapy.Field()
    Head = scrapy.Field()
    Cutting_capacity_copper_cable_multiple_stranded_diameter = scrapy.Field()
    Cutting_capacity_copper_cable_multiple_stranded = scrapy.Field()
    Stripping_capacities_diameter = scrapy.Field()
    Capacity_square = scrapy.Field()
    Capacity_triangular = scrapy.Field()
    Capacity_double_bit_key = scrapy.Field()
    Capacity_half_moon = scrapy.Field()
    Capacity_step_like_square = scrapy.Field()
    Stripping_capacities_round_cable = scrapy.Field()
    Stripping_capacities = scrapy.Field()
    Wire_stripping_value_for_conductors_and_strands = scrapy.Field()
    Wire_stripping_value_for_data_cable = scrapy.Field()
    Stripping_capacities_for_coax_cable = scrapy.Field()
    Cutting_capacities_soft_wire = scrapy.Field()
    Cutting_capacities_medium_hard_wire = scrapy.Field()
    Cutting_capacities_hard_wire = scrapy.Field()
    Cutting_edge_length_mm = scrapy.Field()
    B1 = scrapy.Field()
    B2 = scrapy.Field()
    B3 = scrapy.Field()
    Capacities_for_nuts1 = scrapy.Field()
    Capacities_for_nuts2 = scrapy.Field()
    Capacity_for_pipes_inches = scrapy.Field()
    Capacity_for_pipes_diameter = scrapy.Field()
    Style1 = scrapy.Field()
    Style2 = scrapy.Field()
    Size_of_bore = scrapy.Field()
    Tips_diameter = scrapy.Field()
    L3 = scrapy.Field()
    T1 = scrapy.Field()
    W3 = scrapy.Field()
    W4 = scrapy.Field()
    T2 = scrapy.Field()
    Insulation_standard = scrapy.Field()
    Nominal_size = scrapy.Field()
    L4 = scrapy.Field()
    dimension_angle = scrapy.Field()
    Blade_length = scrapy.Field()
    Radius = scrapy.Field()



#For Astro
class AstroItem(scrapy.Item):
    product_image = scrapy.Field()
    product_name = scrapy.Field(
        output_processor = TakeFirst()
    )