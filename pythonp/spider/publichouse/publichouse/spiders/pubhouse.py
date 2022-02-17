# -*- coding: utf-8 -*-
import scrapy
from publichouse.items import PublichouseItem
from  scrapy.selector import Selector
from scrapy.http import Request



class PubhouseSpider(scrapy.Spider):
    name = 'pubhouse'
    allowed_domains = ['cqgzfglj.gov.cn']
    start_urls = ['http://www.cqgzfglj.gov.cn/gongzdt/']
    homes = 'www.cqgzfglj.gov.cn/gongzdt/'

    def parse(self, response):
        # dt = Selector(response)
        # 获取每条动态的URL
        dongtai = response.xpath('//ul[@id="textList_ul"]//li/a/@href').extract()
        for details in dongtai:
            # 根据每条动态的URL跳转到具体页面
            item = PublichouseItem()
            # item['title'] = details.xpath('a/text()').extract()
            # jumpurl = details.xpath('a/@href').extract()
            jumpurl = details.lstrip('./')    # 去掉左边的 .
            print("URL is : %s" % jumpurl)
            # yield item
            yield  Request("http://www.cqgzfglj.gov.cn/gongzdt/" + jumpurl, callback=self.paresDetail)

    def paresDetail(self, response):
        hxs = Selector(response)
        item = PublichouseItem()
        # 获取动态的标题
        biaoti = hxs.xpath('//h2[@class="article_title f20 t_center"]/text()').extract()[0]
        ti=(str(biaoti)).strip()    # 消除标题前后的空格
        # 标题中如有 、 的，替换为 _
        if '、' in ti:
            biaotia = ti.replace("、", "_")
        else:
            biaotia = ti
        print("标题： ", biaotia)
        item['title'] = biaotia
        cont = hxs.xpath('//p/font/text()').extract()
        content = ''
        content = content + biaotia + '\n' + str(cont)
        item['desc'] = content
        print(item.get('desc') + '\n')
        yield item
