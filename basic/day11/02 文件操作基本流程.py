# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-12 23:27 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 1.打开文件
# windows路径分隔符问题：
# 解决方案一：推荐
# open(r'C:\Users\haiyu.ma\PycharmProjects')
# 解决方案二：
# open('C:/Users/haiyu.ma/PycharmProjects')
file_path = 'a.txt'
f = open('a.txt', mode='rt', encoding='utf-8')  # 默认mode='rt'# f的值是一种变量，占用的是应用程序的内存空间

# 2.操作文件：读、写文件：应用程序对文件的读写请求都是在向操作系统发送系统调用，然后由操作系统控制硬盘
# 把数据读入内存、或者写入硬盘
res = f.read()
print(res)

# 3.关闭文件
f.close()  # 回收操作系统资源

# print(f)
# f.read()  # 变量f存在，但是不能再读了  # ValueError: I/O operation on closed file.

# del f  # 回收应用程序资源(不用写)