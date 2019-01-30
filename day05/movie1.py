#-*-coding:utf-8-*-
'''
Created by IntelliJ PyCharm
@author: Firewine
@contact: 1451661318@qq.com
@file: movie1.py
@time: 2019/1/24 10:34
@desc:
'''
import re
from random import randint
from time import sleep

from bs4 import BeautifulSoup
from lxml import etree

import requests
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    sleep(randint(3, 10))
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None
# 是通过xpath 来解析的
def parse_html(html):
    e = etree.HTML(html)
    all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    return ['https://maoyan.com{}'.format(url) for url in all_url]


def format_actors(actors): #用来去重
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())

    return actor_set

def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath('//h3[@class="name"]/text()')[0]
    types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a/text()')
    actors = format_actors(actors)
    return {
        "name":name,
        "types":types,
        "actors":actors
    }

def main():
    index_url = "https://maoyan.com/films"
    html = get_html(index_url)
    movie_urls = parse_html(html)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)

if __name__ == '__main__':
    main()




#下面是通过bs4来解析的
def parse_html1(html):
    soup = BeautifulSoup(html, 'lxml')
    all_a = soup.select('.channel-detail.movie-item-title > a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrs['href'])
    return ['http://maoyan.com{}'.format(url) for url in all_url]
def parse_info1(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.select('h3.name')[0].text
    types = soup.select('li.ellipsis')[0].text
    actors = soup.select('li.celebrity.actor > div.info > a')

    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }

# 通过正则表达式来获取的
def parse_html2(html):
    all_url = re.findall(r' <a href="(/films/\d+)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">',
                         html)
    return ['http://maoyan.com{}'.format(url) for url in all_url]


def parse_info2(html):
    name = re.findall(r'<h3 class="name">(.+)</h3>', html)[0]
    types = re.findall(r'<li class="ellipsis">(.+)</li>', html)[0]
    actors = re.findall(
        r'<li class="celebrity actor".+>\s+<a href="/films/cel.+>\s+<img.+>\s+</a>\s+<div.+>\s+<a.+>\s+(.+)\s+</a>',
        html)
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }

# 是通过pyquery 来解析的
from pyquery import PyQuery as pq
def parse_html3(html):
    doc = pq(html)

    all_a = doc('.channel-detail.movie-item-title a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrib['href'])
    return ['http://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    doc = pq(html)
    name = doc('h3.name')[0].text
    types = doc('li.ellipsis')[0].text
    actors = doc('li.celebrity.actor > div.info > a')
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }
