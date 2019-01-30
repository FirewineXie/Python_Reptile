# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 08-ajax请求的使用.py
@time: 2019/1/19 21:15
@desc:
'''
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20"
# 明显在 limit 是 每页的显示数量，，但是也不是无限制增大
i = 0
while True:
    headers = {
        "User-Agent": UserAgent().chrome
    }

    url = base_url.format(i*20)
    request = Request(url, headers=headers)

    response = urlopen(request)
    info = response.read().decode()
    print(response.read().decode())
    if info == "" or info is None:
        break
    i+= 1
