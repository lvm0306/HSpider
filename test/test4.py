import csv

import requests

from bs4 import BeautifulSoup as bs
from utils.DownloadUtils import DownloadBinaryFileWithProgressBar
#
# imageurl = 'https://xiazai.xqishu.com/txt/超神学院的咸鱼.txt'
#
# DownloadBinaryFileWithProgressBar(aim_url=imageurl,save_url='1.txt').load()
# csv_name='a.csv'
# f = open(csv_name, 'a+', newline='')
# csv_write = csv.writer(f)
#
# temp = []
# temp.append('列1')  # 链接
# temp.append('列2')  # 小说名
# csv_write.writerow(temp)
#
# temp = []
# temp.append('金融')  # 链接
# temp.append('会计')  # 小说名
# csv_write.writerow(temp)
# base_url='https://www.qishus.com'
# # url=base_url+'/wuxia/list3_1.html'
# url='https://www.qishus.com/wuxia/list3_1.html'
# ua_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
#     'Referer':base_url
# }
# respone=requests.get(url,headers=ua_headers)
# print(respone.encoding)
# respone.encoding = 'gbk'
# html=respone.text
# print(html)
# bs4=bs(html, 'html.parser')
# t_ul=bs4.find('div',id='listbox')#_class
# print(t_ul)

def run(u):
    # I = 2240 / (1.732 * 0.8 * U)
    i=2240/(1.732*0.8*u)
    print("i===="+str(i))
    pass

def run2(u):
    # I = 2240 / (1.732 * 0.8 * U)
    i=2240/(1.732*0.8*u)
    print("i===="+str(i))
    pass

if __name__ == "__main__":
    run(6.3)

