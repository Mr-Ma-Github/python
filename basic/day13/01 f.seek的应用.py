# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-19 17:09 
# @Software：PyCharm
# ----------------------------------------------------------------------------
import time
with open(r'access.log', mode='rb')as file:
    # 1.将指针调到文件末尾
    # file.read()  # 错误
    file.seek(0, 2)
    while True:
        res = file.readline()
        if len(res) == 0:
            time.sleep(0.3)
        else:
            print(res.decode('utf-8'), end='')
