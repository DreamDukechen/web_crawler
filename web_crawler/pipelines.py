# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 数据处理行为，如：一般数据化的数据持久化

class WebCrawlerPipeline(object):
    def process_item(self, item, spider):
        with open("./test.txt", "a+") as f:
            f.write(item['name'].encode("utf8") + ",")
            f.write(item['price'].encode("utf8") + "\n")
