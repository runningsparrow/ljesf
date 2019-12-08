# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient

from ljesf.items import LjesfItem
from ljesf.items import LjdistrictItem
from ljesf.items import LjareaItem

class LjesfPipeline(object):
    def process_item(self, item, spider):
        return item

class districtPipeline(object):

    def open_spider(self, spider):
        if spider.name == "esflist":
            print("======pipe esflist========")
            # 链接数据库
            self.mongoconn = MongoClient(host="127.0.0.1",port=27017,) #connect to mongodb
            #for prod
            # self.mongoconn.ljesf.authenticate("sparrow","123456")  #auth
            # self.ljesfdb = self.mongoconn.ljesf
            #for dev
            self.mongoconn.lianjiaesf.authenticate("sparrow","123456")  #auth
            self.lianjiaesfdb = self.mongoconn.lianjiaesf


    def process_item(self, item, spider):
        if spider.name == "esflist":
            print ("start process districtPipeline")
            print (">>>>>>>>>>>>>>>>>>>>>>>>>>")
            print (item)
            print ("<<<<<<<<<<<<<<<<<<<<<<<<<<")


    
            # 写入数据库
            if isinstance(item, LjdistrictItem):
                self.lianjiaesfdb.district.insert(item)

            if isinstance(item, LjareaItem):
                self.lianjiaesfdb.area.insert(item)

            print("after insert")

        return item

    def close_spider(self,spider):

      #关闭连接
        if spider.name == "esflist":
            print ("clsee esflist")

