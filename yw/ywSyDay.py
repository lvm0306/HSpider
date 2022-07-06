import csv
import os
import time
import sys

# 当前路径
from yw.RZGenerate import mkdir

os_folder = ''
os_folder_log = ''
# 系统版本 1
xt_bn = {}
# 系统内核 2
xt_nh = {}
# 默认语言 4
mryy = {}
# 系统运行时间 7
xt_yxsj = {}
# cup型号 11
cpu_xh = {}
# cpu信息 10
cpu_xx = {}
# cpu架构 12
cpu_jg = {}
# 内存信息
nc_xx = {}
# 系统负载信息 20
xt_fzxx = {}
# 空闲cpu 24
kx_cpu = {}
# 用户缓存容量 28
yh_hcrl = {}
# 空闲缓存容量 29
kx_hcrl = {}
# 缓冲缓存容量 30
hc_hcrl = {}
# 内存状态 40
nc_zt = {}
# 内存总大小 41
nc_zdx = {}
# 剩余内存大小 42
nc_sydx = {}
# 内存使用率 43
nc_ssl = {}
# 是否存在暴力破解密码 45
blpj = {}
# 是否存在僵尸进程 47
jsjc = {}
# 内存占用率前3
nc_zyl = {}
# cpu利用率
cpu_lyl = {}
# 磁盘分区
cpfq = {}
# ip集合
ips = []


# 解析文件
def run(ip, file):
    print('开始解析文件' + file)
    print('当前ip=====>' + ip)
    ips.append(ip)
    f = open(file, encoding="utf-8")
    # 输出读取到的数据
    file_last = []
    # print(len(f.readlines()))
    temp = f.readlines()
    all_lines = []
    nc_zyl_t = []  # 49 50 51
    cpu_lyl_t = []  # 61 62 63
    cpfq_t = []

    for i in temp:
        all_lines.append(i.replace('\n', ''))
    for index, value in enumerate(all_lines):
        # print(str(index) + "---" + value)
        if index == 1:
            # 系统版本 1
            if '系统版本' in value:
                xt_bn[ip] = value.split('|')[1]
            else:
                xt_bn[ip] = ''
        if index == 2:
            # 系统内核 2
            if '系统内核' in value:
                xt_nh[ip] = value.split('|')[1]
            else:
                xt_nh[ip] = ''
        if index == 4:
            # 默认语言 4
            if '默认语言' in value:
                mryy[ip] = value.split('|')[1]
            else:
                mryy[ip] = ''
        if index == 7:
            # 系统运行时间 7
            if '系统已运行时间' in value:
                xt_yxsj[ip] = value.split('|')[1]
            else:
                xt_yxsj[ip] = ''
        if index == 11:
            # cup型号 11
            if 'CPU型号' in value:
                cpu_xh[ip] = value.split('|')[1]
            else:
                cpu_xh[ip] = ''
        if index == 10:
            # cpu信息 10
            if 'CPU信息' in value:
                cpu_xx[ip] = value.split('|')[1]
            else:
                cpu_xx[ip] = ''
        if index == 12:
            # cpu架构 12
            if 'CPU架构' in value:
                cpu_jg[ip] = value.split('|')[1]
            else:
                cpu_jg[ip] = ''
        if index == 20:
            # 系统负载信息 20
            if '系统负载' in value:
                xt_fzxx[ip] = value.split('|')[1]
            else:
                xt_fzxx[ip] = ''
        if index == 24:
            # 空闲cpu 24
            if '空闲CPU' in value:
                kx_cpu[ip] = value.split('|')[1]
            else:
                kx_cpu[ip] = ''
        if index == 28:
            # 用户缓存容量 28
            if '用户缓存容量' in value:
                yh_hcrl[ip] = value.split('|')[1]
            else:
                yh_hcrl[ip] = ''
        if index == 29:
            # 空闲缓存容量 29
            kx_hcrl[ip] = value
            if '空闲缓存容量' in value:
                yh_hcrl[ip] = value.split('|')[1]
            else:
                yh_hcrl[ip] = ''
        if index == 30:
            # 缓冲缓存容量 30
            if '缓冲缓存容量' in value:
                hc_hcrl[ip] = value.split('|')[1]
            else:
                hc_hcrl[ip] = ''
        if index == 40:
            # 内存状态 40
            nc_zt[ip] = value
        if index == 41:
            # 内存总大小 41
            if '总内存大小' in value:
                nc_zdx[ip] = value.split('：')[1]
            else:
                nc_zdx[ip] = ''
        if index == 42:
            # 剩余内存大小 42
            if '剩余内存大小' in value:
                nc_sydx[ip] = value.split('：')[1]
            else:
                nc_sydx[ip] = ''
        if index == 43:
            # 内存使用率 43
            if '内存使用率' in value:
                nc_ssl[ip] = value.split('：')[1]
            else:
                nc_ssl[ip] = ''
        if index == 45:
            # 是否存在暴力破解密码 45
            blpj[ip] = value
        if index == 47:
            # 是否存在僵尸进程 47
            jsjc[ip] = value
        if index == 49:
            # 是否存在僵尸进程 47
            nc_zyl_t.append(value)
        if index == 50:
            # 是否存在僵尸进程 47
            nc_zyl_t.append(value)
        if index == 51:
            # 是否存在僵尸进程 47
            nc_zyl_t.append(value)
            nc_zyl[ip] = nc_zyl_t
        if index == 29:
            # 内存占用率前4
            nc_zyl[ip] = value
        if index == 29:
            # cpu利用率
            cpu_lyl[ip] = value
        if index == 29:
            # 磁盘分区
            cpfq[ip] = value

            #
    # 关闭文件
    f.close()


# 获取目录下的所有文件
def search_dir_all_files(input_dir):
    files_list = []
    for root, dirs, files in os.walk(input_dir, topdown=1):  # 优先top目录
        # os.walk会返回一个三元组分别存储了当前目录地址，该地址下所有的目录地址，该目录下所有的文件地址
        for name in files:
            files_list.append(os.path.join(root, name))
        for name in dirs:
            files_list.append(os.path.join(root, name))
    return files_list


# 检查参数
def checkArgs():
    try:
        # d = '220627'
        d = sys.argv[1]
        print('日期时间为：' + d)
        if len(d) != 6:
            raise Exception("请输入正确的日期，六位")

        if not (os.path.exists(d)):
            raise Exception("日期与本地日志不匹配")
        os_folde = os.getcwd()
        os_folder_log = os_folde + '\\' + d
        print('当前路径：' + os_folde)
        print('日志路径：' + os_folder_log)
        ll = search_dir_all_files(os_folder_log)
        print('一共产生了' + str(len(ll)) + '个日志文件')
        for i in ll:
            ip = i.split('-')[0].split('.')[-1]
            run(ip, i)
        with open(d + '.csv', "a+", encoding="gbk", newline='') as f:
            writer = csv.writer(f)
            title = []
            title.append('ip')
            title.append('系统运行时间')
            title.append('系统负载信息')
            title.append('内存总大小')
            title.append('剩余内存大小')
            title.append('内存使用率')
            title.append('是否存在暴力破解密码')
            title.append('是否存在僵尸进程')
            writer.writerow(title)
            print('ips:' + str(len(ips)))
            print(ips)
            # tt = []
            for ip_t in ips:
                # print(ip_t)
                ip_temp = []
                ip_temp.append(ip_t)
                ip_temp.append(xt_yxsj[ip_t])
                ip_temp.append(xt_fzxx[ip_t])
                ip_temp.append(nc_zdx[ip_t])
                ip_temp.append(nc_sydx[ip_t])
                ip_temp.append(nc_ssl[ip_t])
                ip_temp.append(blpj[ip_t])
                ip_temp.append(jsjc[ip_t])
                writer.writerow(ip_temp)
                # tt.append(ip_temp)
            # writer.writerows(tt)
    except Exception as e:
        print(e)


# 全月版
def checkArgsAllMouth(d, t):
    try:
        # d = '220627'
        # d = sys.argv[1]
        print('日期时间为：' + d)
        if len(d) != 6:
            raise Exception("请输入正确的日期，六位")

        # if not (os.path.exists(d)):
        #     raise Exception("日期与本地日志不匹配")
        os_folde = os.getcwd()
        os_folder_log = os_folde + '\\result\\' + d
        print('当前路径：' + os_folde)
        print('日志路径：' + os_folder_log)
        ll = search_dir_all_files(os_folder_log)
        print('一共产生了' + str(len(ll)) + '个日志文件')
        for i in ll:
            ip = i.split('-')[0].split('.')[-1]
            run(ip, i)
        mkdir('result\\' + t )
        with open('result\\' + t + '\\' + d + '.csv', "a+", encoding="gbk", newline='') as f:
            writer = csv.writer(f)
            title = []
            title.append('ip')
            title.append('系统运行时间')
            title.append('系统负载信息')
            title.append('内存总大小')
            title.append('剩余内存大小')
            title.append('内存使用率')
            title.append('是否存在暴力破解密码')
            title.append('是否存在僵尸进程')
            writer.writerow(title)
            print('ips:' + str(len(ips)))
            print(ips)
            # tt = []
            for ip_t in ips:
                # print(ip_t)
                ip_temp = []
                ip_temp.append(ip_t)
                ip_temp.append(xt_yxsj[ip_t])
                ip_temp.append(xt_fzxx[ip_t])
                ip_temp.append(nc_zdx[ip_t])
                ip_temp.append(nc_sydx[ip_t])
                ip_temp.append(nc_ssl[ip_t])
                ip_temp.append(blpj[ip_t])
                ip_temp.append(jsjc[ip_t])
                writer.writerow(ip_temp)
                # tt.append(ip_temp)
            # writer.writerows(tt)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print('-------------')
    # run()
    checkArgs()
    print('-------------')
