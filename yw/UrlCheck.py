import csv
import time

import requests



def run():
    f = open("url.txt", "r")
    result=[]
    for i in f.readlines():
        temp=[]
        i=i.replace('\n','')
        print('当前正在尝试连接 ：'+i)
        try:
            respone = requests.get(url=i, headers= {'User-Agent': "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"},timeout=3)
            temp.append(i)
            if respone.status_code == 200:
                temp.append(respone.status_code)
                temp.append('正常')
                print('目标服务器正常')
            else:
                temp.append(respone.status_code)
                temp.append('异常')
                print('目标服务器异常')
        except Exception as e:
            temp.append(999)
            temp.append('异常')
            temp.append(e)
            print('目标服务器可能出现了错误'+str(e))
        result.append(temp)
    with open('tt.csv', "a+", encoding="utf-8",newline='') as f:
        writer = csv.writer(f)
        for i in result:
            writer.writerow(i)
    pass


if  __name__=="__main__":
    print('-------------')
    time.sleep(1)
    run()
    print('-------------')