import io
import sys
from lxml import html
import scrapy 
import requests
import os
import json


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)    


class Scrape_fin(scrapy.Spider):
    name="Scrape_fin"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    start_urls = [
            'https://www.redfin.com/city/245/NY/Albany/filter/include=sold-6mo',
    ]
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)
 
    def parse(self,response):
        
        links=dict()
        for city in response.css('td'):
            links[city.css('a::text').extract_first()]=self.start_urls[0]+city.css('a::attr("href")').extract_first()
        with open("links"+'.json','w') as f:
                    f.write(json.dumps(links))
        
               