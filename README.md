## 基于scrapy的爬虫小项目
![py3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg) 
  [![](https://img.shields.io/badge/Scrapy-2.5-brightgreen.svg)]()

>这个是基于python-scrapy的爬虫项目，爬取电影天堂的所有电影，并保存到excel和sql中，写开发过程的原因是本人不是专门做爬虫的，担心时间长了，偶尔用的时候，不知道咋入手，并且这个项目放在public仓库中，也希望对爬虫初学者有一丁丁的帮助吧，我会尽量把步骤写详细一点点。
### 一、开发环境
* Python: 3.10.1
* Scrapy: 2.5.1
* 编辑器：pycharm
* 数据库：MySQL（考虑过用sqlite3，担心并发爬取时，可能存在并发写操作，而sqlite貌似写独占，还是用mysql吧，官网是用mangodb举例的）
* OS：Windows 10
### 二、准备工作
>这个是项目开发要做的事情，如果想直接使用项目，参考项目使用说明（最后再写）
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

```
