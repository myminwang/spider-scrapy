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
先看下要爬的网站：https://www.ygdy8.net/html/gndy/dyzz/index.html  
上面的链接是最新电影，点击末页，能看到最老的电影是09年更新的，可以猜测，这个标签下应该能爬取到网站的所有电影。  
一页有25部电影，目前看一共有243页（22年2月5日）、6000多部电影。  

#### 1、修改配置文件
#### 2、编写爬虫，获取数据（测试为主）
#### 3、编写items
#### 4、编写管道
#### 5、运行爬虫



下载链接有两种：磁力链接和迅雷专用的链接：thunder://格式

