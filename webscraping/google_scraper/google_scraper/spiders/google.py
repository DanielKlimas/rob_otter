# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import re
import configparser

#-------------------------------------------------------------------------------------------------------------------
#   this is importing the config of the webscraping.ini for configuring the spider without programming it
#-------------------------------------------------------------------------------------------------------------------
module = "webscraping.ini"
separator = os.sep
path_to_ini = os.getcwd()
path_to_ini = re.sub(r'/google_scraper/google_scraper/spiders','',path_to_ini)
path_to_ini = path_to_ini + separator + module
print(path_to_ini)


############################################
def get_ini():

    path = path_to_ini
    config = configparser.ConfigParser()
    config.read(path)
    config.sections()
    config_dict = dict(config['config'])


    return config_dict
############################################
sites_scraping = int(get_ini()['google_sites'])
sites_scraping *= 10
print(sites_scraping)


class GoogleSpider(scrapy.Spider):

    name = 'google'
    allowed_domains = ['google.at']

    def start_requests(self):


        list_of_urls = []

        for i in range(0,sites_scraping,10):
            list_of_urls.append("https://www.google.at/search?q=site:.at&start={}".format(i))

        for url in list_of_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for i in response.css('cite::text').extract():
            yield {'link': i}


