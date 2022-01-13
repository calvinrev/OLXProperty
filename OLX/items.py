# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    
    property_id   = scrapy.Field()
    category_id   = scrapy.Field()
    category      = scrapy.Field()
    types         = scrapy.Field()
    province_code = scrapy.Field()
    province      = scrapy.Field()
    regency_code  = scrapy.Field()
    regency       = scrapy.Field()
    subdistrict_code = scrapy.Field()
    subdistrict   = scrapy.Field()
    latitude      = scrapy.Field()
    longtitude    = scrapy.Field()
    status        = scrapy.Field()
    created_at    = scrapy.Field()
    created_at_first = scrapy.Field()
    title         = scrapy.Field()
    main_info     = scrapy.Field()
    price         = scrapy.Field()
    sqr_building  = scrapy.Field()
    sqr_land      = scrapy.Field()
    bedroom       = scrapy.Field()
    bathroom      = scrapy.Field()
    floor         = scrapy.Field()
    certificate   = scrapy.Field()
    facility      = scrapy.Field()
    user_id       = scrapy.Field()
    user_type     = scrapy.Field()
    crawl_time    = scrapy.Field()