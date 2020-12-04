# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-11 23:56 
# @Software：PyCharm
# ----------------------------------------------------------------------------
x = '上'
res = x.encode('gbk')  # unicode--->gbk         编码
print(res, type(res))

res1 = res.decode('gbk')  # gbk---->unicode      解码
print(res1, type(res1))
