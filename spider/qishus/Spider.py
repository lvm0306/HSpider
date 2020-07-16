import os
import time

from utils import DownloadUtils
from utils.DownloadUtils import DownloadBinaryFile
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup
import csv

baseurl = "https://www.qishus.com/"
# https://www.qishus.com/ 久久小说网的爬虫
def getCate():
    html = SpiderHtml(baseurl).getHtmlWithReferer(baseurl)
    bs = BeautifulSoup(html, 'html.parser')
    a_list = bs.find('ul', id='globalNavUL').find_all('a')
    print(a_list[1:])
    pass


def getPagesBefore():
    #https://www.qishus.com/xuanhuan/list1_1.html
    test_url='https://www.qishus.com/xuanhuan/list1_1.html'
    bs = SpiderHtml(test_url).getBeautifulSoup(baseurl)
    a_s=bs.find('code')
    print(a_s)
    print(type(a_s))
    a_s2=a_s.find_all('a')
    print(a_s2)
    print(type(a_s2))

    print(a_s2[-1]['href'])
    print(a_s2[-1].text)

    pass


def dowaloadTxt():
    # str="https://www.qishus.com/txt/76410.html"
    #
    # bs = SpiderHtml(str).getBeautifulSoup(baseurl)
    # down = bs.find('div',id='downAddress')
    # print(down)
    base="https://xiazai.xqishu.com"
    str="https://xiazai.xqishu.com/rar/迷茫魔法师与堕落者公会.rar"
    DownloadUtils.DownloadBinaryFileWithReferer(str, '1.rar', base).load()
    pass


def run():
    # 获取类别写入csv
    # getCate()
    # 读取csv 获取每一类得页码
    # getPagesBefore()
    # 获取每一类下得小说信息
    # getTxtList()
    # 下载小说
    dowaloadTxt()

    pass


if __name__ == "__main__":
    run()
