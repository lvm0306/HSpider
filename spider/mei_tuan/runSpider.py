import requests
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs
import csv
# base = 'http://fine.gq/'
base = 'http://www.dianping.com/'
url = 'http://www.dianping.com/haerbin/ch30/o3'

def runSpider():

    html = SpiderHtml(url).getHtmlWithReferer(base)
    soup = bs(html, 'html.parser')
    div = soup.find_all('div',class_='content')
    ul=div[0].find_all('ul')
    lis=ul[1].find_all('li')
    print(len(lis))
    for i in lis:
        print('名字：'+i.find('img')['title'])
        print('图片地址：'+i.find('img')['src'])
        # 需要处理 svgmtsi
        print('地址：'+i.find('div',class_='tag-addr').text)

    pass

if __name__ == "__main__":
    runSpider()