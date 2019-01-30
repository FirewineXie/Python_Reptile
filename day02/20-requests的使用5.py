#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 20-requests的使用5.py
@time: 2019/1/21 1:51
@desc:
'''
from fake_useragent import UserAgent
import requests

session = requests.Session()
headers = {
    "User-Agent": UserAgent().chrome
}
login_url = "http://www.sxt.cn/index/login/login"
params = {
    "user": "17703181473",
    "password": "123456"
}
response = session.post(login_url, headers=headers, data=params)

# 前面是用HTTPCookie 来保存到文件中然后读取的，
# 现在是通过session来保存的
info_url = "http://www.sxt.cn/index/user.html"
resp = session.get(info_url, headers=headers)
print(resp.text)