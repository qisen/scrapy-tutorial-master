# -*- coding: utf-8 -*-
# @Time     : 2017/1/1 17:51
# @Author   : woodenrobot

import os
import re
import requests
import time
from scrapy import cmdline
from selenium import webdriver
from scrapy.http import HtmlResponse
import time


name = 'jiandan'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
# header={
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Encoding':'gzip, deflate',
#         'Accept-Language':'zh-CN,zh;q=0.8',
#         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
#         'Policy':'no-referrer-when-downgrade',
#         'Cache-Control':'max-age=300',
#         'Fcache':'HIT',
#         'Link':'<http://jandan.net/?p=21183>; rel=shortlink',
#         'Link':'<http://jandan.net/wp-json/>; rel="https://api.w.org/"',
#     }
# def main():
#     try:
#         driver = webdriver.PhantomJS(
#             executable_path='D:/用户目录/下载/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')  # 指定使用的浏览器
#         # driver = webdriver.Firefox()
#         driver.get("http://jandan.net/ooxx")
#         time.sleep(1)
#         js = "var q=document.documentElement.scrollTop=10000"
#         driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
#         time.sleep(3)
#         body = driver.page_source
#         print("body", body)
#     except requests.exceptions.ConnectionError:
#         print("cann't connection")
#     except requests.exceptions.HTTPError:
#         print("http error:" + str(requests.exceptions.HTTPError))
#         time.sleep(3)
#     return 0
#
# if __name__ =='__main__':
#     main()