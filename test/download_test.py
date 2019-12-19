from utils.DownloadUtils import DownloadBinaryFileWithProgressBar,DownloadBinaryFile

import requests

from utils.UserAgentSeed import argent, getHeaders,getHeadersWithReferer

from urllib import request as req
imageurl = 'http://t2.hddhhn.com/uploads/tu/201810/9999/9822b56d58.jpg'
videourl = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f410000bd08252gd9fg6tidtt50&line=0'
radiourl = 'https://translate.google.cn/translate_tts?ie=UTF-8&q=%E4%B8%8B%E8%BD%BD%E8%A7%86%E5%B1%8F%E5%89%8D%E5%85%88%E8%8E%B7%E5%8F%96%E5%88%B0%E8%A7%86%E5%B1%8F%E7%9A%84%E9%93%BE%E6%8E%A5%EF%BC%8C%E8%BF%99%E9%87%8C%E6%88%91%E5%B0%B1%E5%85%88%E9%9A%8F%E4%BE%BF%E9%80%89%E5%8F%96%E4%B8%80%E4%B8%AASRC%E4%BD%9C%E4%B8%BA%E5%8F%82%E7%85%A7&tl=zh-CN&total=1&idx=0&textlen=33&tk=240950.338665&client=t&hint=en'
image_pathurl = 'image.jpg'
video_pathurl = 'mp4.mp4'
radio_pathurl = 'mp3.mp3'
txt_url='https://www.jjxs.la/e/DownSys/doaction.php?enews=DownSoft&classid=47&id=31513&pathid=0&pass=ee247a67a5adcf1dfb1abecbd1ff5635&p=:::'
# dfwp=DownloadBinaryFileWithProgressBar(aim_url=imageurl,save_url=image_pathurl)
# dfwp.load()
# DownloadBinaryFileWithProgressBar(aim_url=imageurl,save_url=image_pathurl).load()
# DownloadBinaryFile(aim_url='https://i.meizitu.net/2018/11/21c31.jpg',save_url='F:\space\\torrent\meizitu\甜美御姐五官精致 丰满好身材衣服都要绷不住了'+'\\1.jpg').load()
# DownloadBinaryFileWithProgressBar(aim_url=txt_url,save_url='1.txt').load()
# req.urlretrieve('https://i.meizitu.net/2018/11/21c01.jpg','1.jpg')txt_url
# respone=requests.get(txt_url,headers=getHeaders())
#
# with open('1.txt','wb') as f :
#     f.write(respone.content)
# req.urlretrieve('https://i.meizitu.net/2018/11/21c01.jpg','1.jpg')
DownloadBinaryFileWithProgressBar(aim_url=imageurl,save_url='1.jpg').load()
DownloadBinaryFile(aim_url=txt_url,save_url='2.txt').load()