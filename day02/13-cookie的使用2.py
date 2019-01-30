# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 13-cookie的使用2.py
@time: 2019/1/20 14:46
@desc:
'''
from urllib.parse import urlencode
from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor

from fake_useragent import UserAgent


# 登录
login_url ="http://www.sxt.cn/index/login/login"

headers={

    "User-Agent":UserAgent().chrome
}
form_data ={
    "user" :" 17703181473",
    "password":"123456"
}
f_data = urlencode(form_data).encode()
request  =Request(login_url,headers=headers,data=f_data)

# response = urlopen(request)
handler = HTTPCookieProcessor()
opener = build_opener(handler)

response = opener.open(request)
print(response.read().decode())

#访问页面

info_url = "http://www.sxt.cn/index/user.html"

request = Request(info_url,headers=headers)

# response = urlopen(request)

response = opener.open(request)

print(response.read().decode())







