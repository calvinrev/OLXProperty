@echo [off]
cmd /k "scrapy crawl olxPropertySitemap  && python removeDuplicate.py"