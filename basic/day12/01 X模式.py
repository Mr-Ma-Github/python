# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-17 23:56 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# x模式（控制文件操作的模式）-了解
# x：只写模式：不可读，不存在则创建，存在保错--FileExistsError
# with open('a.txt', mode='x', encoding='utf-8') as f:
#     ...

# with open('test1.txt', mode='x', encoding='utf-8') as f:
#     f.read()  # 报错--x模式下不可读--io.UnsupportedOperation: not readable

# with open('test2.txt', mode='x', encoding='utf-8') as f:
#     f.write('啊哈哈哈哈')  # 可以写

# x+:可读可写