# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import json
import codecs
class Cnkispider10Pipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('wdzj.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_close(self, spider):
        self.con.close()