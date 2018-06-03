#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:46:35 2018

@author: ajv
"""

import scrapy,csv,time
from datetime import datetime

#filename = input('Please enter the filename with urls input: ')
filename = 'output.csv'

links = []
with open(filename,'r') as starter:
    stuff = csv.reader(starter)
    for row in stuff:
        links += row
urls = links[11::3]

class BaTSpider_Listing_Summary(scrapy.Spider):
    name = "bat_listing_spider"
    start_urls = urls

    def parse(self, response):  
        LISTING_TITLE = '//title/text()'
        CAR_NAME = '//h1/text()'
        CURRENT_BID_SELECTOR = '//table//*[@class="listing-stats-value current-bid-value"]/text()'
        NUM_BIDS_SELECTOR = '//table//*[@class="listing-stats-value number-bids-value"]/text()'
        VIEW_STATS = '//table//*[@class="listing-stats-views"]//span/text()'
        NUM_COMMENTS = '//*[@class="comments-title"]/text()'
        ESSENTIALS = '//*[@class="listing-essentials-item"]//text()'
        ESSENTIALS_2 = '//*[@class="listing-essentials-item listing-essentials-item-categories"]//text()'
        yield {
                'Timestamp': datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                'Listing Title': response.xpath(LISTING_TITLE).extract_first(),
                'Car Make and Model': response.xpath(CAR_NAME).extract_first(),
                'Current Bid Price': response.xpath(CURRENT_BID_SELECTOR).extract(),
                'Number of Bids': response.xpath(NUM_BIDS_SELECTOR).extract(),
                'View Stats': response.xpath(VIEW_STATS).extract(),
                'Number of Comments': response.xpath(NUM_COMMENTS).extract_first(),
                'Essentials Table': response.xpath(ESSENTIALS).extract(),
                'Essentials Cont\'d': response.xpath(ESSENTIALS_2).extract()
            }
