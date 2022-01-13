# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from OLX import settings
import pymysql
import logging

class OlxPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into olxproperty (property_id, category_id, category, types, province_code, province, regency_code, regency, subdistrict_code, subdistrict, latitude, longtitude, status, created_at, created_at_first, title, main_info, price, sqr_building, sqr_land, bedroom, bathroom, floor, certificate, facility, user_id, user_type, crawl_time) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (  item['property_id'],
                   item['category_id'],
                   item['category'],
                   item['types'],
                   item['province_code'],
                   item['province'],
                   item['regency_code'],
                   item['regency'],
                   item['subdistrict_code'],
                   item['subdistrict'],
                   item['latitude'],
                   item['longtitude'],
                   item['status'],
                   item['created_at'],
                   item['created_at_first'],
                   item['title'],
                   item['main_info'],
                   item['price'],
                   item['sqr_building'],
                   item['sqr_land'],
                   item['bedroom'],
                   item['bathroom'],
                   item['floor'],
                   item['certificate'],
                   item['facility'],
                   item['user_id'],
                   item['user_type'],
                   item['crawl_time']
                 ))
            self.connect.commit()
        
        except Exception as e:
            logging.exception(e)
            
        return item
 
    def close_spider(self, spider):
        self.connect.close()
