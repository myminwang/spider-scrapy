## 基于scrapy的爬虫小项目
![py3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg) 
  [![](https://img.shields.io/badge/Scrapy-2.5-brightgreen.svg)]()

>这个是基于python-scrapy的爬虫项目，爬取电影天堂的所有电影，并保存到excel和sql中，写开发过程的原因是本人不是专门做爬虫的，担心时间长了，偶尔用的时候，不知道咋入手，并且这个项目放在public仓库中，也希望对爬虫初学者有一丁丁的帮助吧，我会尽量把步骤写详细一点点。
### 开发环境
* Python: 3.10.1
* Scrapy: 2.5.1
* 编辑器：pycharm
* 数据库：mysql（考虑过用sqlite3，担心并发爬取时，可能存在并发写操作，而

### 二、准备工作
* 查看py版本：`python -V`
* 并创建虚拟环境（环境的目录自己定吧，不要有中文路径、不要放到项目目录里就行）：`python -m venv venv`
* 进入虚拟环境：`venv\Scrpyt
* 升级pip等（这都是开发过程记录，如果要直接使用项目，参考后面的项目使用指南-如有）  
    
    
  `pip install --upgrade pip setuptools -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`
* 安装scrapy：`pip install scrapy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

* 博客文章 `markdown` 渲染，代码高亮
* 第三方社会化评论系统支持(畅言)
* 三种皮肤自由切换
* 全局搜索
* 阅读排行榜/最新评论
* 多目标源博文分享
* 博文归档
* 友情链接
* 分享、打赏功能

### 下载
```
git clone https://github.com/myminwang/myblog.git
```

### 安装
