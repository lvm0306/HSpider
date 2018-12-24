import csv

import time

from utils.DownloadUtils import DownloadBinaryFile
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'http://qingyule9.com/'
folder = "F:\space\\torrent\\qyl9"
test_url = 'http://qingyule9.com/vod-type-id-1-pg-1.html'

def runSpyder(url, name):
    # 获取列表  名字 - 链接 - 图片地址
    html = SpiderHtml(url).getHtmlWithReferer(base)

    # 获取页码
    page = 0
    page_url=''
    try:
        a_s = bs(html, 'html.parser').find('div', class_='pages').find_all('a')
        if (len(a_s) > 1):
            page = a_s[-1]['href'].split('.')[0].split('-')[-1]
            page_url = "-".join(a_s[-1]['href'].split('.')[0].split('-')[:-1])
            print(page_url)
    except Exception as e:
        print(name + "只有一页哦~" + str(e))

    print(name + "该分类下共" + page)

    try:
        for i in range(int(page)):
            print('此分类是'+name+"当前是第" + str(i + 1) + "页,"+"链接为"+base+str(page_url)+'-'+str(i+1)+'.html')
            spider_title(base+str(page_url),name)
            time.sleep(0.3)

    except Exception as e:
        print("出错了~~")

def spider_title(url, name):
    # 获取列表  名字 - 链接 - 图片地址
    html = SpiderHtml(url).getHtmlWithReferer(base)

    li_s = bs(html, 'html.parser').find('ul', class_='videos').find_all('li')
    # 写入csv
    with open("test.csv", "a+", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in li_s:
            list = []
            list.append(name)
            list.append(i.div.a['href'])#链接
            list.append(i.div.a['title'])#标题
            list.append(i.div.a.div.img['src'])#图片链接
            writer.writerow(list)

def getType():
    html = SpiderHtml(test_url).getHtmlWithReferer(base)
    li_s = bs(html, 'html.parser').find('ul', class_='menu').find_all('li')[1:]
    for i in li_s:
        print('当前进行的是'+i.a.text+i.a['href'])
        runSpyder(base+str(i.a['href']),i.a.text)
        time.sleep(1)

if __name__ == "__main__":
    getType()