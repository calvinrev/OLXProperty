@echo [off]
cmd /k "scrapy crawl olxPropertyBrute && python removeDuplicate.py"