#!/usr/bin/env python
# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 04-get请求1.py
@time: 2019/1/18 21:43
@desc:
'''
from random import choice
from urllib.request import Request, urlopen

url = "https://www.baidu.com/s?wd=尚学堂"


user_agents=["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
             "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
             "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"]
headers = {
    "User-Agent" : choice(user_agents)

}
request = Request(url,headers=headers)

response = urlopen(request)


print(response.read())
