import scrapy


class Ygdy8Spider(scrapy.Spider):
    name = 'ygdy8'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://ygdy8.net/']

    def parse(self, response):
        pass
