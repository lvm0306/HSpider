import os
import time

import pymysql
import xlrd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.MysqlUtil import MysqlUtil
from utils.SpiderUtil import SpiderHtml

from bs4 import BeautifulSoup as bs

helper = None
base = 'https://xueshu.baidu.com'
default_url = "https://xueshu.baidu.com/s?wd=Weaving+the+Web+of+ER+Tubules&rsv_bp=0"

chromer_driver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'


def runSpider():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chromer_driver, options=option)
    driver.get(default_url)
    WebDriverWait(driver, 4)
    time.sleep(2)  # 获取到网页数据
    div_1 = driver.find_elements_by_xpath('//*[@id="top_hint"]/div/div/div[1]/h3/a')
    print(div_1[0].get_attribute('href'))

    driver.quit()
    # html = SpiderHtml(default_url).getHtmlWithReferer(base)
    # print(html)
    # ids=bs(html,'html.parser').find('id', id='top_hint')
    # print(ids)
    driver.quit()
    pass


def runSpider2(url):

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chromer_driver, options=option)
    driver.get(url)
    WebDriverWait(driver, 4)
    time.sleep(2)  # 获取到网页数据

    # 全局获取
    cates = driver.find_elements_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]//div')
    cates = driver.find_elements_by_xpath('//*[@class="c_content"]//div')
    print(len(cates))
    for i in cates:
        lists = i.text.split('\n')
        if lists[0] == '作者：':
            print('作者：')
            print(lists[1])
        if lists[0] == '摘要：':
            print('摘要：')
            print(lists[1])
        if lists[0] == '关键词：':
            print('关键词：')
            a_s = i.find_elements_by_xpath('.//a')
            for j in a_s:
                print(j.text)
            print(lists[1])
        if lists[0] == 'DOI：':
            print('DOI：')
            print(lists[1])
        if lists[0] == '被引量：':
            print('被引量：')
            print(lists[1])
        if lists[0] == '年份：':
            print('年份：')
            print(lists[1])

    # 研究点分析
    yanjiudian = driver.find_element_by_xpath('//*[@id="dtl_r"]/div[3]/div')
    lists = yanjiudian.text.split('\n')
    if lists[0] == '研究点分析':
        print('研究点分析：')
        for i in lists[1:]:
            print(i)
    driver.quit()

    # auther=driver.find_element_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]/div[2]/p[2]')
    # print(auther.text)
    # authers=auther.text.split('，')
    # print('作者:')
    # print(authers)
    #
    # zhaiyao=driver.find_element_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]/div[3]/p[2]')
    # print('摘要:')
    # print(zhaiyao.text)
    #
    #
    #
    #
    # guanjianci=driver.find_elements_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]/div[4]/p[2]//a')
    # title=driver.find_element_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]/div[4]/p[1]')
    # print(title.text)
    # print('关键词：')
    # print(len(guanjianci))
    # for i in guanjianci:
    #     print(i.text)
    # # print(guanjianci[0].text)
    #
    # zhaiyao=driver.find_element_by_xpath('//*[@id="dtl_l"]/div[1]/div[1]/div[5]/p[2]')
    # print(zhaiyao.text)
    #
    #
    # # 研究点分析
    # div_1 = driver.find_element_by_xpath('//*[@id="dtl_r"]/div[3]/div')
    # print(div_1.text)
    # print(div_1.text)

    # text = driver.find_element_by_xpath('//*[@class="c_content"]')
    # print(text.text)

    # html = SpiderHtml(testurl).getHtmlWithReferer(base)
    # print(html)
    # ids=bs(html,'html.parser').find('div', class_='main-info')
    # print(ids)
    pass


def useDb():

    mu = MysqlUtil(host='127.0.0.1', user='root', psw='shi123456', db='shi')
    mu.init()
    # 读取excel 数据
    workBook = xlrd.open_workbook('list.xlsx')
    allSheetNames = workBook.sheet_names()
    print(allSheetNames)
    sheet1_content1 = workBook.sheet_by_index(0)
    print(sheet1_content1.name, sheet1_content1.nrows, sheet1_content1.ncols);
    # num=1
    dblist=[]
    for i in range(sheet1_content1.nrows):
        print(sheet1_content1.row_values(i))
        temp=[]
        temp.append(pymysql.escape_string(sheet1_content1.row_values(i)[0]))
        temp.append(pymysql.escape_string(sheet1_content1.row_values(i)[1]))
        temp.append(pymysql.escape_string(sheet1_content1.row_values(i)[2]))
        dblist.append(temp)
    num_tuple = tuple(dblist)
    print(num_tuple)
    sql = "insert into xueshulist(xueshu_year,xueshu_cate,xueshu_name ) " \
          "values(%s,%s,%s)"
    mu.executeSqlmany(sql,num_tuple)

        # print('正在执行'+str(num)+'条')
        # num=num+1
        # try:
        #      mu.executeSql(sql)
        # except  Exception as e:
        #     print('插入'+str(num)+'时出错')
        #     print(sheet1_content1.row_values(i))
        #     print(e)
        #     pass

    pass


if __name__ == '__main__':
    useDb()


    # 找到目标
    # runSpider()
    # 详情获取
    # testurl = 'https://xueshu.baidu.com/usercenter/paper/show?paperid=c254b384f13089b07a6b9a0cab51354e&site=xueshu_se'
    # runSpider2(testurl)


    pass
