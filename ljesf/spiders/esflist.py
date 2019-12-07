# -*- coding: utf-8 -*-
import scrapy
import os
import sys


#to resolve module not found ljesf
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)

import time
import random

from ljesf.items import LjesfItem
from ljesf.items import LjdistrictItem
from ljesf.items import LjareaItem

class EsflistSpider(scrapy.Spider):
    name = 'esflist'
    allowed_domains = ['sh.lianjia.com/ershoufang/']
    start_urls = ['https://sh.lianjia.com/ershoufang/']

    def __init__(self):
        self.baseurl = "https://sh.lianjia.com"
        #控制第一层访问区域的开关
        self.level1 = 0
        #控制第二层访问小区域的开关
        self.level2 = 1
        #区域列表
        self.districtlist = []
        self.arealist = []
        #存储区域的总数
        self.districtcount = 0
        #区域索引,用于控制访问哪个区域页面
        self.districtindex = 0

    def parse(self, response):
        # pass
        print ("EsflistSpider start parse")
        
        if self.level1 == 0:
            print("start level1")
            if self.districtcount == 0:
                self.districtlist = response.xpath('//div[@data-role="ershoufang"]/div/a')
                print(self.districtlist)
                self.districtcount = len(self.districtlist)
                # for item in self.districtlist:
                #     print(item.xpath('@href').extract())
                #####################################
                # #first yield
                print(self.districtlist[self.districtindex])
                onedistrict = self.districtlist[self.districtindex]

                if self.districtindex < self.districtcount:
                    print(onedistrict.xpath('@href').extract())
                    nexturl = self.baseurl + onedistrict.xpath('@href').extract()[0]
                    # self.districtindex += 1
                    yield scrapy.Request(nexturl, callback=self.parse, dont_filter=True)
                else:
                    #open level2
                    self.level2 = 0
                    print("debug1 area crawl finished!")
            else:
                if self.districtindex < self.districtcount:
                    onedistrict = self.districtlist[self.districtindex]

                    print(self.districtlist[self.districtindex])
                    print(response.url)

                    #build item
                    ljditem = LjdistrictItem()

                    #_id
                    ljditem['_id'] = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) + str(random.randrange(100, 999))

                    #district_title
                    ljditem['district_title'] = onedistrict.xpath('@title').extract()[0]

                    #district_text
                    ljditem['district_text'] = onedistrict.xpath('text()').extract()[0]

                    #district_href
                    ljditem['district_href'] = onedistrict.xpath('@href').extract()[0]
                    
                    #district_date
                    ljditem['district_date'] = str(time.strftime('%Y%m%d',time.localtime(time.time())))

                    #district_timestamp
                    ljditem['district_timestamp'] = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

                    yield ljditem
                    #build item end

                    #parse areas of each district

                    self.arealist = response.xpath('//div[@data-role="ershoufang"]/div[2]/a')
                    for item in self.arealist:
                        print(item.xpath('@href').extract())

                        #build area item
                        ljaitem = LjareaItem()

                        # _id
                        ljaitem['_id'] = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) + str(random.randrange(100, 999))

                        # area_text 
                        ljaitem['area_text'] = item.xpath('text()').extract()[0]


                        # area_href 
                        ljaitem['area_href'] = item.xpath('@href').extract()[0]

                        # area_date 
                        ljaitem['area_date'] = str(time.strftime('%Y%m%d',time.localtime(time.time())))

                        # area_timestamp 
                        ljaitem['area_timestamp'] = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

                        # area_district_id 
                        ljaitem['area_district_id'] = ljditem['_id']

                        yield ljaitem
                        #build area item end
                    

                    nexturl = self.baseurl + onedistrict.xpath('@href').extract()[0]
                    yield scrapy.Request(nexturl, callback=self.parse, dont_filter=True)
                    #区域索引自增
                    self.districtindex += 1
                    
                else:
                    #open level2
                    self.level2 = 0
                    print("debug2 area crawl finished!")

                
                


        if self.level2 == 0:
            print("start level2")

#代替命令行执行爬虫
if __name__ == '__main__':
    os.system("scrapy crawl esflist")