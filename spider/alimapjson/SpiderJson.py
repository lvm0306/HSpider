import os
import time

from selenium.webdriver.android import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import csv
from bs4 import BeautifulSoup as bs

from utils.FileUtil import CsvUtil
from utils.SpiderUtil import SpiderHtml

base = 'http://www.mca.gov.cn/'
url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html'
chromer_driver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
cate_file = 'cate5.csv'
nowProvence = ''
nowCity = ''
nowQu = ''
nowfile = ''


def getCate():
    html = SpiderHtml(url).getHtmlWithReferer(base)
    soup = bs(html, 'html.parser')
    divs = soup.find_all('tr')
    write = CsvUtil(cate_file, 'a+')
    print(len(divs))
    for i in divs[3:]:
        tds = i.find_all('td')
        a = []
        for j in tds[1:3]:
            temp = j.text
            t = temp.replace(' ', '')
            t = t.replace('\xa0', '')
            a.append(t)
            print(t + '---' + str(t.isdigit()))
            if not t.isdigit():
                cishu2 = temp.count('\xa0')
                a.append(cishu2)
        write.write(a)


def downloadJson():
    with open(cate_file, 'r') as f:
        reader = csv.reader(f)
        # temp 中断变量
        temp = False
        for row in reader:
            print(row)
            # 如果是等于0 就是省 要新建省级目录
            if row[2] == '0':
                nowProvence = row[1]
                nowCity = ''
            if row[2] == '1':
                nowCity = row[1]
            print('当前='+row[0] )
            if row[0] == '450311':
                temp = True

            if temp:
                try:
                    if nowCity == '':
                        download(row[0], '全国/' + nowProvence, row[1])
                        continue

                    download(row[0], '全国/' + nowProvence + '/' + nowCity, row[1])

                except Exception as e:
                    info = '下载失败' + 'https://geo.datav.aliyun.com/areas_v3/bound/' + row[0] + '.json'
                    writeError(info)
                    print(e)
    pass


def download(code, filefold, name):
    if not (os.path.exists(filefold)):
        os.makedirs(filefold)
    print('正在下载' + 'https://geo.datav.aliyun.com/areas_v3/bound/' + code + '.json')
    html = SpiderHtml('https://geo.datav.aliyun.com/areas_v3/bound/' + code + '.json').getHtmlWithReferer(
        'https://geo.datav.aliyun.com/')

    with open(filefold + '\\' + name + '.json', "w") as file:  #
        file.write(html)
    writeInfo('下载成功:' + 'https://geo.datav.aliyun.com/areas_v3/bound/' + code + '.json')
    writeInfo('下载路径:' + filefold + '\\' + name)
    pass


def writeError(info):
    with open('错误日志.txt', 'a', encoding='utf-8') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(info + "\n")  # 写入


def writeInfo(info):
    with open('内容存储.txt', 'a', encoding='utf-8') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(info + "\n")  # 写入


if __name__ == "__main__":
    # 获取类别    #给类别做标记 把省市区 区分开来
    # getCate()
    # 下载json
    downloadJson()
    # html = SpiderHtml('https://geo.datav.aliyun.com/areas_v3/bound/110119.json').getHtmlWithReferer('https://geo.datav.aliyun.com/')
    # print(html)
