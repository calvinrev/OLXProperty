import scrapy, json, logging
from datetime import datetime
from random import randint
from OLX.items import OlxItem
from OLX.getKecList import*
from OLX.formatData import*

class OlxpropertysitemapSpider(scrapy.Spider):
    name = 'olxPropertySitemap'
    allowed_domains = ['www.olx.co.id']
    start_urls = ['https://www.olx.co.id/']

    def __init__(self):
        #run time
        self.runtime = datetime.now().strftime('%Y-%m-%d')

        # setup log
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logFormatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

        # log file handler
        fileHandler = logging.FileHandler(f'logs/log-sitemap-{datetime.now().strftime("%Y-%m-%d")}.log')
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        #category
        self.category = {
            "jual-rumah-apartemen":5158,
            "sewa-rumah-apartemen":5160,
            "tanah":4827,
            "indekos":4833,
            "jual-bangunan-komersil":5154,
            "sewa-bangunan-komersil":5156
        }

        #kecamatan list
        self.kecList = getKecList()

    def parse(self, response):
        #Loop getting API response
        for batch in batchProcess(self.kecList): #batch processing
            for loc in batch:
                for category, category_id in self.category.items():
                    urls = f'https://www.olx.co.id/api/relevance/search?category={category_id}&facet_limit=100&location={loc}&location_facet_limit=20&page=0&platform=web-desktop&user={randint(11, 99)}a{randint(1000, 9999)}4bfax26d{randint(100, 999)}a9'
                    yield response.follow(url=urls, callback=self.parseProp, meta={'category': category, 'category_id': category_id, 'loc': loc, 'page':0}, priority=1)

    def parseProp(self, response):       
        cat    = response.request.meta['category']
        catId   = response.request.meta['category_id']
        loc     = response.request.meta['loc']
        page    = response.request.meta['page']
        resp    = json.loads(response.body)
        notEmpty= resp.get('not_empty')
        
        if notEmpty:
            try:
                logging.info(f'{response.status}: {loc} {page}')
                props = resp.get('data')

                for prop in props:
                    location   = prop.get('locations_resolved')
                    subdis     = location.get('SUBLOCALITY_LEVEL_1_id')
                    status     = prop.get('status')
                    parameters = prop.get('parameters')

                    if str(subdis) == str(loc): #make sure fits the kecamatan area 
                        item = OlxItem()
                        item['property_id']     = prop.get('id')
                        item['category_id']     = prop.get('category_id')
                        item['category']        = cat
                        item['types']           =  getValue(parameters, 'type')
                        item['province_code']   = location.get('ADMIN_LEVEL_1_id')
                        item['province']        = location.get('ADMIN_LEVEL_1_name')
                        item['regency_code']    = location.get('ADMIN_LEVEL_3_id')
                        item['regency']         = location.get('ADMIN_LEVEL_3_name')
                        item['subdistrict_code']= subdis
                        item['subdistrict']     = location.get('SUBLOCALITY_LEVEL_1_name')
                        item['latitude']        = prop.get('locations')[0].get('lat')
                        item['longtitude']      = prop.get('locations')[0].get('lon')
                        item['status']          = status.get('status')
                        item['created_at']      = prop.get('created_at')
                        item['created_at_first']= prop.get('created_at_first')
                        item['title']           = prop.get('title')
                        item['main_info']       = prop.get('main_info')
                        item['price']           = int(prop.get('price').get('value').get('raw'))
                        item['sqr_building']    = getValue(parameters, 'p_sqr_building')
                        item['sqr_land']        = getValue(parameters, 'p_sqr_land')
                        item['bedroom']         = getValue(parameters, 'p_bedroom')
                        item['bathroom']        = getValue(parameters, 'p_bathroom')
                        item['floor']           = getValue(parameters, 'p_floor')
                        item['certificate']     = getValue(parameters, 'p_certificate')
                        item['facility']        = getFacilities(parameters)
                        item['user_id']         = prop.get('user_id')
                        item['user_type']       = prop.get('user_type')
                        item['crawl_time']      = self.runtime
                        yield item

                if len(props)==20:
                    yield scrapy.Request(
                        url = response.url.replace(f'page={page}',f'page={page+1}'),
                        callback = self.parseProp,
                        priority=1,
                        meta={'category': cat, 'category_id': catId, 'loc': loc, 'page':page+1}
                    )

            except Exception as e:
                logging.critical(e, exc_info=True)

        else:
            logging.info(f'Page: {page} - {loc} {response.url} : Reach the last page..')
