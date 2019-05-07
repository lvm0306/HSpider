import csv
import json
import time

import requests

from utils.FileUtil import CsvUtil
from utils.SpiderHelper import SpiderHelper

import itchat
from itchat.content import PICTURE, TEXT, FRIENDS

name = '@225948ac7647e958aef0a0aa647ef26bd98b414f2b9027f64348c053e059671f'
myname = '@d0375b43062cc471856559312e3022b2'
she_name = '❇婧哥哥💋'
t_name = '小h'
yao_csv = 'yao.csv'
joke_page=1
laoke=1


def get_response(msg):
    KEY5 = '85f80b03da8b478381f5af2ba4188d76'

    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY5,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        print(r)
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

def findWeather(msg):
    weather = 'http://www.weather.com.cn/'
    heb = 'http://www.weather.com.cn/weather/101050101.shtml'
    helper = SpiderHelper(base=weather).init()
    bs = helper.getBs(url=heb)
    temper = bs.find(id='7d').ul.find_all('li')
    tianqi = temper[0].text.replace('\n', ' ')

    itchat.send_msg('哈尔滨天气：'+tianqi, msg['FromUserName'])
    lis = bs.find('div', class_='hide show').ul.find_all('li')
    j = 0
    for i in lis:
        # if i['class']=='li1':
        if j == 0:
            # 紫外线
            j += 1
            itchat.send_msg(i.em.text+':'+i.span.text+'\n'+i.p.text, msg['FromUserName'])
            continue
        if j == 1:
            # 减肥
            j += 1
            # print('减肥')
            continue
        if j == 2:
            # 健康
            j += 1
            # print(i.em.text)
            # print(i.span.text)
            # print(i.p.text)
            continue
        if j == 3:
            # 穿衣指数
            j += 1
            itchat.send_msg(i.em.text+':'+i.span.text+'\n'+i.p.text, msg['FromUserName'])
            continue
        if j == 4:
            # 洗车指数
            j += 1
            # print(i.em.text)
            # print(i.span.text)
            # print(i.p.text)
            continue
        if j == 5:
            # 空气污染
            j += 1
            itchat.send_msg(i.em.text+':'+i.span.text+'\n'+i.p.text, msg['FromUserName'])
            continue

def findFortune(msg,url,star):
    getStarToday(msg,star)
    base = 'https://www.xzw.com'
    helper = SpiderHelper(base)
    helper.init()
    bs = helper.getBs(url=base+url)
    ps = bs.find('div', class_='c_cont').find_all('p')
    result=''
    for i in ps:
        result+=i.strong.text +' : '+i.span.text+'\n\n'

    itchat.send_msg(result, msg['FromUserName'])

def getStarToday(msg,star):
    appkey = '88dd08554b74ada0b134b26d53ab8813'
    url = "http://web.juhe.cn:8080/constellation/getAll"

    params = {
        "key": appkey,  # 您申请的appKey
        "consName": star,  # 指定日期,格式为YYYY-MM-DD,如月份和日期小于10,则取个位,如:2012-1-1
        "type":'today',
    }
    respone = requests.get(url, params)
    result = ''
    if respone.status_code == 200:
        print()
        bean = json.loads(respone.text)
        name=bean['name']
        all=bean['all']
        color=bean['color']
        health=bean['health']
        love=bean['love']
        money=bean['money']
        number=bean['number']
        QFriend=bean['QFriend']
        summary=bean['summary']
        work=bean['work']
        result=name+':\n'+'综合指数:'+all+'\n幸运色:'+color+'\n健康指数:'+health+'\n爱情指数:'+love+'\n财运指数:'+money+'\n工作指数:'+work+'\n速配星座:'+QFriend+'\n幸运数字:'+str(number)+'\n今日总结:'+summary

        itchat.send_msg(result, msg['FromUserName'])
    else:
        itchat.send_msg('服务器异常', msg['FromUserName'])

def getWannianLi(msg):
    appkey = '487cc26fcca63fb9b10b2ce4c82d2979'
    url = "http://v.juhe.cn/calendar/day"
    year = time.strftime('%Y', time.localtime(time.time()))
    month_day = time.strftime('%m-%d', time.localtime(time.time())).replace('0', '')
    today = year + '-' + month_day
    print(today)

    params = {
        "key": appkey,  # 您申请的appKey
        "date": today,  # 指定日期,格式为YYYY-MM-DD,如月份和日期小于10,则取个位,如:2012-1-1
    }
    respone = requests.get(url, params)
    result=''
    if respone.status_code == 200:
        bean = json.loads(respone.text)
        data = bean['result']['data']
        animalsYear = data['animalsYear']
        avoid = data['avoid']
        suit = data['suit']
        lunarYear = data['lunarYear']
        lunar = data['lunar']

        result='今天是' + lunarYear + animalsYear + '年，' + '农历' + lunar + '\n忌：' + avoid + '\n宜：' + suit

        itchat.send_msg(result, msg['FromUserName'])
    else:
        itchat.send_msg('服务器异常', msg['FromUserName'])

def getJoke(msg):
    appkey = 'e0470cf3743375b7731b99f764d32f7e'
    url = "http://v.juhe.cn/joke/content/list.php"

    params = {
        "sort":'desc',
        "page":joke_page,
        "pagesize":1,
        "time":str(int(time.time())),
        "key": appkey,  # 您申请的appKey
    }
    respone = requests.get(url, params)
    if respone.status_code == 200:
        print(respone.text)
        bean = json.loads(respone.text)
        data=bean['result']['data']
        for i in data:
            itchat.send_msg(i['content'], msg['FromUserName'])
    else:
        itchat.send_msg('服务器异常', msg['FromUserName'])

# # 自动回复
@itchat.msg_register([PICTURE, TEXT, ])
def simple_reply(msg):
    print(msg)
    global laoke
    if msg['Type'] == TEXT:
        print(msg['Content'])
        if (msg['User']['NickName'] == she_name or msg['User']['NickName'] == t_name ):
            if laoke==1:
                if msg['Content'] == '天气':
                    findWeather(msg)
                if msg['Content'] == '安':
                    print(time.strftime('%Y-%m-%d  %H:%M', time.localtime(time.time())))
                    # 查询今天吃药次数，
                    nowTime1 = time.strftime('%Y/%m/%d', time.localtime(time.time()))
                    nowTime2 = time.strftime('%H:%M', time.localtime(time.time()))
                    cishu = 0
                    try:
                        reader = CsvUtil(yao_csv, 'r').read()
                        yao_list = []
                        # 准备list
                        for i in reader:
                            temp = []
                            temp.append(i[0])
                            temp.append(i[1])
                            yao_list.append(temp)
                        print(yao_list)
                        for i in yao_list:
                            if i[0] == nowTime1:
                                cishu += 1
                    except Exception as e:
                        print(e)
                    cishu+=1
                    itchat.send_msg('当前时间为' + nowTime1 + '  ' + nowTime2 + '\n晚安小婧婧，做个好梦' , msg['FromUserName'])
                    temp = []
                    temp.append(nowTime1)
                    temp.append(nowTime2)
                    write = CsvUtil(yao_csv, 'a+').getWiter()
                    write.writerow(temp)
                if msg['Content'] == '最近睡觉时间':
                    print(time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time())))
                    try:
                        reader = CsvUtil(yao_csv, 'r').read()
                        print(reader)
                        yao_list = []
                        # 准备list
                        for i in reader:
                            if len(i)==0:
                                continue
                            temp = []
                            temp.append(i[0])
                            temp.append(i[1])
                            yao_list.append(temp)
                        print(yao_list)
                        if len(yao_list) >=3:
                            lenght=len(yao_list)-3
                        else:
                            lenght=0
                        today_yao_list=yao_list[lenght:]
                        sleep_time=''
                        for i in today_yao_list:
                            sleep_time +=i[0]+' '+i[1]+'\n'
                        itchat.send_msg('最近三天的睡觉时间为:' + sleep_time, msg['FromUserName'])
                    except Exception as e:

                        itchat.send_msg('今天还没吃药', msg['FromUserName'])
                        print(e)
                if msg['Content'] == '白羊座运势':
                    star=msg['Content'][0:3]
                    print(star)
                    findFortune(msg,'/fortune/aries/',star)
                if msg['Content'] == '金牛座运势':
                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/taurus/',star)
                if msg['Content'] == '双子座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/gemini/',star)
                if msg['Content'] == '巨蟹座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/cancer/',star)
                if msg['Content'] == '狮子座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/leo/',star)
                if msg['Content'] == '处女座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/virgo/',star)
                if msg['Content'] == '天秤座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/libra/',star)
                if msg['Content'] == '天蝎座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/scorpio/',star)
                if msg['Content'] == '射手座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/sagittarius/',star)
                if msg['Content'] == '摩羯座运势':
                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/capricorn/',star)
                if msg['Content'] == '水瓶座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/aquarius/',star)
                if msg['Content'] == '双鱼座运势':

                    star=msg['Content'][0:3]
                    findFortune(msg,'/fortune/pisces/',star)
                if msg['Content']=='万年历':

                    getWannianLi(msg)
                if msg['Content']=='笑话':
                    getJoke(msg)
                    global joke_page
                    joke_page+=1
                    print(joke_page)
                if msg['Content']=='来唠嗑':
                    laoke=2
                    itchat.send_msg('开启话痨模式，回复不唠了关闭此模式', msg['FromUserName'])
                if msg['Content']=='help':
                    itchat.send_msg('当前版本:兆青青 v1.0版本 \n基本功能: \n回复天气--查看今天天气及天气指数 \n回复万年历--查看万年历\n回复笑话--讲一个笑话\n回复安--记录今天睡觉时间 \n回复最近睡觉时间--查看最近3天睡觉时间 \n高级功能:\n回复来唠嗑--开始唠嗑模式，兆青青变成话痨，问一句答一句 \n回复不唠了--关闭唠嗑模式\n注唠嗑模式下，基本功能不可以使用', msg['FromUserName'])
            else:
                if msg['Content']=='不唠了':
                    laoke=1
                    itchat.send_msg('关闭话痨模式，回复来唠嗑打开此模式', msg['FromUserName'])
                else:
                    s=get_response(msg['Text'])
                    itchat.send_msg(s, msg['FromUserName'])



    # ReplyContent = 'I received message: ' + msg['Content']
    # if msg['Type'] == PICTURE:
    #     ReplyContent = 'I received picture: ' + msg['FileName']
    # itchat.send_msg(ReplyContent, msg['FromUserName'])


## 自动添加好友
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录，微信不要开启“加好友无需验证”
#     itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 遍历好友
# friendList = itchat.get_friends(update=True)[1:]
# for friend in friendList:
#     print(friend)

itchat.auto_login(hotReload=True)
itchat.run()

# from utils.SpiderHelper import *
# from lxml import etree
# base = 'http://www.nmc.cn'
# url = 'http://www.nmc.cn/publish/forecast/AHL/haerbin.html'
# helper = SpiderHelper(base=base).init()
# html = helper.getHtml(url=url)
# selector=etree.HTML(html)
# tds=selector.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div//td//text()')
# print(tds)
