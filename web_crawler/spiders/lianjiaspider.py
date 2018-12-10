#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "hailong"

from web_crawler.items import WebCrawlerItem
import scrapy

next_link = 0
url = 'https://cd.fang.lianjia.com/loupan/pg{}/'.format(next_link)

class Test(scrapy.Spider):
    name = "test"
    start_urls = [url]

    def parse(self, response):
        if response.xpath("//div[@class='no-result-wrapper show']"):
            return

        names = response.xpath("//div[@class='resblock-desc-wrapper']")
        for name in names:
            item = WebCrawlerItem()
            item['name'] = name.xpath(".//div[@class='resblock-name']/a/text()").extract()[0]
            item['price'] = name.xpath(".//div[@class='resblock-price']/div/span[1]/text()").extract()[0]
            yield item
        next_link += 1
        global next_link
        print next_link
        next_url = 'https://cd.fang.lianjia.com/loupan/pg{}/'.format(next_link)
        yield scrapy.Request(next_url, callback=self.parse)
