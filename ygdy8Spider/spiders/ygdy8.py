# -*- coding: utf-8 -*-
import scrapy


class Ygdy8Spider(scrapy.Spider):
    name = 'ygdy8'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/index.html']  # 爬虫起始页，跟list_23_1.html，是一个页面

    # 列表页的urls很规则，可以用下面的生成式，但是考虑到以后网站如果添加新的页面，就不好用了，所以改成点击“下一页”的方式
    # start_urls = [f'https://www.ygdy8.net/html/gndy/dyzz/list_23_{page}.html' for page in range(1,244)]

    def parse(self, response):
        # 测试一下
        movie_detail_urls = response.xpath('//div[@class="co_content8"]/ul//a/@href').getall()
        print(movie_detail_urls)
        pass
