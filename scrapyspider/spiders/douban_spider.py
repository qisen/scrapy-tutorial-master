# -*- coding: utf-8 -*-
# @Time     : 2017/1/7 17:04
# @Author   : woodenrobot
# -*- coding: UTF-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem


class DoubanMovieTop250Spider(Spider):
    name = 'jiandan'
    allowed_domains = ["jandan.net"]
    headers ={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Policy': 'no-referrer-when-downgrade',
        'Cache-Control': 'max-age=300',
        'Fcache': 'HIT',
        'Link': '<http://jandan.net/?p=21183>; rel=shortlink',
        'Link': '<http://jandan.net/wp-json/>; rel="https://api.w.org/"',
    }
    #http://blog.csdn.net/djd1234567/article/details/50319329   防止屏蔽
    #http://blog.csdn.net/qq_31518899/article/details/76576537  数据存储
    # http: // m.blog.csdn.net / t1anyuan / article / details / 78644814
    start_urls = ["http://jandan.net/ooxx/page-336#comments"]
    maxNum = 300
    current = 0

    def parse(self, response):
        item = DoubanMovieItem()
        strpp=response.xpath('//img//@src').extract()
        strpplist=[]
        print("strpp",strpp)
        for i in range(len(strpp)):
            strpplist.insert(i,strpp[i] if 'http:' in strpp[i] else ('http:' + strpp[i]))
            item['image_urls'] = strpplist# 提取图片链接

        # print('image_urls',item['image_urls'])
        yield item
        self.current = self.current + 1
        if self.maxNum > self.current:
            new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()  # 翻页
            # print 'new_url',new_url
            if new_url:
               yield Request(new_url if 'http:' in new_url else ('http:' + new_url), callback=self.parse)