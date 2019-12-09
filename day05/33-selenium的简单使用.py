#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 33-selenium的简单使用.py
@time: 2019/1/24 11:29
@desc:
'''
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#chrome = webdriver.Chrome(chrome_options=options)
chrome = webdriver.Chrome()
chrome.get('https://cn.bing.com/')
chrome.find_element_by_id('sb_form_q').send_keys('python')
chrome.find_element_by_id('sb_form_go').click()

html = chrome.page_source
print(html)
chrome.quit()
