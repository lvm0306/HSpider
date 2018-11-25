# # coding=utf-8
# import chardet
#
# import pytorrent
# data =open('test2.torrent','rb').read()
# print(data)
# base_bianma = chardet.detect(data)
# print(base_bianma)
# print(data.strip().decode( "Windows-1252").encode('utf-8'))
#
#
#
#
#
#
#
# coding=utf-8
import requests
import re
import os
import threading

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}


def downImg1():
    for page in range(1, 45):
        url = 'https://www.bu330.com/htm/downlist1/' + str(page) + '.htm'
        # print url
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        # print r.text.encode('utf-8')
        pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>', re.S)
        items = re.findall(pattern, r.text)
        # print items
        for item in items:
            # print item[0],item[1],item[2]
            imgname = './1/' + item[1] + '/' + item[1] + ".jpg"
            dirname = './1/' + item[1]
            try:
                os.mkdir(dirname)
                imgr = requests.get(item[2], headers=headers)

                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except:
                print()
                'pass'
                continue
            url1 = 'https://www.bu330.com' + item[0]
            # print url1
            r1 = requests.get(url1, headers=headers)
            # r1.encoding='utf-8'
            # print r1.text
            pattern1 = re.compile(r'href="https.*?=(.*?)"', re.S)
            myitems = re.findall(pattern1, r1.text)
            # print myitems
            for myitem in myitems:
                pass
            url2 = 'https://123456bt.com/download.php?ref=' + myitem
            # print url2
            r2 = requests.get(url2, headers=headers)
            name = dirname + '/' + myitem + '.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print
                    u'finish write %s' % item[1]
            except:
                continue


def downImg2():
    for page in range(1, 70):
        url = 'https://www.bu330.com/htm/downlist3/' + str(page) + '.htm'
        # print url
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        # print r.text.encode('utf-8')
        pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>', re.S)
        items = re.findall(pattern, r.text)
        # print items
        for item in items:
            # print item[0],item[1],item[2]
            imgname = './2/' + item[1] + '/' + item[1] + ".jpg"
            dirname = './2/' + item[1]
            try:
                os.mkdir(dirname)
                imgr = requests.get(item[2], headers=headers)

                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except:
                continue
            url1 = 'https://www.bu330.com' + item[0]
            # print url1
            r1 = requests.get(url1, headers=headers)
            # r1.encoding='utf-8'
            # print r1.text
            pattern1 = re.compile(r'href="https.*?=(.*?)"', re.S)
            myitems = re.findall(pattern1, r1.text)
            # print myitems
            for myitem in myitems:
                pass
            url2 = 'https://123456bt.com/download.php?ref=' + myitem

            r2 = requests.get(url2, headers=headers)
            name = dirname + '/' + myitem + '.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print
                    u'finish write %s' % item[1]
            except:
                continue


def downImg3():
    for page in range(1, 64):
        url = 'https://www.bu330.com/htm/downlist4/' + str(page) + '.htm'
        # print url
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        # print r.text.encode('utf-8')
        pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>', re.S)
        items = re.findall(pattern, r.text)
        # print items
        for item in items:
            # print item[0],item[1],item[2]
            imgname = './3/' + item[1] + '/' + item[1] + ".jpg"
            dirname = './3/' + item[1]
            try:
                os.mkdir(dirname)
                imgr = requests.get(item[2], headers=headers)

                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except IOError as e:
                continue

            url1 = 'https://www.bu330.com' + item[0]
            # print url1
            r1 = requests.get(url1, headers=headers)
            # r1.encoding='utf-8'
            # print r1.text
            pattern1 = re.compile(r'href="https.*?=(.*?)"', re.S)
            myitems = re.findall(pattern1, r1.text)
            # print myitems
            for myitem in myitems:
                pass
            url2 = 'https://123456bt.com/download.php?ref=' + myitem

            r2 = requests.get(url2, headers=headers)
            name = dirname + '/' + myitem + '.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print
                    u'finish write %s' % item[1]
            except IOError as  e:
                continue


def downImg4():
    for page in range(1, 56):
        url = 'https://www.bu330.com/htm/downlist4/' + str(page) + '.htm'
        # print url
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        # print r.text.encode('utf-8')
        pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>', re.S)
        items = re.findall(pattern, r.text)
        # print items
        for item in items:
            # print item[0],item[1],item[2]
            imgname = './4/' + item[1] + '/' + item[1] + ".jpg"
            dirname = './4/' + item[1]
            try:
                os.mkdir(dirname)
                imgr = requests.get(item[2], headers=headers)

                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except IOError as e:
                continue
            url1 = 'https://www.bu330.com' + item[0]
            # print url1
            r1 = requests.get(url1, headers=headers)
            # r1.encoding='utf-8'
            # print r1.text
            pattern1 = re.compile(r'href="https.*?=(.*?)"', re.S)
            myitems = re.findall(pattern1, r1.text)
            # print myitems
            for myitem in myitems:
                pass
            url2 = 'https://123456bt.com/download.php?ref=' + myitem
            # print url2
            r2 = requests.get(url2, headers=headers)
            name = dirname + '/' + myitem + '.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print
                    u'finish write %s' % item[1]
            except IOError as  e:
                continue


def downImg5():
    for page in range(44):
        url = 'https://www.bu330.com/htm/downlist2/' + str(page) + '.htm'
        # print url
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        # print r.text.encode('utf-8')
        pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><h3>(.*?)</h3><img src="(.*?)" /><p>', re.S)
        items = re.findall(pattern, r.text)
        # print items
        for item in items:
            # print item[0],item[1],item[2]
            imgname = './5/' + item[1] + '/' + item[1] + ".jpg"
            dirname = './5/' + item[1]
            try:
                os.mkdir(dirname)
                imgr = requests.get(item[2], headers=headers)

                with open(imgname, "wb") as code:
                    code.write(imgr.content)
            except:
                print
                'pass'
                continue
            url1 = 'https://www.bu330.com' + item[0]
            # print url1
            r1 = requests.get(url1, headers=headers)
            # r1.encoding='utf-8'
            # print r1.text
            pattern1 = re.compile(r'href="https.*?=(.*?)"', re.S)
            myitems = re.findall(pattern1, r1.text)
            # print myitems
            for myitem in myitems:
                pass
            url2 = 'https://123456bt.com/download.php?ref=' + myitem
            # print url2
            r2 = requests.get(url2, headers=headers)
            name = dirname + '/' + myitem + '.torrent'
            try:
                with open(name, "wb") as code:
                    code.write(r2.content)
                    print
                    u'finish write %s' % item[1]
            except:
                continue


if __name__ == "__main__":

    for i in range(1, 6):
        os.makedirs(str(i))
    t1 = threading.Thread(target=downImg1, args=())
    t1.start()

    t2 = threading.Thread(target=downImg2, args=())
    t2.start()

    t3 = threading.Thread(target=downImg3, args=())
    t3.start()
    t4 = threading.Thread(target=downImg4, args=())
    t4.start()
    t5 = threading.Thread(target=downImg5, args=())
    t5.start()
