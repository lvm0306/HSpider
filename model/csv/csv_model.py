import csv

'''
mode 的值
w=只能操作写入（如果而文件中有数据，再次写入内容，会把原来的覆盖掉）
r=只能读取
a=向文件追加
w+=可读可写
r+=可读可写
a+=可读可追加
wb+=写入数据
'''


# encoding utf-8-sig/gbk
# 写csv
def write():
    with open("../test.csv", mode='a+', encoding='utf-8-sig', newline="") as f:
        cswrite = csv.writer(f)
        row = ['曹操', '23', '学生', '黑龙江', '5000']
        row1 = ['曹操', '23', '学生', '黑龙江', '5000']
        cswrite.writerow(row)
        cswrite.writerow(row1)
    pass


# 批量写
def dict_writer():
    # 创建列表，保存header内容
    header_list = ["name", "sex", "age", "score"]
    # 创建列表，保存数据
    data_list = [
        {"name": "a", "sex": "m", "age": 20, "score": 80},
        {"name": "bb", "sex": "fm", "age": 19, "score": 90},
        {"name": "ccc", "sex": "fm", "age": 21, "score": 95},
    ]
    # 以写方式打开文件。注意添加 newline=""，否则会在两行数据之间都插入一行空白。
    with open("dict_new_data.csv", mode="w", encoding="utf-8-sig", newline="") as f_out:
        # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
        writer = csv.DictWriter(f_out, header_list)
        # 写入 header
        writer.writeheader()
        # 写入数据
        writer.writerows(data_list)
    pass


# 读取csv
def read():
    with open("../test.csv", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        lista = list(reader)
        print(lista)
    pass


if __name__ == '__main__':
    write()
    read()
    dict_writer()
    pass
