# 下载工具库
import time

import csv
import random
import re
import threading

from bs4 import BeautifulSoup
import requests
from contextlib import closing

# user-agent 随机种子
from utils.UserAgentSeed import argent, getHeaders,getHeadersWithReferer


class DownloadBinaryFile():

    def __init__(self, aim_url, save_url):
        self.aim_url = aim_url
        self.save_url = save_url

    def load(self):
        try:
            response = requests.get(self.aim_url + '', headers=getHeaders())
            with open(self.save_url, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print('图片下载出现错误   ' + str(e))

class DownloadBinaryFileWithReferer():

    def __init__(self, aim_url, save_url,referer):
        self.aim_url = aim_url
        self.save_url = save_url
        self.referer = referer

    def load(self):
        try:
            response = requests.get(self.aim_url + '', headers=getHeadersWithReferer(self.referer))
            with open(self.save_url, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print('图片下载出现错误   ' + str(e))

class DownloadBinaryFileWithProgressBar():

    def __init__(self, aim_url, save_url):
        self.aim_url = aim_url
        self.save_url = save_url
        self.chunk_size=1024 #默认值1024 单次长度
        self.open_log=True #默认值True 是否开启log

    def setChunkSize(self,chunk_size):
        self.chunk_size=chunk_size

    def setOpenLog(self,open_log):
        self.open_log=open_log

    def load(self):
        with closing(requests.get(self.aim_url, headers=getHeaders(), stream=True)) as response:
            content_size = int(response.headers['content-length'])  # 内容体总大小
            if self.open_log:
                print('文件总长度' + str(content_size))
            data_count = 0
            with open(self.save_url, "wb") as file:
                for data in response.iter_content(chunk_size=self.chunk_size):
                    file.write(data)
                    data_count = data_count + len(data)
                    now_jd = (data_count / content_size) * 100
                    if self.open_log:
                        print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, self.save_url), end=" ")
