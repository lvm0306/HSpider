import csv
import os

from yw.writeTooMuchLog import writeLog

url_list_rules = []
logs_os = []
current_year = '22'
current_mouth = '06'


def readRules():
    csvFile = open("config\\url_rules.csv", "r")
    reader = csv.reader(csvFile)
    url_list_rules.append(list(reader))
    # 测试
    # list0 = url_list_rules[0]
    # print(list0)
    # left = int(list0[1])
    # right = int(list0[2])+1
    # print('left=={},right={}'.format(left, right))
    # for i in range(left, right):
    #     print(i)
    # print(url_list_rules)
    # for row in url_list_rules:
    #     print(row)
    pass


def generateUrlCsv():
    current_directory = os.getcwd()
    print(current_directory)
    with open('config\\temp_rzgenerate.csv', "a+", encoding="gbk", newline='') as f:
        for i in url_list_rules[0]:
            left = int(i[1])
            right = int(i[2]) + 1
            # print('left=={},right={}'.format(left, right))
            for j in range(left, right):
                # print('{},{}{}{}'.format(i[0], current_year, current_mouth, j))
                temp = []
                j_t = ''
                if j < 10:
                    j_t = '0' + str(j)
                else:
                    j_t = str(j)
                f_time = current_year + current_mouth + str(j_t)
                temp.append(i[0])
                temp.append(f_time)
                writer = csv.writer(f)
                writer.writerow(temp)


pass

'''
创建指定的文件夹
:param path: 文件夹路径，字符串格式
:return: True(新建成功) or False(文件夹已存在，新建失败)
'''


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 创建日志
def createLogs():
    csvFile = open("config\\temp_rzgenerate.csv", "r")
    reader = csv.reader(csvFile)
    logs_os.append(list(reader))
    print(logs_os[0])
    for i in logs_os[0]:
        # print(i[0])
        # print(i[1])
        mkdir('result\\' + i[1])
        writeLog('result\\' + i[1], '{}-{}'.format(i[0], i[1]))
    pass


def createFold():
    mkdir('result')

    pass


if __name__ == '__main__':
    # createFold()
    # readRules()
    # generateUrlCsv()
    createLogs()
    pass
