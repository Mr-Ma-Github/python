# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-16 18:10 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 文件对象又称为文件句柄：
# with open("a.txt", mode='rt') as file:  # 不需要写file.close(), with会自动关闭
#     res = file.read()
#     print(res)

with open("db.txt", mode='rt') as file, open("test2.txt", mode='rt') as file1:
    res = file.read()
    res1 = file1 .read()
    print(res)
    print(res1)
