# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CounterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()    #  标题
    company = scrapy.Field()    # 公司名称
    desc = scrapy.Field()    # 描述
    salary = scrapy.Field()    #  薪水范围
    location = scrapy.Field()    # 工作地点
    date = scrapy.Field()    # 发布日期
    datasource = scrapy.Field()    # 消息来源
