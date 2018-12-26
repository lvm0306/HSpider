# url='https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f410000bd08252gd9fg6tidtt50&line=0'
url='https://translate.google.cn/translate_tts?ie=UTF-8&q=%E4%B8%8B%E8%BD%BD%E8%A7%86%E5%B1%8F%E5%89%8D%E5%85%88%E8%8E%B7%E5%8F%96%E5%88%B0%E8%A7%86%E5%B1%8F%E7%9A%84%E9%93%BE%E6%8E%A5%EF%BC%8C%E8%BF%99%E9%87%8C%E6%88%91%E5%B0%B1%E5%85%88%E9%9A%8F%E4%BE%BF%E9%80%89%E5%8F%96%E4%B8%80%E4%B8%AASRC%E4%BD%9C%E4%B8%BA%E5%8F%82%E7%85%A7&tl=zh-CN&total=1&idx=0&textlen=33&tk=240950.338665&client=t&hint=en'
# 下载实例1
#!/usr/bin/env python3
#-*- coding:utf8 -*-
# import requests
# header = {'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)'}
# response=requests.get('https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f410000bd08252gd9fg6tidtt50&line=0',headers=header,stream=True)
#
# #视频在传输过程中是以二进制流的形式传输的
#
# with open('aaa.mp4','wb') as f:
#     f.write(response.content)
# f.close

# 下载实例2
# import requests
# import datetime
# url = 'http://video.pearvideo.com/mp4/adshort/20180623/cont-1373472-12317846_adpkg-ad_hd.mp4'
# # 请求要下载的url地址
# html = requests.get(url)
# # content返回的是bytes型也就是二进制的数据。
# html = html.content
# start_time = datetime.datetime.now()
# print('开始输出时间{}'.format(start_time))
# start_down_time = datetime.datetime.now()
# print('开始下载时间{}'.format(start_down_time))
# with open('my_video.mp4','wb') as f:
#     f.write(html)
# end_time = datetime.datetime.now()
# print('下载结束时间{}'.format(end_time))



# 文件下载器 带进度条的
import requests
from contextlib import closing

def Down_load(file_url, file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    with closing(requests.get(file_url, headers=headers, stream=True)) as response:
        chunk_size = 8192  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        print('文件总长度'+str(content_size))
        data_count = 0
        with open(file_path, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, file_path), end=" ")


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    file_url = url  # 文件链接
    file_path = "mp41.mp3"  # 文件路径
    Down_load(file_url, file_path)