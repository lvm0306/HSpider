import time

from utils.MysqlUtil import MysqlUtil
from utils.SpiderHelper import SpiderHelper
from bs4 import BeautifulSoup
from utils.FileUtil import *
import requests

cate_url = 'https://www.ecook.cn/caipu/'
base = 'https://www.ecook.cn/'
helper = None
cate_csv = 'cate2.csv'


# 获取分类
def getCate():
    bs = helper.getBs(cate_url)
    divs = bs.find_all('div', class_='recipe_class')
    write = CsvUtil(cate_csv, 'a+').getWiter()
    for i in divs:
        cate = i.h3.text
        lis = i.find_all('li')
        for j in lis:
            temp = []
            temp.append(j.a.span.text)
            temp.append(j.a['href'])
            temp.append(cate)
            write.writerow(temp)
    pass


# 初始化工具
def init():
    global helper
    helper = SpiderHelper(base).init2()
    pass


def getList():
    reader = CsvUtil(cate_csv, 'r').read()
    cate_list = []
    # 准备list
    for i in reader:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        temp.append(i[2])
        cate_list.append(temp)

    # 遍历分类
    for i in cate_list:
        try:
            bs = helper.getBs(base + i[1])
            page = bs.find('div', class_='pagediv').find_all('a')[-2]
            mu = MysqlUtil(host='127.0.0.1', user='root', psw='', db='love')
            mu.init()
            print('当前是' + i[0])
            for j in range(int(page.text))[1:]:
                try:
                    print('当前是  ' + base + i[1] + '?page=' + str(j))
                    bs = helper.getBs(base + i[1] + '?page=' + str(j))
                    lis = bs.find('ul', class_='menu_list').find_all('li')
                    for k in lis:
                        time.sleep(0.1)
                        try:
                            caiming = k.find('div', class_='txt').find('h4').text
                            caiming_img_link = k.find('img')['src']
                            caiming_link = k.a['href']
                            # print('图片连接'+caiming_img_link)
                            # print('菜名'+caiming)
                            # print('链接'+caiming_link)
                            try:
                                sql = "insert into menu(menu_title,menu_img,menu_link,menu_one_cate,menu_two_cate )values ('%s','%s','%s','%s','%s')" % (
                                    caiming, caiming_img_link, caiming_link, i[0], i[2])
                                print(sql)
                                mu.executeSql(sql)
                            except Exception as e:
                                print(e)
                                print('菜名' + caiming + '出现了问题')
                        except Exception as e:
                            print(e)
                            print('error : 数据库插入时出现问题' + k)
                except Exception as e:
                    print(e)
                    print('error :二级分类' + i[2] + '下的第' + str(j) + '页 出现问题')
        except Exception as e:
            print(e)
            print('error :二级分类' + i[2] + ' 出现问题')

    pass


# 获取每一道菜的具体做法
def getMenuInfo():
    mu = MysqlUtil(host='127.0.0.1', user='root', psw='', db='love')
    mu.init()
    for i in range(500):
        sql ='select * from menu limit '+str((i)*100)+','+str((i+1)*100)
        mu.executeSql(sql)
        temp=mu.cursor.fetchall()
        try:
            for j in temp:
                try:
                    time.sleep(0.2)
                    bs=helper.getBs(base+j[3])
                    lis=bs.find_all('li',class_='material_li')
                    food=[]
                    try:
                        for k in lis:
                            food.append(k.text.replace('\n',''))
                    except Exception as e:
                        print(str(e)+'error:109')
                    menu_food=('|'.join(food))

                    steps=bs.find_all('div',class_='step_one')
                    step=[]
                    try:
                        for k in steps:
                            text=k.find(class_='step_text').text.replace('\n','')
                            img=k.find('img',class_='step_img')['src']
                            step.append(text+'^'+img)
                    except Exception as e:
                        print(str(e)+'error:119')
                    menustep=('|'.join(step))
                    sql = "insert into menu_info(menu_id,menu_title,menu_food,menu_step,menu_one_cate,menu_two_cate )values ('%s','%s','%s','%s','%s','%s')" %\
                          (str(j[0])+'',j[1],menu_food,menustep,j[4],j[5])
                    print(sql)
                    mu.executeSql(sql)
                except Exception as e:
                    print(str(e)+'error:127')
        except Exception as e:
            print(str(e)+'error:131')
    pass


def run():
    # 初始化爬虫工具
    init()
    # 获取分类
    # getCate()
    # 获取分类下的菜单名
    # getList()
    # 获取每一道菜的具体做法
    getMenuInfo()

    pass


if __name__ == '__main__':
    run()
