#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 22-糗事百科.py
@time: 2019/1/22 23:01
@desc:
'''
import re

import requests
from fake_useragent import UserAgent

url = "https://www.qiushibaike.com/text/page/1"
headers = {

    "User-Agent":UserAgent().random
}

# 构造请求
response = requests.get(url,headers=headers)

info = response.text
infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)

with open("dunzi.txt",'w',encoding="utf-8")as f:
    for info in infos:
        f.write(info + "\n\n")

