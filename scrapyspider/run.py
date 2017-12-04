# -*- coding: utf-8 -*-
# @Time     : 2017/1/1 17:51
# @Author   : woodenrobot

import os
import re
import requests
import time
from scrapy import cmdline


# name = 'jiandan'
# cmd = 'scrapy crawl {0}'.format(name)
# cmdline.execute(cmd.split())
header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Policy':'no-referrer-when-downgrade',
        'Cache-Control':'max-age=300',
        'Fcache':'HIT',
        'Link':'<http://jandan.net/?p=21183>; rel=shortlink',
        'Link':'<http://jandan.net/wp-json/>; rel="https://api.w.org/"',
    }
def main():
    try:
        req = requests.get("https://www.zhihu.com/question/263549941/answer/270693862", headers=header, timeout=1000)
        print("req",req.text)
        print("req",req.headers)
        print("req",req.cookies)
    except requests.exceptions.ConnectionError:
        print("cann't connection")
    except requests.exceptions.HTTPError:
        print("http error:" + str(requests.exceptions.HTTPError))
        time.sleep(3)
    return 0

if __name__ =='__main__':
    main()