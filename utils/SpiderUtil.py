import requests

from utils.UserAgentSeed import *
from utils.GetEncoding import GetEncoding
from selenium import webdriver
from bs4 import BeautifulSoup as bs

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
# 需要修改
# proxies = {
#     "http": "http://121.232.148.82:9000",
# }
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

class SpiderHtml():
    def __init__(self, url):
        self.url = url
        self.driver = None

    def getHtml(self):
        respone = requests.get(url=self.url, headers=getHeaders())
        respone.encoding = GetEncoding(self.url).get_encode2()
        return respone.text

    def getHtmlWithReferer(self, referer):
        respone = requests.get(url=self.url, headers=getHeadersWithReferer(referer))
        respone.encoding = GetEncoding(self.url).get_encode2()
        return respone.text

    def getHtmlWithRefererAndProxy(self, referer):
        respone = requests.get(url=self.url, headers=getHeadersWithReferer(referer),proxies=proxies)
        respone.encoding = GetEncoding(self.url).get_encode2()
        return respone.text

    def getBeautifulSoup(self, referer):
        return bs(self.getHtmlWithReferer(referer), 'html.parser')

    def getBeautifulSoupProxy(self, referer):
        return bs(self.getHtmlWithRefererAndProxy(referer), 'html.parser')

    def driverUrl(self, url):
        if self.driver is None:
            self.driver = webdriver.Chrome('chromedriver')
        self.driver.get(url)

    def driverXpath(self,xpath):
        if self.driver is None:
            raise Exception("driver is not init")
        return self.driver.find_elements_by_xpath(xpath)

    def driverUrlXpath(self,url,xpath):
        self.driverUrl(url)
        return self.driver.find_elements_by_xpath(xpath)

    def getDriver(self):
        if self.driver is None:
            raise Exception("driver is not init")
        return self.driver