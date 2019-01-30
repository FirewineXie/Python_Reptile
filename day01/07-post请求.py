
# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 07-post请求.py
@time: 2019/1/19 21:02
@desc:
'''
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

url = "http://www.sxt.cn/index/login/login.html"
form_data={
    "user" : "17703181473",
    "password":"123456"
}
headers = {
    "User-Agent":UserAgent().chrome
}
f_data = urlencode(form_data)
# 发送post 请求  与get请求的区别就是 有data的参数
request = Request(url,data=f_data.encode(),headers=headers)

response = urlopen(request)

print(response.read().decode())
