# -*- coding: utf-8 -*-
import scrapy, time
from datetime import datetime

class BaTSpider(scrapy.Spider):
    name = "bat_spider"
    start_urls = ['https://bringatrailer.com/auctions/']
    def parse(self, response):  
        CONTAINER_SELECTOR = '.auctions-item-container'
        NAME_SELECTOR = 'a ::text'
        LINK_SELECTOR = 'h3 ::attr(href)'
        TITLE_SELECTOR = '.auctions-item-title'
        for bat_spider in response.css(CONTAINER_SELECTOR):
            yield {
                'timestamp': datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                'name': bat_spider.css(TITLE_SELECTOR).css(NAME_SELECTOR).extract_first(),
                'link': bat_spider.css(LINK_SELECTOR).extract_first()
            }