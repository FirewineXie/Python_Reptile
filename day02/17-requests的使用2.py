#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 17-requests的使用2.py
@time: 2019/1/21 1:40
@desc:
'''

from fake_useragent import UserAgent
import requests
headers = {
    "User-Agent" : UserAgent().chrome
}

login_url = "http://www.sxt.cn/index/login/login"
params = {
    "user" : "17703181473",
    "password":"123456"
}

response = requests.post(login_url,headers=headers,data=params)

print(response.text)