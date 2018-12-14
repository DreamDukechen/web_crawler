#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = "hailong"

from web_crawler.items import WebCrawlerItem
import scrapy

class Test(scrapy.Spider):
    name = "test"
    allowed_domains = ["fang.lianjia.com"]
    next_link = 0
    url = 'https://cd.fang.lianjia.com/loupan/pg{}/'.format(next_link)
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
        self.next_link += 1
        next_url = 'https://cd.fang.lianjia.com/loupan/pg{}/'.format(self.next_link)
        yield scrapy.Request(next_url, callback=self.parse)
