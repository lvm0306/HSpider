import csv

import time

from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'http://qingyule9.com/'
test_url = 'http://qingyule9.com//vod-play-id-20592-src-1-num-1.html'


def runSpyder():
    # 获取列表  名字 - 链接 - 图片地址
    html = SpiderHtml(test_url).getHtmlWithReferer(base)
    # 需要 用到chrome 所以暂不考虑，尝试播放网页
    # a_s = bs(html, 'html.parser').find(id ='playleft')
    # print(a_s)


if __name__ == "__main__":
    runSpyder()
