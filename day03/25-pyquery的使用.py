#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 25-pyquery的使用.py
@time: 2019/1/23 21:24
@desc:
'''
import requests
from fake_useragent import UserAgent
from pyquery import PyQuery  as pq
url = "https://www.xicidaili.com/nn/"

headers ={
    "User-Agent" : UserAgent().random
}

response = requests.get(url,headers=headers)

doc = pq(response.text)
trs = doc('#ip_list tr') #可以通过标签也可以是选择器
for num in range(1,len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    type = trs.eq(num).find('td').eq(5).text()
    print(ip + " : " + port +"  :  " + type)