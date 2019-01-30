#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 26-json的使用.py
@time: 2019/1/23 21:42
@desc:
'''
import json

str = '{"name":"盗梦空间"}'
print(type(str))
obj = json.loads(str)
print(type(obj))

str2 = json.dumps(obj, ensure_ascii=False)
print(type(str2), ":", str2)

json.dump(obj, open('movie.txt', 'w', encoding='utf-8'), ensure_ascii=False)

str3 = json.load(open('movie.txt',encoding='utf-8'))
print(str3)
