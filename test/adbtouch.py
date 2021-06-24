import os
import time

adbShell = "adb shell  {cmdStr}"


def execute(cmd):
    str = adbShell.format(cmdStr=cmd)
    print(str)
    os.system(str)


if __name__ == '__main__':
    # 点击返回按键
    # os.system(" adb shell input keyevent 4 ")
    # 点击
    for i in range(2000):
        execute("input tap 941 2200")
        time.sleep(0.1)
