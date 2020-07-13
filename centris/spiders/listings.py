# -*- coding: utf-8 -*-
import scrapy


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca/en']
    start_urls = ['http://www.centris.ca/en/']

    def parse(self, response):
        pass
