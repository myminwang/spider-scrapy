# -*- coding: utf-8 -*-
import scrapy
import re


class Ygdy8Spider(scrapy.Spider):
    name = 'ygdy8'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/index.html']  # 爬虫起始页，跟list_23_1.html，是一个页面

    # 列表页的urls很规则，可以用下面的生成式，但是考虑到以后网站如果添加新的页面，就不好用了，所以改成点击“下一页”的方式
    # start_urls = [f'https://www.ygdy8.net/html/gndy/dyzz/list_23_{page}.html' for page in range(1,244)]

    def parse(self, response):
        # 测试一下
        movie_detail_urls = response.xpath('//div[@class="co_content8"]/ul//a/@href').getall()
        if movie_detail_urls:
            for movie_detail_url in movie_detail_urls:
                detail_url = response.urljoin(movie_detail_url)  # 拼接详情页url
                # 如果要传递参数给detail_page_parse方法，在这里添加meta={"title", "123"}，然后在detail_page_parse使用response.meta.get("title", "")即可
                yield scrapy.Request(detail_url, callback=self.detail_page_parse)  # 使用回调函数detail_page_parse解析response
                break

    def detail_page_parse(self, response):
        title = response.css(".title_all h1 font::text").get()  # css选择器：.title_all选择所有有这个class的元素，然后筛选h1 font元素，然后提取text值
        contents = response.css('#Zoom').get().replace('\u3000', '').replace('\xa0','').replace('\r\n','')  # 获取div标签内容，str类型   \xa0 是不间断空白符 \u3000 是全角的空白符
        # 进行数据整理
        print('====================================start',title)
        if contents:
            content_list = contents.split('<br>')    # 按<br>转换为list，正则就是一个灾难，果断放弃了，以后再转re吧
            print(content_list)
            for element in content_list:
                # element.replace('\u3000', '').replace('\xa0','')  # \xa0 是不间断空白符 \u3000 是全角的空白符
                # with open('./1.txt',"a+") as fa:
                #     fa.write(str(element))
                # print(element)
                pass

        print('====================================end',title)

