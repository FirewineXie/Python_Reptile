#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 27-jsonpath的使用.py
@time: 2019/1/23 21:47
@desc:
'''
import json

import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath



url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)

names = jsonpath(json.loads(response.text), '$..name')
codes = jsonpath(response.json(), '$..code')

print(names)
print(codes)