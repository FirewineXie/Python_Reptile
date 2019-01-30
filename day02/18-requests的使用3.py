#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 18-requests的使用3.py
@time: 2019/1/21 1:43
@desc:
'''
import requests
from fake_useragent import UserAgent

url = "http://httpbin.org/get"

headers = {
    "User-Agent":UserAgent().chrome
}
proies ={
    "https" :"113.13.160.30:9999"
}


response = requests.get(url,headers=headers,proxies=proies)


print(response.text)


requests.get(url,headers=headers)