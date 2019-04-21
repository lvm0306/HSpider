import os
import time

from utils.DownloadUtils import DownloadBinaryFile
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup
import csv

baseurl = "https://www.jjxs.la/"
csv_cate = 'cate.csv'
csv_cate2 = 'cate2.csv'
txt_list = 'txt_list.csv'
# https://www.jjxs.la/ 久久小说网的爬虫
def run():
    # 获取类别写入csv
    # getCate()
    # 读取csv 获取每一类得页码
    # getPagesBefore()
    # 获取每一类下得小说信息
    # getTxtList()
    # 下载小说
    dowaloadTxt()

    return 0


# 步骤六
def dowaloadTxt():
    # csv_file = csv.reader(open(txt_list, 'r'))
    # txts = []
    # for i in csv_file:
    #     temp = []
    #     temp.append(i[0])
    #     temp.append(i[1])
    #     temp.append(i[2])
    #     txts.append(temp)
    test = 'https://www.jjxs.la/txt/31534.htm'
    bs = SpiderHtml(test).getBeautifulSoup(baseurl)
    download_link = bs.find('ul', class_='downlistbox').find('a')['href']
    print(download_link)
    bs = SpiderHtml(baseurl + download_link).getBeautifulSoup(baseurl)
    trs = bs.find_all('td')[0].find_all('tr')
    for i in trs:
        a_s = i.find_all('a')
        for j in a_s:
            if j.text == 'TXT电子书下载地址【无需解压缩】':
                print(j['href'])
                folder= '穿越小说'
                if not (os.path.exists(folder)):
                    os.makedirs(folder)
                DownloadBinaryFile(baseurl + j['href'],folder+'/小说1.txt').load()
    pass


# 步骤五
def getTxtListInfo(cate, link, num):
    print('-----开始获取' + cate + str(num) + '下的小说-----')
    url = baseurl + link + 'index_' + str(num) + '.html'
    print(url)
    bs = SpiderHtml(url=url).getBeautifulSoup(baseurl)
    info_list = bs.find('div', id='catalog').find_all('div', class_='listbg')
    f = open(txt_list, 'a+', newline='')
    csv_write = csv.writer(f)

    try:
        for i in info_list:
            temp = []
            temp.append(i.a['href'])  # 链接
            temp.append(i.a['title'])  # 小说名
            date = ''
            try:
                date = i.find('span', class_='newDate').text
            except Exception as e:
                date = i.find('span', class_='oldDate').text
            temp.append(date)
            csv_write.writerow(temp)
    except Exception as e:
        print(e)

    return 0


# 步骤四 获取每页的小说信息
def getTxtList():
    csv_file = csv.reader(open(csv_cate2, 'r'))
    cate_list = []
    for i in csv_file:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        temp.append(i[2])
        cate_list.append(temp)
    for i in cate_list:
        try:
            for j in range(int(i[2])):
                try:
                    getTxtListInfo(i[0], i[1], j + 1)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    return 0


# 步骤二 读取类别csv 获取页码
def getPagesBefore():
    csv_file = csv.reader(open(csv_cate, 'r'))
    cate_list = []
    for i in csv_file:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        cate_list.append(temp)
    for i in cate_list:
        getCatePages(i[1], i[0])
        time.sleep(0.2)
    return 0


# 步骤三 分别个个类别的页码
def getCatePages(link, cate):
    html = SpiderHtml(baseurl + link).getHtml()
    bs = BeautifulSoup(html, 'html.parser')
    a_list = bs.find('div', id='pages').find_all('a')
    pages = int(a_list[-1]['href'].split('/')[-1].split('.')[0].split('_')[1])
    print(cate + ' 总页码为：' + str(pages))
    out = open(csv_cate2, 'a+', newline='')
    csv_write = csv.writer(out)
    csv_write.writerow([cate, link, pages])

    return 0


# 步骤一 获取类别
def getCate():
    html = SpiderHtml(baseurl).getHtml()
    bs = BeautifulSoup(html, 'html.parser')
    div1 = bs.find('div', id='navber').find_all('li')
    out = open(csv_cate, 'a+', newline='')
    csv_write = csv.writer(out)
    for i in div1[1:]:
        temp = []
        temp.append(i.a['title'])
        temp.append(i.a['href'])
        csv_write.writerow(temp)
    return 0


if __name__ == "__main__":
    run()
