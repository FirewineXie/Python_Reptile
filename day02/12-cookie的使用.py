# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 12-cookie的使用.py
@time: 2019/1/20 14:40
@desc:
'''
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

url= "http://www.sxt.cn/index/user.html"

heasers={

    "User-Agent":UserAgent().chrome,
    # cookie 包含了你的登录信息，我这里没有网站的账号，所以就没有写  这是第一种方式，，但是要先在网页打开登录
    "Cookie":""
}

request  =Request(url,headers=heasers)

response = urlopen(request)


print(response.read().decode())