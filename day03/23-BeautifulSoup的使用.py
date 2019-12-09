#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine

@file: 23-BeautifulSoup的使用.py
@time: 2019/1/22 23:51
@desc:
'''


from bs4 import BeautifulSoup, Comment

str = '''
<title id="title">尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str,"lxml")

print(soup.title)
print(soup.div)

print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a["href"])


print(soup.div.string)
print(soup.div.text)

print(soup.strong.string)
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())
else :
    print(soup.strong.text)

print("---------find_all--------------")
print(soup.find_all('title'))
print(soup.find_all(id='title'))
print(soup.find_all(class_='info'))
print(soup.find_all(attrs={'float':'left'}))


print("------------css()-----------------")
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('.info'))
print(soup.select('div > span'))
print(soup.select('div span')) # 筛选过后的还是选择器 还可以select
print(soup.select('div')[1].select('a'))

