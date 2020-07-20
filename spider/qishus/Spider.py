import os
import time

from utils import DownloadUtils
from utils.DownloadUtils import DownloadBinaryFile
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup
import csv
from bs4 import BeautifulSoup as bs

baseurl = "https://www.qishus.com/"
cate_csv_name = "qishius.csv"
note_csv_name = "xiaoshuo_title.csv"


# https://www.qishus.com/ 久久小说网的爬虫
def getCate():
    html = SpiderHtml(baseurl).getHtmlWithReferer(baseurl)
    bs = BeautifulSoup(html, 'html.parser')
    ul = bs.find('ul', id='globalNavUL')
    print(ul)
    a_list = ul.find_all('a')
    print(a_list[1:])

    f = open(cate_csv_name, 'a+', newline='')
    csv_write = csv.writer(f)

    try:
        for i in a_list[1:]:
            print(i)
            temp = []
            temp.append(i['href'])  # 链接
            temp.append(i['title'])  # 小说名
            csv_write.writerow(temp)
    except Exception as e:
        print(e)
    pass


def getPagesBefore():
    # https://www.qishus.com/xuanhuan/list1_1.html
    test_url = 'https://www.qishus.com/xuanhuan/list1_1.html'
    bs = SpiderHtml(test_url).getBeautifulSoup(baseurl)
    a_s = bs.find('code')
    print(a_s)
    print(type(a_s))
    a_s2 = a_s.find_all('a')
    print(a_s2)
    print(type(a_s2))

    print(a_s2[-1]['href'])
    print(a_s2[-1].text)

    pass


def dowaloadTxt():
    # str="https://www.qishus.com/txt/76410.html"
    # bs = SpiderHtml(str).getBeautifulSoup(baseurl)
    # down = bs.find('div',id='downAddress')
    # print(down)
    base = "https://xiazai.xqishu.com"
    # str = "https://xiazai.xqishu.com/txt/神武天帝.txt"
    # https: // xiazai.xqishu.com / txt / 星兽王.txt
    str1 = "https://xiazai.xqishu.com/txt/%s.txt"
    csv_file = csv.reader(open("t.csv", 'r', encoding='gb2312'))

    folder = "D:\\space\\py_space\\spider\\spider\\qishus\\down\\"
    cate_list = []
    for i in csv_file:
        print(str1%i[0])
        try:
            DownloadUtils.DownloadBinaryFileWithReferer(str1%i[0], folder+i[0]+'.txt', base).load()
        except Exception as e:
            writeError("下载"+ i[0]+"出现错误\n"+str(e))
            print("下载"+ i[0]+"出现错误\n"+str(e))

    pass


def getCSV():
    csv_file = csv.reader(open(cate_csv_name, 'r'))
    cate_list = []
    for i in csv_file:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        temp.append(int(i[2]))
        cate_list.append(temp)
        print(temp)
        getTxtList(i[0], i[2], i[1])

    pass


def getTxtList(link, page, title):
    base = "https://www.qishus.com"
    link1 = base + link
    print("当前开始爬取===" + title)
    for i in range(int(page))[1:]:
        time.sleep(0.3)
        print("第" +str(i)+"页==="+ title)
        _links=link1.split("_")
        print(_links[0]+"_"+str(i)+".html")
        try:
            html = SpiderHtml(_links[0]+"_"+str(i)+".html").getHtmlWithReferer(baseurl)
            bs1 = bs(html, 'html.parser')
            divs = bs1.find_all('div', class_="mainListInfo")
            # print(divs)
            # print(len(divs))
            if len(divs)!=0:
                for i in range(len(divs)):
                    note_title=divs[i].find_all('a')[0]['title']
                    note_title=note_title.replace("TXT全集下载", "").replace(" ", "")
                    # print(note_title)
                    writeCsv(note_title)

            if len(divs) == 0:
                divs2 = bs1.find_all('div', class_="list_b")
                # print(divs2)
                # print(len(divs2))
                # print(divs2[0])
                for i in range(len(divs2)):
                    note_title=divs2[i].find_all('a')[0]['title']
                    note_title=note_title.replace("TXT全集下载", "").replace(" ", "")
                    # print(note_title)
                    writeCsv(note_title)
        except Exception as e:
            writeError("第" +str(i)+"页==="+ title+"出现错误\n"+str(e))
            print("第" +str(i)+"页==="+ title+"出现错误\n"+str(e))

    # bs=SpiderHtml(str).getBeautifulSoup(baseurl)
    # divs= bs.find_all('div',class_="mainListInfo")
    # print(divs)
    # print(len(divs))
    pass


def checkCSV():

    csv_file = csv.reader(open(note_csv_name, 'r', encoding='UTF-8'))
    cate_list = []
    for i in csv_file:
        f = open("t.csv", 'a+', newline='',encoding="gb2312")
        csv_write = csv.writer(f)
        temp = []
        temp.append(i[0])
        # print(temp)
        try:
            cate_list.append(temp)
            csv_write.writerow(temp)
        except Exception as e:
            writeError("保存" + i[0] + "出现问题" + str(e))
            print("保存" + i[0] + "出现问题" + str(e))
    print(len(cate_list))
    pass


def run():
    # 获取类别写入csv
    # getCate()
    # getCSV()
    # 读取csv 获取每一类得页码
    # getPagesBefore()
    # 获取每一类下得小说信息
    # getTxtList()
    # 下载小说
    dowaloadTxt()

    # checkCSV()
    # print('\ufffd')
    pass


def writeError(info):
    with open('错误日志.txt', 'a',encoding='utf-8') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(info+"\n")  # 写入

def writeCsv(name):
    try:
        f = open(note_csv_name, 'a+', newline='',encoding='utf-8')
        csv_write = csv.writer(f)
        temp = []
        temp.append(name)  # 链接
        csv_write.writerow(temp)
    except Exception as e:
        writeError("保存"+name+"出现问题"+str(e))

if __name__ == "__main__":
    run()
