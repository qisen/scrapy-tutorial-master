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
    # headers ={
    #     'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.113Safari / 537.36',
    # }
    #http://blog.csdn.net/djd1234567/article/details/50319329   防止屏蔽
    #http://blog.csdn.net/qq_31518899/article/details/76576537  数据存储
    start_urls = ["http://jandan.net/ooxx"]
    maxNum = 10
    current = 0

    def parse(self, response):
        item = DoubanMovieItem()
        strpp=response.xpath('//img//@src').extract()
        # print("response",response.body)
        # return
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