#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: 32-selenium的使用.py
@time: 2019/1/24 10:11
@desc:
'''
from selenium import webdriver

chromes = webdriver.chrome()

chromes.get("http://www.baidu.com")

chromes.save_screenshot("bjsxt.png") # 保存快照

html = chromes.page_source # 获取源代码
# chrome.quit()
