# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    product_url = scrapy.Field()
    product_title = scrapy.Field()
    product_sub_title = scrapy.Field()
    product_price = scrapy.Field()
    model_number = scrapy.Field()
    images = scrapy.Field()
    fetched_at = scrapy.Field()
    internet_no=scrapy.Field()
    pass
