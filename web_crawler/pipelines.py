# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 数据处理行为，如：一般数据化的数据持久化

import json

class WebCrawlerPipeline(object):
    """
        功能：保存item数据
    """

    def __init__(self):
        self.filename = open("test.txt", "a+")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()
