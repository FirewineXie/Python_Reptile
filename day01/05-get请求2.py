#!/usr/bin/env python
# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 05-get请求2.py
@time: 2019/1/19 20:21
@desc:
'''
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

args = {
    "wd" : "百度",
    "ie":"utf-8"
}


url = "http://www.baidu.com/s?{}".format(urlencode(args))

print(url)
headers={
    "User-Agent":UserAgent().random
}
request = Request(url,headers=headers)


response = urlopen(request)

info  = response.read()

print(info.decode())




