
# from utils.SpiderHelper import SpiderHelper
# url='https://www.xzw.com/fortune/aries/'
# base='https://www.xzw.com/'
# helper=SpiderHelper(base)
# helper.init()
# html=helper.getHtml(url)
# bs=helper.getBs(url=url)
# ps=bs.find('div',class_='c_cont').find_all('p')
# for i in ps:
#     print(i.strong.text +' : '+i.span.text+'\n')
# print(len(ps))


# from utils.SpiderUtil import SpiderHtml
# from bs4 import BeautifulSoup
# import requests
#
# url='https://www.ecook.cn/caipu/262972127'
# base='https://www.ecook.cn/'
# requests.get(url)
# text=SpiderHtml(url=url).getHtml2()
# bs=BeautifulSoup(text, 'html.parser')
#
#
# print('食物名')
# main=bs.find('div',class_='main_img')
# print(main.img['alt'])
# print(main.img['src'])
#
# print('所需食材')
# uls=bs.find_all('ul',class_='material_subul')
# for i in uls:
#     print(i.text)
#
# print('制作步骤')
# divs=bs.find_all('div',class_='step_one')
# for i in divs:
#     print(i.find('div','step_text').text)
#     print(i.find('div',class_='img').img['src'])


# import time
#
# from utils.SpiderHelper import *
# import json
# def getStarToday(star):
#     appkey = '88dd08554b74ada0b134b26d53ab8813'
#     url = "http://web.juhe.cn:8080/constellation/getAll"
#
#     params = {
#         "key": appkey,  # 您申请的appKey
#         "consName": star,  # 指定日期,格式为YYYY-MM-DD,如月份和日期小于10,则取个位,如:2012-1-1
#         "type":'today',
#     }
#     respone = requests.get(url, params)
#     result = ''
#     if respone.status_code == 200:
#         print()
#         bean = json.loads(respone.text)
#         name=bean['name']
#         all=bean['all']
#         color=bean['color']
#         health=bean['health']
#         love=bean['love']
#         money=bean['money']
#         number=bean['number']
#         QFriend=bean['QFriend']
#         summary=bean['summary']
#         work=bean['work']
#         result=name+':\n'+'综合指数:'+all+'\n幸运色:'+color+'\n健康指数:'+health+'\n爱情指数:'+love+'\n财运指数:'+money+'\n工作指数:'+work+'\n速配星座:'+QFriend+'\n幸运数字:'+str(number)+'\n今日总结:'+summary
#         return result
#     else:
#         return '服务器异常'
#
# def getWannianLi():
#     appkey = '487cc26fcca63fb9b10b2ce4c82d2979'
#     url = "http://v.juhe.cn/calendar/day"
#     year = time.strftime('%Y', time.localtime(time.time()))
#     month_day = time.strftime('%m-%d', time.localtime(time.time())).replace('0', '')
#     today = year + '-' + month_day
#     print(today)
#
#     params = {
#         "key": appkey,  # 您申请的appKey
#         "date": today,  # 指定日期,格式为YYYY-MM-DD,如月份和日期小于10,则取个位,如:2012-1-1
#     }
#     respone = requests.get(url, params)
#     result=''
#     if respone.status_code == 200:
#         bean = json.loads(respone.text)
#         data = bean['result']['data']
#         animalsYear = data['animalsYear']
#         avoid = data['avoid']
#         suit = data['suit']
#         lunarYear = data['lunarYear']
#         lunar = data['lunar']
#
#         result='今天是' + lunarYear + animalsYear + '年，' + '农历' + lunar + '\n忌：' + avoid + '\n宜：' + suit
#         return result
#     else:
#         return '服务器异常'
#
# def getJoke(page):
#     appkey = 'e0470cf3743375b7731b99f764d32f7e'
#     url = "http://v.juhe.cn/joke/content/list.php"
#
#     params = {
#         "sort":'desc',
#         "page":page,
#         "pagesize":5,
#         "time":str(int(time.time())),
#         "key": appkey,  # 您申请的appKey
#     }
#     respone = requests.get(url, params)
#     result=''
#     if respone.status_code == 200:
#         print(respone.text)
#         bean = json.loads(respone.text)
#         data=bean['result']['data']
#         for i in data:
#             print(i['content'])
#             print(i['updatetime'])
#         return result
#     else:
#         return '服务器异常'
#
# if __name__=='__main__':
#     getJoke(1)
#     # print(str(int(time.time())))
# import math
#
# import requests
# from selenium import webdriver

# driver = webdriver.Chrome('chromedriver')
# driver.get('https://louisalflame.github.io/CFantasyClick/index.html')
# btn=driver.find_element_by_class_name('btn btn-lg btn-default')
# for i in 10:
#     btn.click()
# 获取百度网盘链接
# url="https://www.agefans.tv/link/20190221/0"
# respone = requests.get(url=url, allow_redirects=False) # 注 allow_redirects=False是必须的
# # respone=requests.get(url=url)
# print(respone.headers['Location'])
from utils.SpiderUtil import SpiderHtml
from bs4 import BeautifulSoup as bs

url='https://www.agefans.tv/catalog/all-all-all-all-all-time-1'
base='https://www.agefans.tv'
html = SpiderHtml(url=url).getHtmlWithReferer(base)

div_s = bs(html, 'html.parser').find_all('div', class_='cell blockdiff')
print(len(div_s))
for i in div_s[0:1]:
    print(i)
    print('detail====>'+i.find('a')['href'])
    print('src====>'+i.find('a').img['src'])




