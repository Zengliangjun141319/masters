# -*- coding: utf-8 -*-
import scrapy
from books.items import BooksItem
from scrapy.http import Request

class FictionSpider(scrapy.Spider):
    name = 'fiction'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://book.qidian.com/info/3614713#Catalog']
    global cc
    cc = 0
    
    def parse(self, response):
        hxs = response
        # 获取书名
        names = hxs.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0]  # 书页获取书名
        # names = hxs.xpath('//a[@id="bookImg"]/text()').extract()[0]
        item = BooksItem()
        item['title'] = names
        charterurls = hxs.xpath('//li[@data-rid="1"]/a/@href').extract()
        # urls = "//read.qidian.com/chapter/2Ieg-MqDCpg1/CoGYf_8Jrm0ex0RJOkJclQ2"
		# 通过获取到的第一章URL进入页面
        for charterurl in charterurls:
            print(charterurl)
            yield Request("https:" + charterurl, meta={'item':item}, callback=self.parsecharter, dont_filter=True)
            return

    def parsecharter(self,response):
        hxs = response
        global cc
        # 获取章节名
        titles = hxs.xpath('//h3[@class="j_chapterName"]/text()').extract()[0]
        item = response.meta['item']
        content = ''
        content = '\n' + content + str(titles) + '\n'
        s = hxs.xpath('//div[@class="read-content j_readContent"]//p/text()').extract()
        for srt in s:
            srt = srt.replace("\u3000", " ")
            content = content + srt +'\n'

        desc = item.get('desc')
        if None==desc:
            item['desc'] = content
        else:
            item['desc'] = desc + content
        if content=='':
            yield item

        chapters = hxs.xpath('//a[@id="j_chapterNext"]/@href').extract()  # 下一章地址
        Nextt = hxs.xpath('//a[@id="j_chapterNext"]/text()').extract()[0]  #判断是不是最后一章
        if Nextt == '书末页':
            yield item
            return
        '''
        if cc == 600:
            yield item
            return
        cc = cc + 1
        '''
        for chapter in chapters:
            yield Request("https:" + chapter, meta={'item':item}, callback=self.parsecharter, dont_filter=True)