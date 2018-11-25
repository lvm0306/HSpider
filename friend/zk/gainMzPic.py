# coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup
import uuid
import requests as reqs2
import time

import chardet

# 目标抓取网页(美图)
from utils.GetEncoding import GetEncoding

src = 'https://www.mzitu.com/all'  # 带/还是不一样的
# 浏览器请求头（大部分网站没有这个请求头可能会报错）
mheaders = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


# 读取一个指定src的网页的html
def getHtml(url):
    # req = request.Request(url,headers=mheaders) #添加headers避免服务器拒绝非浏览器访问,携带请求头访问url
    respone = reqs2.get(src, headers=mheaders)
    respone.encoding = chardet.detect(respone.content)['encoding']
    print(respone.text)

    # page = request.urlopen(req)  # open request ;向指定的url发送请求
    # html = page.read()  # read数据
    # return html.decode('utf-8', errors="replace")  # python3 python2版本直接返回html>>编码utf-8格式


# 从入口爬取所有的目标链接
def getallUrl(html):
    # 构造一个bs对象>>用于解析html,也可解析xml(超文本解析器)
    soup = BeautifulSoup(html, 'html.parser')
    # 使用bs对象寻找class为all的div 然后再寻找这些div里面的a标签，可能我们需要多试几次才能准确的get
    print('html is ', html)
    all = soup.find('div', class_='all').find('ul', class_='archives').find_all('a')  # a标签列表
    print('所有的a标签长度', len(all))  # 无聊打印点什么
    for li in all:
        subSrc = li.attrs['href']  # 获取a标签中的链接
        print('subSrc is ', subSrc)  # http://www.mzitu.com/123392
        subHtml = getHtml(subSrc)  # 获取subSrc对应的html
        subSoup = BeautifulSoup(subHtml, 'html.parser')  # 构造bs对象
        # print('subHtml---->',subHtml)
        page = subSoup.find('div', class_='pagenavi').find_all('span')  # 使用bs对象寻找class为pagenavi的div,然后找到span标签
        # page[-2]是表示数组从右(末端数2个) maxpage拿到套图最后一页>>??
        maxPage = page[-2].get_text()
        i = 1
        while (i <= int(maxPage)):  # 遍历所有span中的元素
            time.sleep(0.08)  # 休息0.08s，防止服务器拒绝频繁请求
            tagetSrc = subSrc + '/' + str(i)  # >> 根据源码找到规律,拼接成图片的地址
            tagetHtml = getHtml(tagetSrc)  # >> 获取图片的html
            tagetSoup = BeautifulSoup(tagetHtml, 'html.parser')  # >>构造bs对象
            img = tagetSoup.find('div', class_='main-image').find('img')  # 使用bs对象寻找class为main-image的div,然后找到img标签
            print(time.time())  # 无聊打印点什么
            # uuid()构造一个世界唯一字符串，为了防止文件重名>>和hash一个效果?
            name = img.attrs['alt'] + str(uuid.uuid4())  # 图片文件名
            imgsrc = img.attrs['src']  # 图片地址
            print(imgsrc + "-----" + name)  # 无聊打印点什么
            try:
                # 这里的指定存储路径，需要注意的是这里需手动创建文件夹，如需自动想、可以使用os库
                request.urlretrieve(imgsrc, 'F:\\meizi\\' + '%s.jpg' % name)  # 指定目录位置
            except BaseException as e:
                # 捕获异常情况
                print('Error:there is something wrong!', e)
                # 遇到IOError: [Errno socket error] [Errno 10060]服务器拒绝频繁访问 阻塞1s
                time.sleep(1)
                try:
                    request.urlretrieve(imgsrc, 'F:\\meizi\\' + '%s.jpg' % name)  # 指定目录位置>>name是文件名字
                except BaseException:
                    print('Error:there is something wrong!over')
            # print(tagetSrc)
            i += 1
        print(
            '=======================================================end==========================================================')
        # print(li)


# 开始
print(
    '=======================================================begin======================================================')
# print(getHtml(src))
try:
    getHtml(src)
    # getallUrl(getHtml(src))
except:
    pass
