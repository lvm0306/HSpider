from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs
import requests


def runSpider(url):
    html = SpiderHtml(url).getHtml()
    p_s = bs(html, 'html.parser').find_all('ul', class_='archives')
    for i in p_s:
        a_s = i.find_all('a')

        print(len(a_s))


def getImage(url):
    html = SpiderHtml(url).getHtml()
    link=bs(html, 'html.parser').find('figure').find('img')['src']
    print(link)


if __name__ == "__main__":
    # runSpider('https://www.mzitu.com/all')
    getImage('https://www.mzitu.com/159605')