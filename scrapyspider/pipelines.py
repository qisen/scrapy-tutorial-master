# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
from scrapyspider import settings

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        print
        'dir_path', dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_urls']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]  # 图片名称
            # print 'filename',file_name
            file_path = '%s/%s' % (dir_path, file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path, 'wb') as file_writer:
                print("image_url",image_url)
                conn = None
                try:
                  conn = urllib.request.urlopen(image_url)  # 下载图片
                except  urllib.error.URLError as e:
                    print(e.reason)
                if conn!=None :
                   file_writer.write(conn.read())

            file_writer.close()
        return item
