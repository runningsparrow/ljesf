# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LjesfItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    esf_title = scrapy.Field()
    erf_title_href = scrapy.Field()
    erf_title_housecode = scrapy.Field()
    #小区
    esf_flood_region = scrapy.Field()   
    #乡镇
    esf_flood_position = scrapy.Field()
    #户型
    esf_houseinfo_roomtype = scrapy.Field()
    #面积 
    esf_houseinfo_area = scrapy.Field()
    #朝向
    esf_houseinfo_orientation = scrapy.Field()
    #装修
    esf_houseinfo_decoration = scrapy.Field()
    #楼层
    esf_houseinfo_floor = scrapy.Field()
    #房龄
    esf_houseinfo_age  = scrapy.Field()
    #楼型
    esf_houseinfo_style = scrapy.Field()
    #挂牌情况
    esf_followinfo = scrapy.Field()
    #价格
    esf_price_total = scrapy.Field()
    esf_price_measurement = scrapy.Field()
    esf_price_unit = scrapy.Field()
    esf_date = scrapy.Field()
    esf_timestamp = scrapy.Field()

class LjdistrictItem(scrapy.Item):

    _id = scrapy.Field()
    district_title = scrapy.Field()
    district_text = scrapy.Field()
    district_href = scrapy.Field()
    district_date = scrapy.Field()
    district_timestamp = scrapy.Field()


class LjareaItem(scrapy.Item):

    _id = scrapy.Field()
    area_text = scrapy.Field()
    area_href = scrapy.Field()
    area_date = scrapy.Field()
    area_timestamp = scrapy.Field()
    area_district_id = scrapy.Field()
