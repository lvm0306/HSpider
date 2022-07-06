import random

u1 = '#系统基础信息：\n'
u2 = '系统版本|CentOS Linux release 7.7.1908 (Core)\n'
u3 = '系统内核|3.10.0-1062.el7.x86_64\n'
u4 = '主机名称|localhost.domain.com\n'
u5 = '默认语言|en_US.UTF-8\n'
u6 = '当前时间|2022-06-27 16:27:23\n'
u7 = '此用户登录时间|2020-10-17 07:41\n'
u8 = '系统已运行时间|{}\n'  # 200-1000的随机数
u9 = 'IP地址|35.1.11.201\n'
u10 = '掩码|255.255.255.0\n'
u11 = 'CPU信息|6 *Intel(R) Xeon(R) Silver 4214\n'
u12 = 'CPU型号| Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz\n'
u13 = 'CPU架构|x86_64\n'
u14 = '物理CPU数|2\n'
u15 = '逻辑CPU数|6\n'
u16 = '单内存容量|10240 MB\n'
u17 = '最大存储容量|10 GB\n'
u18 = '内存卡槽数|1\n'
u19 = '理论总内存|10GB\n'
u20 = '内存品牌|KVM\n'
u21 = '系统负载|3 users, load average: {}, {}, {} \n'  # 做随机数
u22 = '获取近1分钟占用CPU内核数|0\n'
u23 = '用户空间占用CPU的百分比|2.1\n'
u24 = '内核空间占用CPU的百分比|1.0\n'
u25 = '空闲CPU|99.0\n'
u26 = '等待占用CPU的百分比|0.0\n'
u27 = '实际总物理内存M|9979M\n'
u28 = '实际可用内存M|2240M\n'
u29 = '用户缓存容量|3200M\n'
u30 = '空闲缓存容量|2239M\n'
u31 = '缓冲缓存容量|4539M\n'
u32 = '交换分区总容量|0M\n'
u33 = '交换分区空闲容量|0M\n'
u34 = '交换分区占用容量|0M\n'
u35 = '交换分区可用容量|6045M\n'
u36 = '网卡1每秒接收数据包数|lo\n'
u37 = '网卡1每秒发送数据包数|2.00\n'
u38 = '网卡1每秒接收字节数|0.00\n'
u39 = '网卡1每秒发送字节数|0.00\n'
u40 = '#内存状态：\n'
u41 = '正常\n'
u42 = '总内存大小：9979M\n'
u43 = '剩余内存大小：{}M\n'
u44 = '内存使用率：{}%\n'
u45 = '#是否存在暴力破解密码：\n'
u46 = '正常\n'
u47 = '#是否存在僵尸进程：\n'
u48 = '不存在\n'
u49 = '#内存占用率TOP10进行列表：\n'
u50 = '88123 {} 1936404 /opt/IBM/WebSphere/AppServer/java/bin/java\n'
u51 = '1123 {} 13640 /opt/IBM/WebSphere/AppServer/java/bin/java\n'
u52 = '87199 1.6 165604 /usr/bin/gnome-software\n'
u53 = '86908 1.5 158116 /usr/bin/gnome-shell\n'
u54 = '87069 0.8 85816 /usr/libexec/gsd-color\n'
u55 = '1696 0.3 35288 /usr/bin/X\n'
u56 = '87152 0.1 17820 /usr/libexec/tracker-store\n'
u57 = '88241 0.1 17504 /usr/libexec/gnome-terminal-server\n'
u58 = '1009 0.1 16804 /usr/lib/polkit-1/polkitd\n'
u59 = '1361 0.1 16336 /usr/bin/python2\n'
u60 = '#CPU利用率TOP10进行列表：\n'
u61 = '   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND\n'
u62 = ' 84670 root      20   0 5657684   1.9g  98276 S  13.3 19.1  76:22.57 java\n'
u63 = '     1 root      20   0  191296   3756   2096 S   0.0  0.0  33:46.72 systemd\n'
u64 = '     2 root      20   0       0      0      0 S   0.0  0.0   0:08.51 kthreadd\n'
u65 = '     4 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0+\n'
u66 = '     6 root      20   0       0      0      0 S   0.0  0.0   2:07.73 ksoftirqd+\n'
u67 = '     7 root      rt   0       0      0      0 S   0.0  0.0   0:04.46 migration+\n'
u68 = '     8 root      20   0       0      0      0 S   0.0  0.0   0:00.00 rcu_bh\n'
u69 = '     9 root      20   0       0      0      0 S   0.0  0.0 410:14.06 rcu_sched\n'
u70 = '    10 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 lru-add-d+\n'
u71 = '    11 root      rt   0       0      0      0 S   0.0  0.0   2:31.50 watchdog/0\n'
u72 = '#磁盘使用情况：\n'
u73 = '/dev 分区 剩余空间 4.9G 使用率 0%\n'
u74 = '/dev/shm 分区 剩余空间 4.9G 使用率 0%\n'
u75 = '/run 分区 剩余空间 4.5G 使用率 9%\n'
u76 = '/sys/fs/cgroup 分区 剩余空间 4.9G 使用率 0%\n'
u77 = '/ 分区 剩余空间 {}G 使用率 {}%\n'
u78 = '/boot 分区 剩余空间 40M 使用率 78%\n'
u79 = '/run/user/42 分区 剩余空间 998M 使用率 1%\n'
u80 = '/run/user/0 分区 剩余空间 998M 使用率 1%\n'


def getFloatRandom(a, b):
    rm = random.random()
    ri = random.randint(a, b)
    r = round(rm, 2)
    return r + ri

    pass


def getFloatSimple():
    rm = random.random()
    r = round(rm, 2)
    return r

    pass


def getIntRandom(a, b):
    return random.randint(a, b)
    pass


def getIntRandom80w(a, b):
    t = 800000 + random.randint(a, b)
    return t
    pass


def getIntRandom60w(a, b):
    t = 600000 + random.randint(a, b)
    return t
    pass


def writeLog(fold, name):
    f = open(fold + "\\" + name + ".log", 'w', encoding='utf-8')
    f.write(u1)
    f.write(u2)
    f.write(u3)
    f.write(u4)
    f.write(u5)
    f.write(u6)
    f.write(u7)
    f.write(u8.format(str(getIntRandom(200, 500))))
    f.write(u9)
    f.write(u10)
    f.write(u11)
    f.write(u12)
    f.write(u13)
    f.write(u14)
    f.write(u15)
    f.write(u16)
    f.write(u17)
    f.write(u18)
    f.write(u19)
    f.write(u20)
    f.write(u21.format(str(getFloatSimple()), str(getFloatSimple()), str(getFloatSimple())))
    f.write(u22)
    f.write(u23)
    f.write(u24)
    f.write(u25)
    f.write(u26)
    f.write(u27)
    f.write(u28)
    f.write(u29)
    f.write(u30)
    f.write(u31)
    f.write(u32)
    f.write(u33)
    f.write(u34)
    f.write(u35)
    f.write(u36)
    f.write(u37)
    f.write(u38)
    f.write(u39)
    f.write(u40)
    f.write(u41)
    f.write(u42)
    f.write(u43.format(str(getIntRandom(3000, 4000))))
    f.write(u44.format(str(getIntRandom(60, 80))))
    f.write(u45)
    f.write(u46)
    f.write(u47)
    f.write(u48)
    f.write(u49)
    f.write(u50.format(str(getFloatRandom(19, 30))))
    f.write(u51.format(str(getFloatRandom(10, 15))))
    f.write(u52)
    f.write(u53)
    f.write(u54)
    f.write(u55)
    f.write(u56)
    f.write(u57)
    f.write(u58)
    f.write(u59)
    f.write(u60)
    f.write(u61)
    f.write(u62)
    f.write(u63)
    f.write(u64)
    f.write(u65)
    f.write(u66)
    f.write(u67)
    f.write(u68)
    f.write(u69)
    f.write(u70)
    f.write(u71)
    f.write(u72)
    f.write(u73)
    f.write(u74)
    f.write(u75)
    f.write(u76)
    f.write(u77.format(str(getIntRandom(200, 240)), str(getIntRandom(20, 40))))
    f.write(u78)
    f.write(u79)
    f.write(u80)
    f.close()


pass

# if __name__ == '__main__':
#     writeLog()
#     print()
#     pass
