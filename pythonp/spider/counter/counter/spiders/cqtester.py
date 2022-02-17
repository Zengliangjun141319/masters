# -*- coding: utf-8 -*-
import scrapy
from counter.items import CounterItem
from scrapy.http import Request


class CqtesterSpider(scrapy.Spider):
    name = 'cqtester'
    allowed_domains = ['www.51job.com']
    start_urls = ['https://jobs.51job.com/chongqing/ruanjianceshi/p1/']

    def parse(self, response):
        pages = response.xpath('//input[@id="hidTotalPage"]/@value').extract()[0]
        pages = int(pages)
        # print("\n The Page is %d \n" %pages)
        for p in range(1, pages+1):
            # print("第 %d 页 \n" %p)
            yield Request("https://jobs.51job.com/chongqing/ruanjianceshi/p"+ str(p),callback=self.parsecontent, dont_filter=True)

    def parsecontent(self, response):
        contents = response.xpath('//p[@class="info"]')
        for content in contents:
            item = CounterItem()
            item['title'] = content.xpath('span/a/@title').extract()
            item['company'] = content.xpath('a/@title').extract()
            pays = content.xpath('span[@class="location"]/text()').extract()
            if not pays:
                pays = '面议'
            item['salary'] = pays
            item['location'] = content.xpath('span[@class="location name"]/text()').extract()
            pushdate = content.xpath('span[@class="time"]/text()').extract()
            # pushdate = "2018-" + pushdate
            item['date'] = pushdate
            item['datasource'] = '51Job'

            yield item
