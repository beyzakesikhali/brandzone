# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonprojectItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    brand=scrapy.Field()
    image = scrapy.Field()
    barcode = scrapy.Field()
    url = scrapy.Field()
    pass
