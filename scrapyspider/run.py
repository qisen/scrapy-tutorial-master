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
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
def main():
    try:
        req = requests.get("http://jandan.net/ooxx", headers=header, timeout=1000)
        print("req",req.text)
    except requests.exceptions.ConnectionError:
        print("cann't connection")
    except requests.exceptions.HTTPError:
        print("http error:" + str(requests.exceptions.HTTPError))
        time.sleep(3)
    return 0

if __name__ =='__main__':
    main()