# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 库名
    repo = scrapy.Field()
    # # 子标题
    sub_title = scrapy.Field()
    # # 排名
    rank = scrapy.Field()
     
    # # 链接
    link = scrapy.Field()