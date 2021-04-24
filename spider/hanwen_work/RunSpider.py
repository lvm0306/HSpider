import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.DownloadUtils import DownloadBinaryFile
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup
import csv

default_url="https://per.spdb.com.cn/bank_financing/financial_product/?tdsourcetag=s_pctim_aiomsg"
chromer_driver='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
def run ():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chromer_driver,options=option)
    driver.get(default_url)
    WebDriverWait(driver,4)
    time.sleep(4)
    title=driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div/ul//li')
    for i in title:
        print(i.get_attribute('class'))
    print(title.text)

    # uls=driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div/div//ul')
    # for i in uls:
    #     print(i.text)



    # html=driver.page_source
    # divs=driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div/div')
    # print(divs)
    # for i in divs:
    #     print(i.text)
    # pages=driver.find_element_by_xpath('//*[@id="js_page2"]/a[last()]')
    # pages.click()
    # time.sleep(4)
    # divs2 = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div/div')
    # for i in divs2:
    #     print(i.text)
    # print()
    # #    run()
    #
    # pages=driver.find_element_by_xpath('//*[@id="js_page2"]/a[last()]')
    # print(pages.get_attribute('class'))
    pass
if __name__ == "__main__":
    run()