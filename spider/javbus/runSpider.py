import csv

import time

from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait

chromer_driver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

base = 'https://www.busjav.icu/'
test_url = 'https://www.busjav.icu/star/tyv'
test_url2 = 'https://www.busjav.icu/MIAA-293'

cate_csv_name = 'link_name2.csv'
result_csv = 'result2.csv'


def getMovieList(link):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chromer_driver, options=option)
    driver.get(link)
    WebDriverWait(driver, 4)
    time.sleep(4)
    a_s = driver.find_elements_by_xpath('//*[@id="waterfall"]//a')
    print(driver.page_source)
    f = open(cate_csv_name, 'a+', newline='')
    csv_write = csv.writer(f)

    try:
        for i in a_s[1:]:
            print(i.get_attribute('href'))
            temp = []
            temp.append(i.get_attribute('href'))  # 链接
            csv_write.writerow(temp)
    except Exception as e:
        writeError("下载出现错误\n" + str(e))
        print(e)
    driver.close()
    pass


def getMovieInfo(link,csv_write):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chromer_driver, options=option)
    driver.get(link)
    WebDriverWait(driver, 4)
    time.sleep(4)
    a = driver.find_element_by_xpath('//*[@id="magnet-table"]/tr[1]/td[1]/a[1]')
    # print(driver.page_source)
    print(a.get_attribute('href'))
    print(a.text)
    # for i in title:
    #     print(i.text)
    #     a=i.find_elements_by_xpath('//a')
    #     print(a[0].text)
    #     print(a[0].find_elements_by_xpath('/@href'))
    # print(title.text)


    try:
        temp = []
        temp.append(link)  # 链接
        temp.append(a.get_attribute('href'))  # 链接
        csv_write.writerow(temp)
        writeInfo(link)
        writeInfo(a.get_attribute('href'))
    except Exception as e:
        writeError(link+"下载出现错误\n" + str(e))
        print(e)
    driver.close()
    pass


def writeError(info):
    with open('错误日志.txt', 'a', encoding='utf-8') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(info + "\n")  # 写入

def writeInfo(info):
    with open('内容存储.txt', 'a', encoding='utf-8') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(info + "\n")  # 写入


if __name__ == "__main__":
    # for i in range(9)[1:]:
    #     print('https://www.busjav.icu/star/tyv/' + str(i))
    #     getMovieList('https://www.busjav.icu/star/tyv/' + str(i))

    csv_file = csv.reader(open(cate_csv_name, 'r'))
    cate_list = []
    for i in csv_file:
        cate_list.append(i[0])

    for i in cate_list:
        print(i)
        try:
            f = open(result_csv, 'a+')
            csv_write = csv.writer(f)
            getMovieInfo(i,csv_write)
        except Exception as e:
            print(e)
    # getMovieInfo()
