# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import urllib.request

class SeconddemoPipeline(object):
    def process_item(self, item, spider):
        # print(len(item['url']))
        for i in range(0, len(item['url'])):
            this_url = item['url'][i]
            id = re.findall('http://724.169pp.net/169mm/(.*?).jpg', this_url)[0]
            id = id.replace('/', '_')
            # print(id)
            file = 'D:/WorkSpace/python_ws/python-large-web-crawler/xiyangmeinv/' + id + '.jpg'
            print('Downloading :' , file)
            urllib.request.urlretrieve(this_url, filename=file)
            print('Final Download :' , file)
        return item
