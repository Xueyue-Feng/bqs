# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cnkispider10Item(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    # time = scrapy.Field()
    # source = scrapy.Field()
    # institution = scrapy.Field()
    # refer = scrapy.Field()
    #
    # keywords = scrapy.Field()
    # abstract = scrapy.Field()
    # download = scrapy.Field()
    pass

class YeTuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    dailyRate = scrapy.Field()
    lines = scrapy.Field()
    deadline = scrapy.Field()
    describe = scrapy.Field()
    advantage = scrapy.Field()
    pass

class wdzjSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    rate = scrapy.Field()
    timeOnline = scrapy.Field()
    score = scrapy.Field()
    pass
class FinancingSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    lines = scrapy.Field()
    cost = scrapy.Field()
    pass

class Kouzispider10Item(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    loanAuditDetails = scrapy.Field()
    requirements = scrapy.Field()
    pass

class LoadSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    lines = scrapy.Field()
    describe = scrapy.Field()
    cost = scrapy.Field()
    applications = scrapy.Field()
    pass
