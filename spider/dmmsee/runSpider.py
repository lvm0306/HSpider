import csv

import time

from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'https://www.dmmsee.net/'
test_url = 'https://www.dmmsee.net/actresses'
# base = 'https://dd9871.com/'
# test_url = 'https://dd9871.com/'


def runStarName():
    # 获取列表  名字 - 链接 - 图片地址
    html = SpiderHtml(test_url).getHtmlWithReferer(base)
    div_s=bs(html,'html.parser').find_all('div',class_='item')
    for div in div_s:
        print("演员的名字"+div.a.div.img['title'])
        print("演员的链接"+div.a['href'])
        print("演员的图片"+div.a.div.img['src'])


    #
    # a=bs(html,'html.parser').find(class_="row")
    # print(a)
    # div_s = bs(html, 'html.parser').find('div',class_='masonry').find_all('div',class_='item masonry-brick')
    # print(div_s)
    # for div in div_s:
    #     print("演员的名字"+div.find('div',class_='photo-frame').img['title'])
    #     print("演员的链接"+div.a['href'])
    #     print("演员的图片"+div.find('div',class_='photo-frame').img['src'])

def runStarList():
    #测试
    html = SpiderHtml("https://www.dmmsee.net/star/2pv").getHtmlWithReferer(base)
    div_s=bs(html,'html.parser').find('div',id="waterfall").find_all('div',class_='item')
    print(div_s[1])
    # 第一个是演员介绍
    # 其他为演绎作品
    # 目标 ：获取作品名字，作品图片，作品详情，番号名，出版日日期
    print("作品详情页"+div_s[1].find('a',class_='movie-box')['href'])
    print("作品名字"+div_s[1].find('div',class_='photo-frame').img['title'])
    print("作品图片"+div_s[1].find('div',class_='photo-frame').img['src'])
    print("番号名"+div_s[1].find_all('date')[0].text)
    print("出版日期"+div_s[1].find_all('date')[1].text)
    #详情也需要chrome driver

def runMovieLink():

    html = SpiderHtml("https://www.javhoo.ca/av/juy-578").getHtmlWithReferer('https://www.javhoo.ca')
    div_s=bs(html,'html.parser').find(id='comments').find_all('a')
    print(div_s)

if __name__ == "__main__":
    runMovieLink()
