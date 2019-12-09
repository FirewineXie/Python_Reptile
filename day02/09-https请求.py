# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 09-https请求.py
@time: 2019/1/20 14:06
@desc:
'''
import ssl
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

url = "https://www.12306.cn/mormhweb/"
#虽然现在不要证书，，但是这里还是要写的



headers = {
    "User-Agent":UserAgent().chrome
}


request = Request(url,headers=headers)

# 忽略验证证书
content = ssl._create_unverified_context()

# response = urlopen(request,content=content)
response = urlopen(request)
info  = response.read().decode()

print(info)