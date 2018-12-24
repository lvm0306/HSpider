import csv

import time

from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'https://www.javhoo.ca/'
test_url = 'https://www.javhoo.ca/actresses'



def runStarName():
    # 获取列表  名字 - 链接 - 图片 - 详情
    html = SpiderHtml(test_url).getHtmlWithReferer(base)
    div_s=bs(html,'html.parser').find(id='content').find_all(class_='wf-container loading-effect-none iso-container description-on-hover hover-style-two hover-fade content-align-left')[0].find_all('article')
    print(div_s[0])
    for article in div_s:
        print("演员的名字"+article.div.a['href'].split('/')[-1])
        print("演员的链接"+article.div.a['href'])
        print("演员的图片"+article.div.a.img['data-src'])
        print("演员的详情"+article.find('div',class_='testimonial-content').text)


def runStarList():
    #测试
    html = SpiderHtml("https://www.javhoo.ca/star/%E6%B3%A2%E5%A4%9A%E9%87%8E%E7%B5%90%E8%A1%A3").getHtmlWithReferer(base)
    div_s=bs(html,'html.parser').find(class_='wf-container loading-effect-fade-in iso-container bg-under-post description-under-image content-align-left').find_all('article')
    print("本页共"+len(div_s)+"个")
    # 第一个是演员介绍
    # 其他为演绎作品
    # 目标 ：获取作品名字，作品图片，作品详情，番号名，出版日日期
    for div in div_s[1:]:
        print("作品详情页"+div.a['href'])
        print("作品名字"+div.a['title'])
        print("作品图片"+div.a.img['data-src'])
        print("番号名"+div.find('date').text.split('/')[0])
        print("出版日期"+div.find('date').text.split('/')[1])


def runMovieLink():

    html = SpiderHtml("https://www.javhoo.ca/av/juy-578").getHtmlWithReferer(base)
    div_s=bs(html,'html.parser').find(id='comments').find_all('a')
    print("共"+str(len(div_s))+"个资源可用")
    print(div_s[-1])
    print('磁力链接名字：'+div_s[-1]['title'])
    print('磁力链接地址：'+div_s[-1]['href'])
    print('内容大小'+div_s[-2].text)
    print('分享时间：'+div_s[-1].text)

if __name__ == "__main__":
    runMovieLink()
