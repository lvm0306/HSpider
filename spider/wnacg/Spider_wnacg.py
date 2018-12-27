import csv

import time

import requests

from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs
import socks
import socket
base = 'https://www.wnacg.com/'
para = 'albums-index-'
test_url = 'https://www.javhoo.ca/actresses'


def runTag():
    soup = SpiderHtml(base).getBeautifulSoup(base)
    print(soup)
    tags = soup.find(id='tabs').find_all('a')
    with open("tags.csv", "a+", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in tags:
            list = []
            list.append(i['href'])
            list.append(i.text)
            writer.writerow(list)


def getList(url, tag):
    print(base + para + url)
    soup = SpiderHtml(base + url).getBeautifulSoup(base)
    li_s = soup.find('ul', class_='col_3_1').find_all('li')
    print('此页共' + str(len(li_s)) + '个数据')
    for i in li_s:
        # img_link,info_link,info_name,info_info
        print(i.a['href'])  # info_link
        print(i.a.img['src'])  # img_link
        print(i.find(class_='txtA').text)  # info_name
        print(i.find('span').text)  # info_info


def getListPage(url, tag):
    print()


if __name__ == "__main__":
    # 第一步
    # runTag()
    # 第二步
    csv_reader = csv.reader(open("tags.csv"))
    list = []
    for row in csv_reader:
        list.append([row[0], row[1]])

    for i in list[1:2]:
        link = i[0].split('-')
        # albums-index-cate-5.html
        # 转换
        # albums-index-page-2-cate-5.html
        print('当前进度' + link[2] + '-' + link[3] + '--' + i[1])
        getListPage(link[2] + '-' + link[3], i[1])
        # param: Link ,name
        # getList(i[0], i[1])
