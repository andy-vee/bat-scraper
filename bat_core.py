# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:25:34 2018

@author: anvan
"""

from listing_scraper2b import listing_scraper2b

from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings

def spider_closing(spider):
    """Activates on spider closed signal"""
    log.msg("Closing Reactor", level=log.INFO)
    reactor.stop
    
log.start(loglevel=log.DEBUG)
settings = Settings()
settings.set("USER_AGENT","Vance")
crawler = Crawler(settings)

crawler.signals.connect(spider_closing, signal=signals.spider_closed)

crawler.configure()
crawler.crawl(listing_scraper2b)
crawler.start()
reactor.run()
