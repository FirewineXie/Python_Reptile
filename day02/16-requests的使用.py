# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 16-requests的使用.py
@time: 2019/1/21 1:31
@desc:
'''
from fake_useragent import UserAgent
import requests
headers = {
    "User-Agent" : UserAgent().chrome
}

url = "http://www.baidu.com/s"
params = {
    "wd":"尚学堂"
}

response = requests.get(url,headers=headers,params=params)

print(response.text)
