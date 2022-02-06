## 基于scrapy的爬虫小项目
![py3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg) 
  [![](https://img.shields.io/badge/Scrapy-2.5-brightgreen.svg)]()

> 这个是基于python-scrapy的爬虫项目，爬取电影天堂的所有电影，并保存到excel和sql中，写开发过程的原因是本人不是专门做爬虫的，担心时间长了，偶尔用爬虫的时候，不知道咋入手，并且这个项目放在了public仓库中，也希望对爬虫初学者有一丁丁的帮助吧，我会尽量把步骤写详细一点点。
### 一、开发环境
* Python: 3.10.1
* Scrapy: 2.5.1
* 编辑器：Pycharm
* 数据库：MySQL（考虑过用sqlite3，担心并发爬取时，可能存在并发写操作，而sqlite貌似写独占，还是用mysql吧，官网是用mangodb举例的）
* OS：Windows 10
### 二、准备工作
> 这个是项目开发要做的事情，如果想直接使用项目，参考项目使用说明（最后再写）  
> Scrapy官方文档：https://docs.scrapy.org/en/latest/
* 查看py版本：`python -V`
* 并创建虚拟环境（环境的目录自己定吧，不要有中文路径、不要放到项目目录里就行）：`python -m venv venv`
* 进入虚拟环境：`venv\Scripts\activate`
* 升级pip等（用阿里镜像）：`pip install --upgrade pip setuptools -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`
* 安装scrapy（会发现安装了好多依赖包）：`pip install scrapy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`
* 安装chrome插件：在插件商店里（国内用户需要vpn），搜索xpath helper，安装不了也没啥事。

### 三、创建项目
#### 1、创建项目
终端运行：  
```shell
scrapy startproject ygdy8Spider  # 如果要在已有的文件夹下创建项目，后面加空格再加点(.)就行
```
为啥事ygdy8：我搜索电影天堂的时候，排前面的是这个网站，索性就爬它吧。。。
```shell
ygdy8Spider/
    scrapy.cfg            # 配置文件，可以配置多个项目使用不同的setting文件：https://docs.scrapy.org/en/latest/topics/commands.html

    ygdy8Spider/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # 设置数据存储模板，用于结构化数据，如：Django的Model

        middlewares.py    # project middlewares file

        pipelines.py      # 数据处理行为，爬取到的数据，会给到这里处理，比如转为json还是存到数据库

        settings.py       # 配置文件，如：递归的层数、并发数，延迟下载等

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```
可以发现，项目文件其实很少，而且结构分明：  
* 在scrapy.cfg里写项目整体的配置，尤其是有多个爬虫项目时，需要指定setting文件
* 在items中写要处理的数据，但以后爬虫写的多了，这个文件貌似作用不大
* 在middlewares中写中间件，比如需要ip代理时，把请求和响应通过中间件转给代理的IP和端口就行了
* 在pipelines中写管道，在yield item后，会自动进行管道处理，这里可以写爬到的数据是存到文件里呢，还是存到数据库里呢
* 在setting中写各种配置，比如要使用中间件、管道，需要配置；还可以配置日志信息、数据库信息、并发设置等等
* spiders文件中，是将要写的爬虫py文件，是写核心代码的地方，比如请求那些url、筛选那些数据等等  

#### 2、创建爬虫文件
终端运行：  
```shell
scrapy genspider ygdy8 ygdy8.net  # 第一个ygdy8是爬虫名称，也是生成py文件的名称，不能同项目名称重复了，第二个ygdy8.net是域名，只写域名哦，是允许爬虫采集的域名
```
在spiders文件夹中会生成一个新的py文件，是主要写代码的地方

### 四、边写代码边唠叨
#### 1、修改配置文件
ygdy8Spider/settings.py
```python
...
ROBOTSTXT_OBEY = False  # 是否遵循网站robot协议（类似君子协议，就是有的网站会在/robot.txt中注明那些内容是允许爬取的）

# Configure maximum concurrent requests performed by Scrapy (default: 16)  # 默认并发数可以不用修改，跟电脑性能有关
#CONCURRENT_REQUESTS = 32
...
# 末尾添加
# 设置日志级别
LOG_LEVEL = 'INFO'
LOG_FILE = "./spider.log"  # 设置日志文件，设置后运行爬虫的时候，日志不会在终端输出，都在文件里打印

# 禁止cookies 提高性能
COOKIES_ENABLED = False  # 看网站，对于不需要cookie的网站，关闭cookie可以提升性能

# 设置重试次数
RETRY_ENABLED = True  # 打开重试开关
RETRY_TIMES = 3  # 设置重试次数
```
#### 2、分析目标网站
先看下要爬的网站：https://www.ygdy8.net/html/gndy/dyzz/index.html  
上面的链接是最新电影，点击末页，能看到最老的电影是09年更新的，可以猜测，这个标签下应该能爬取到网站的所有电影。  
一页有25部电影，目前看一共有243页（22年2月5日）、6000多部电影。  
> 先要爬取电影列表页，获取电影详情页的链接；  
> 再爬取电影详情页，获取电影信息（包含下载方式）；
#### 3、动手写代码
ygdy8Spider/spiders/ygdy8.py  
里面已经自动生成了一点代码，继承自scrapy.Spider的类，可以看下官方文档：https://docs.scrapy.org/en/latest/topics/spiders.html#

***常用的属性：***  
* name：爬虫名称，必须项
* allowed_domains：爬取的域名列表，可以是多项，非必须
* start_urls：爬取的起始页面，是个列表，列表里面的url都会进行爬取  

***常用的方法：***
* start_requests()：作用同start_urls，返回的也是一个迭代对象，用于处理非规律性的url，或者使用post请求时，用这个方法，其实爬取一般网站，用start_urls就行了；
* parse(response)：核心方法，用于处理scrapy.request请求后的response，数据抓取、处理，都在这里写


修改后的代码：
```python
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
```
然后，终端运行：  
```shell
scrapy crawl ygdy8
```
会打印出movie_detail_urls列表，并且日志会打印在项目根目录下的scrapy.log中  

scrapy 有好多命令，在终端直接运行scrapy会打印所有命令，常用的就是crawl、shell等  
另外上面代码中，使用了xpath，xpath是一种专门的语法，学习的话，可以看：https://www.w3school.com.cn/xpath/index.asp  
当然，scrapy除了使用xpath选择器，也常使用css选择器，可以看官网：https://docs.scrapy.org/en/latest/topics/selectors.html  
关于xpath：  
* 在页面上，选中待查看的元素，右击查看元素，可以看到xml代码，然后，右击标签 Copy-Copy Xpath，可以获取xpath，挺长的，一般不用它；
* 可以使用chrome插件xpath helper在页面上直接调试；
* 可以使用scrapy的shell进行调试；

终端运行：
```shell
scrapy shell https://www.ygdy8.net/html/gndy/dyzz/index.html
```
会进入调试的shell，用的是py-shell
```shell
>>> res = response.xpath('//div[@class="co_content8"]/ul//a/@href')  # 这个是获取的Selector对象
>>> res
[<Selector xpath='//div[@class="co_content8"]/ul//a/@href' data='/html/gndy/dyzz/20220126/62245.html'>, <Selector xpath='//div[@class="co_content8"]/ul//a/@href' data='/html/gndy/dyzz/20220126/62244.html'>, <Selector xpath='//div[@c
lass="co_content8"]/ul//a/@href' data='/html/gndy/dyz
...
>>> res.get()   # get()只获取单个/首个值，如果获取不到值，返回None，get也能接收一个default参数，用于获取不到值时，返回自定义的默认值
'/html/gndy/dyzz/20220126/62245.html'
>>> res.getall()  # 获取所有值，返回一个列表
['/html/gndy/dyzz/20220126/62245.html', '/html/gndy/dyzz/20220126/62244.html', '/html/gndy/dyzz/20220125/62243.html', '/html/gndy/dyzz/20220125/62242.html', '/html/gndy/dyzz/20220124/62235.html', '/html/gndy/dyzz/20220122/62227.html
', '/html/gndy/dyzz/20220121/62219.html', '/html/gndy/dyzz/20220117/62209.html', '/html/gndy/dyzz/20220116/62203.html', '/html/gndy/dyzz/20220116/62202.html', '/html/gndy/dyzz/20220115/62199.html', '/html/gndy/dyzz/20220114/62196.ht
ml', '/html/gndy/dyzz/20220114/62195.html', '/html/gndy/dyzz/20220114/62194.html', '/html/gndy/dyzz/20220112/62191.html', '/html/gndy/dyzz/20220112/62190.html', '/html/gndy/dyzz/20220111/62188.html', '/html/gndy/dyzz/20220111/62186.
html', '/html/gndy/dyzz/20220109/62183.html', '/html/gndy/dyzz/20220109/62181.html', '/html/gndy/dyzz/20220108/62178.html', '/html/gndy/dyzz/20220107/62176.html', '/html/gndy/dyzz/20220107/62175.html', '/html/gndy/dyzz/20220106/6217
3.html', '/html/gndy/dyzz/20220105/62169.html']

```
其中：get()类似extract_first()、getall()类似.extract()，区别很小，具体可以看下官网说明。  

好了，可以看到，我们获取到了当前列表页中，所有的电影详情的url，接下来我们安装以下步骤进行：
*  请求获取到的电影详情url，来获取电影信息
*  然后将电影信息存储到excel和数据库中
*  解析起始页，然后爬取所有列表页（也就是对“下一页”进行操作）
*  运行爬虫，获取数据

#### 4、编写items
#### 5、编写管道
#### 6、运行爬虫



下载链接有两种：磁力链接和迅雷专用的链接：thunder://格式

