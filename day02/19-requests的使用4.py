#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 19-requests的使用4.py
@time: 2019/1/21 1:47
@desc:
'''
import requests
from fake_useragent import UserAgent

url = "https://www.12306.cn/mormhweb/"

headers = {
    "User-Agent":UserAgent().chrome
}
requests.packages.urllib3.disable_warnings()#关闭警告

response = requests.get(url,verify=False,headers=headers)

response.encoding = "utf-8"
print(response.text)