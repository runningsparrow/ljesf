# -*- coding: utf-8 -*-
import scrapy
import os


class EsflistSpider(scrapy.Spider):
    name = 'esflist'
    allowed_domains = ['sh.lianjia.com/ershoufang/']
    start_urls = ['https://sh.lianjia.com/ershoufang/']

    def __init__(self):
        self.level1 = 0
        self.level2 = 0

    def parse(self, response):
        # pass
        print ("EsflistSpider start parse")
        
        
        districtlist = response.xpath('//div[@data-role="ershoufang"]/div/a')
        print(districtlist)
        for item in districtlist:
            print(item)

#代替命令行执行爬虫
if __name__ == '__main__':
    os.system("scrapy crawl esflist")