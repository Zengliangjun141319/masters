# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

class BaidurecruitPipeline(object):
    def process_item(self, item, spider):
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        pwd = settings['MYSQL_PASSWD']
        db = settings['MYSQL_DBNAME']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']

        # 数据库连接
        con = pymysql.connect(host=host, user=user, passwd=pwd, db=db, charset=c, port=port)
        # 数据库游标
        cue = con.cursor()
        print("Mysql connect succes!")
        sqls = "insert into cqtester(Title,Company,Salary,Location,date,DataSource) values(%s,%s,%s,%s,%s,%s)"
        paras = (item['title'],item['company'],item['salary'],item['location'],item['date'],item['datasource'])

        try:
            cue.execute(sqls, paras)
            print("insert success")
        except Exception as e:
            print("Insert error: ", e)
            con.rollback()
        else:
            con.commit()
        con.close()

        return item
