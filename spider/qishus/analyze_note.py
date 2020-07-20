import csv
import os

from utils.CiyunUtil import CiyunHelper, CiyunHelperBg

fold_name = "D:\space\product_space\down"


def getAllNoteName(file_dir):
    result=""
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(files)  # 当前路径下所有非目录子文件
        for i in files:
            result+=i.replace(".txt","")+" "
        print(len(result))  # 当前路径下所有非目录子文件

    with open('result.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(result)  # 写入
    pass


def getAllNoteName2():
    csv_file = csv.reader(open("t_name.csv", 'r'))
    cate_list = ""
    temp=[]
    for i in csv_file:
        cate_list+=i[0]+" "
        temp.append(i[0])
        # print(temp)
    print(cate_list)
    print(len(temp))
    # with open('result2.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
    #     file_handle.write(cate_list)  # 写入
    pass


def run():
    # 获取所有小说名字
    # getAllNoteName(fold_name)

    # getAllNoteName2()
    # 用结巴进行分词

    # 用词云进行处理
    CiyunHelper(height=1600,width=1600,imageurl='D:\\space\\py_space\\spider\\spider\\qishus\\img.jpg',texturl='D:\\space\\\py_space\\spider\\spider\\qishus\\result2.txt',fontsize=180).createImage()
    pass


if __name__ == "__main__":
    run()
