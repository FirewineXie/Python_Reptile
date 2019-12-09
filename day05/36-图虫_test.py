#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 36-图虫_test.py
@time: 2019/1/24 15:13
@desc:
'''
import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://tuchong.com/1485770/19399344/#image351010920"
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
e = etree.HTML(response.text)
img_urls = e.xpath('//article/img/@src')

print(img_urls)

for url in img_urls:
    response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
    img_name = url[url.rfind('/')+1:]
    with open('img/'+img_name, 'wb') as f:
        f.write(response.content)
