# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class PublichousePipeline(object):
    def process_item(self, item, spider):
        self.file = codecs.open(item.get('title')+ '.txt', 'w', encoding='utf-8')
        self.file.write(item.get('desc')+ '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()