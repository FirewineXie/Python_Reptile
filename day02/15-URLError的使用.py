# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 15-URLError的使用.py
@time: 2019/1/20 16:45
@desc:
'''
from urllib.error import URLError
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

''' 
首先使用URLError 可能产生的原因：
1. 网络无连接
2. 连接不到特定的服务器
3. 服务器不存在
'''

url = "http://www.sxt2.cn/index/login/login"

headers={
    "User-Agent" : UserAgent().chrome
}
try:
    req = Request(url,headers=headers)

    resp = urlopen(req)

    print(resp.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else :
        print(e.args[0].errno)

print("访问完成")

