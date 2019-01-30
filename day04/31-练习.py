#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 31-练习.py
@time: 2019/1/23 23:35
@desc:
'''
from sqlite3 import connect
from xml import etree

import requests
from fake_useragent import UserAgent

url = 'http://www.farmer.com.cn/xwpd/rdjj1/201807/t20180726_1393916.htm'
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
all_p_tag = e.xpath('//div[@class="content"]//p')
content = []
for p in all_p_tag:
    info = p.xpath('string(.)')
    content.append(info)
content_str = ''.join(content)
img_urls = e.xpath('//div[@class="content"]//img/@src')
img_names = e.xpath('//div[@align="center"]')


for num in range(1, len(img_names), 2):
    img_name = img_names[num].xpath('string(.)')

client = connect(host="localhost", port=3306, user='root', password='123', db='news', charset='utf8')

cursor = client.cursor()
'select * from t_user where uname ="zs" and password ="123" or 1=1'
uname = 'zs'
password = '"123" or 1=1 '
sql = 'insert into table_name values(null,%s,%s,%s)'
cursor.execute(sql, [title, content, img_names])