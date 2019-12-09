#!/usr/bin/env python
# encoding: utf-8
'''
Created by IntelliJ PyCharm
@author: Firewine
@file: 03-fake_useragent.py
@time: 2019/1/18 21:29
@desc:
'''


from fake_useragent import UserAgent

ua = UserAgent()

print(ua.chrome)