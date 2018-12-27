from utils.DownloadUtils import DownloadBinaryFile, DownloadBinaryFileWithReferer
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs
import requests
import os

from urllib import request as req
# base = 'https://www.mzitu.com/all'
folder = "F:\space\\torrent\\meizitu"

base = 'https://www.mzitu.com'

def runSpider(url):
    html = SpiderHtml(url).getHtmlWithReferer(base)
    p_s = bs(html, 'html.parser').find_all('ul', class_='archives')
    for i in p_s:
        a_s = i.find_all('a')
        for j in a_s:
            # 获取所有的图片网址
            print(j['href'])
            print(j.text)
            getImageUrl(j['href'], j.text)


def getImageUrl(url, name):
    html = SpiderHtml(url).getHtmlWithReferer(base)
    soup = bs(html, 'html.parser')
    page = int(soup.find(class_='pagenavi').find_all('a')[-2].span.text)  # 获取页码
    for i in range(page):
        html = SpiderHtml(url + '/' + str(i)).getHtmlWithReferer(base)
        image_link = bs(html, 'html.parser').find('div', class_='main-image').p.a.img['src']
        print(name)
        print(image_link)
        #判断地址是否存在
        if not (os.path.exists(folder+'\\'+name)):
            os.makedirs(folder+'\\'+name)
        DownloadBinaryFileWithReferer(aim_url=image_link,
                                      save_url=folder+'\\'+name+'\\'+str(i)+'.jpg',
                                      referer=base).load()
        # req.urlretrieve(image_link,folder+'\\'+name+'\\'+str(i)+'.jpg')
    # link = soup.find('figure').find('img')['src']
    # print(link)

if __name__ == "__main__":
    runSpider('https://www.mzitu.com/all')
    # getImageUrl('https://www.mzitu.com/159605')
