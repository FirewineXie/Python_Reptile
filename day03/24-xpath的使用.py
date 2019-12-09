#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 24-xpath的使用.py
@time: 2019/1/23 21:01
@desc:
'''
from lxml import etree

import requests
from fake_useragent import UserAgent

url = "https://www.qidian.com/all";

headers = {
    "User-Agent":UserAgent().random
}
response = requests.get(url,headers=headers)
e = etree.HTML(response.text)

names = e.xpath('//h4/a/text()')

authors = e.xpath('/html/body/div[2]/div[5]/div[2]/div[2]/div/ul/li/div[2]/p[1]/a[1]/text()')


# for name in range(len(names)):
#     print(names[name],":",authors[name])
#
#

for name,author in zip(names,authors):
    print(name +  " : " + author)


