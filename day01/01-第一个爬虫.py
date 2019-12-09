#!/usr/bin/env python
# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 01-第一个爬虫.py
@time: 2019/1/18 20:52
@desc:
'''
import urllib

from urllib.request import urlopen


url = "http://www.baidu.com"


#发送请求

response = urlopen(url);


#读取内容
info = response.read()

# print(info.decode())

# 打印状态码

print(response.getcode())

#打印真实url
print(response.geturl())

#打印响应头
print(response.info())