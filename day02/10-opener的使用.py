# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 10-opener的使用.py
@time: 2019/1/20 14:19
@desc:
'''
from urllib.request import Request, build_opener, HTTPHandler

from fake_useragent import UserAgent

url = "http://www.baidu.com"

heasers={

    "User-Agent":UserAgent().chrome
}


request = Request(url,headers=heasers)
handler = HTTPHandler()
opener = build_opener(handler)

response = opener.open(request)

print(response.read().decode())