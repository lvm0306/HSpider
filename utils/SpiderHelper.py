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


class SpiderHelper():
    def __init__(self,base):
        self.url = ''
        self.driver = None
        self.base=base
        self.encoding=''

    def init(self):
        # 根据base 获取 encode
        self.encoding = GetEncoding(self.base).get_encode2()
        return self

    def init2(self):
        # 根据base 获取 encode
        self.encoding = GetEncoding(self.base).get_encode1()
        return self

    def getHtml(self,url):
        self.url=url
        respone = requests.get(url=self.url, headers=getHeadersWithReferer(self.base))
        respone.encoding = self.encoding
        return respone.text

    def getHtmlWithProxy(self, url):
        self.url=url
        respone = requests.get(url=self.url, headers=getHeadersWithReferer(self.base),proxies=proxies)
        respone.encoding = self.encoding
        return respone.text

    def getBs(self,url):
        return bs(self.getHtml(url), 'html.parser')

    def getBsWithProxy(self, url):
        return bs(self.getHtmlWithProxy(url), 'html.parser')

    def getDriver(self):
        self._initDriver_()
        return self.driver

    def _initDriver_(self):
        if self.driver is None:
            self.driver = webdriver.Chrome('chromedriver')

    def driverXpath(self,xpath):
        self._initDriver_()
        return self.driver.find_elements_by_xpath(xpath)

    def driverUrl(self,url):
        self._initDriver_()
        return self.driver.get(url)

