import time

import csv

from utils.SpiderUtil import SpiderHtml
from utils import DownloadUtils

url = 'http://www.mmjpg.com/more/'
base = 'http://www.mmjpg.com/'
tag_csv_name = 'mmjpg_tags.csv"'


# 获取标签
def runTags():
    soup = SpiderHtml(url=url).getBeautifulSoup(base)
    tags = soup.find(id='morelist').find_all('li')
    print(len(tags))
    with open(tag_csv_name, "a+", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in tags:
            print(i)
            list = []
            list.append(i.a['href'])  # link
            list.append(i.a.img['src'])  # img
            list.append(i.a.img['data-img'])  # img
            list.append(i.find('i').text)  # num
            list.append(i.a.text)  # name
            writer.writerow(list)


# 获取tag下的列表页的内容
def runList():
    print()
    soup = SpiderHtml('http://www.mmjpg.com/tag/xinggan').getBeautifulSoup(base)
    li_s = soup.find(class_='pic').find('ul').find_all('li')
    print(len(li_s))
    for i in li_s:
        # 获取名字，链接
        print('链接是：' + i.a['href'])  # link
        print('名字是：' + i.find_all('span')[0].text)  # name
        print('发布时间：' + i.find_all('span')[1].text)  # time


# 获取列表数量
def getListNum(url, name):
    page = 1
    try:
        soup = SpiderHtml(url).getBeautifulSoup(base)
        page = soup.find('div', class_='page').find_all('a')[-1]['href']
        page = page.split('/')[-1]
    except Exception as e:
        print()
    print(name + "  共  " + str(page) + "页")
    return int(page)


def runInfo():
    print()
    # 需要加referer
    soup = SpiderHtml('http://www.mmjpg.com/mm/1316').getBeautifulSoup(base)
    content = soup.find('div', id='content').a.img['src']
    print(content)
    DownloadUtils.DownloadBinaryFileWithReferer(content, '1.jpg', base).load()


def getInfoNum(url, name):
    print()
    soup = SpiderHtml(url).getBeautifulSoup(base)
    page = 0
    try:
        page = soup.find('div', id='page').find_all('a')[-2].text
    except Exception as e:
        print()
    print(name+"  共"+str(page)+'页  '+'链接：'+url)
    return int(page)


if __name__ == '__main__':
    print()
    # 第一步
    # runTags()
    # 第二步
    # csv_reader = csv.reader(open(tag_csv_name))
    # list = []
    # for row in csv_reader:
    #     print(row)
    #     page=getListNum(row[0],row[-1])
    #     for i in range(page):
    #         print(row[0]+'/'+str(i+1))

    # 每获取一个标签的内容就 sleep 0.3

    # 第二步测试
    # runList()
    # 第三步测试
    # runInfo()
    getInfoNum('http://www.mmjpg.com/mm/1316','xx')
