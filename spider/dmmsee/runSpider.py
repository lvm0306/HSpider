import csv

import time

from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'https://www.dmmsee.net/'
test_url = 'https://www.pornhd.com/category/sex-videos'


def runSpyder():
    # 获取列表  名字 - 链接 - 图片地址
    html = SpiderHtml(test_url).getHtmlWithReferer(base)
    #
    a_s = bs(html, 'html.parser').find(id ='pageContent').find_all('ul',class_='thumbs')


if __name__ == "__main__":
    runSpyder()