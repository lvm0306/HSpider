import csv

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


url='https://www.ecook.cn/caipu/262972127'
base='https://www.ecook.cn/'
from utils.SpiderHelper import SpiderHelper
sh=SpiderHelper(base).init2()
html=sh.getHtml(url)
print(html)