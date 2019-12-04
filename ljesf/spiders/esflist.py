# -*- coding: utf-8 -*-
import scrapy


class EsflistSpider(scrapy.Spider):
    name = 'esflist'
    allowed_domains = ['https://sh.lianjia.com/ershoufang/']
    start_urls = ['http://https://sh.lianjia.com/ershoufang//']

    def parse(self, response):
        pass
