# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 11-proxy的使用.py
@time: 2019/1/20 14:27
@desc:
'''
from urllib.request import Request, ProxyHandler, build_opener

from fake_useragent import UserAgent

url = "http://httpbin.org/get"

heasers={

    "User-Agent":UserAgent().chrome
}

# http 是无状态的
request = Request(url,headers=heasers)
#两种写法
# handler = ProxyHandler({"https":"ip:port"})
# handler = ProxyHandler({"https":"113.13.160.30:9999"})
# handler = ProxyHandler({"https":"username:password@ip:port"})

handler = ProxyHandler({"https":"113.13.160.30:9999"})
opener = build_opener(handler)

response = opener.open(request)

print(response.read().decode())