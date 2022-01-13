# OLXProperty Scraper
This repo contains the code for crawl property data from (https://www.olx.co.id) using Scrapy (+Requests & BeautifulSoup4). The data scraping method is done by utilizing the APIs available on web pages. Because for each API use there is a limit to the number of pages that can be accessed, we use the lowest available administrative area approach, namely the sub-district (kecamatan). To get the list of sub-district codes, there are 2 methods that we provide in this repository. The first is to use a list of sub-districts on the sitemap page of the website (but not nationally complete). And the second by using the brute force method of sub-district code.

## Setup
1) pip install -r requirements.txt
2) Create a new MySql database, then import the db.sql file so that the olxproperty table will appear
3) Open settings.py file, scroll down, and change the DB setup adjusted to the database you have created previously

## Run
1) Method-1: Using Sitemap <br>
   Run `scrapy crawl olxPropertySitemap` at the project top level.
   <br>or<br>
   Run scrapSitemapProperty.bat file
2) Transacted Ads <br>
   Run `scrapy crawl rumah123trx` at the project top level.
   <br>or<br>
   Run scrapBruteProperty.bat file
   
