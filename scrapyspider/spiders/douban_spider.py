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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    }
    start_urls = ["http://jandan.net/ooxx"]
    maxNum = 10
    current = 0

    def parse(self, response):
        item = DoubanMovieItem()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        # print 'image_urls',item['image_urls']
        yield item
        self.current = self.current + 1
        if self.maxNum > self.current:
            new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()  # 翻页
            # print 'new_url',new_url
            if new_url:
                yield Request(new_url, callback=self.parse)