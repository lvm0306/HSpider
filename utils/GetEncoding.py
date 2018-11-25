import requests

import chardet
ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

class GetEncoding():
    text=''

    def __init__(self,url):
        self.url=url

    def get_encode1(self):
        respone = requests.get(self.url, headers=ua_headers)
        return respone.encoding

    def get_encode2(self):
        respone = requests.get(self.url, headers=ua_headers)
        base_bianma = chardet.detect(respone.content)
        return base_bianma['encoding']