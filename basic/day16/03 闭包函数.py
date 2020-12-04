# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-30 14:50 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 一：大前提：
# 闭包函数 = 名称空间与作用域 + 函数嵌套 + 函数对象
# 核心点：名字的查找关系是以函数定义阶段为准
# 二：什么是闭包函数：若内嵌函数包含对外部函数作用域（而非全局作用域）中变量的引用，
                    # 那么该’内嵌函数’就是闭包函数，简称闭包
# “闭函数”指的是该函数是内嵌函数
# “包函数”指的是该函数包含对外层函数作用域名字的引用（不是全局作用域）
# def f1():
#     def f2():  # 闭函数
#         x = 1
#         def f3():  # 闭包函数
#             print(x)

# 闭包函数:名称空间与作用域 + 函数嵌套
# def f1():
#     x = 333333
#     def f2():  # 闭包函数
#         print(x)
#     f2()
#
# x = 1111
# def bar():
#     x = 444444
#     f1()
#
# def foo():
#     x = 2222
#     bar()
#
# foo()

# 闭包函数:函数对象
def f1():
    x = 333333
    def f2():  # 闭包函数
        print('函数f2：', x)
    return f2

f = f1()
print(f)
f()

# 三：为何要有闭包函数==》闭包函数的应用
# 两种为函数传参的方式：
# 方式一：直接把函数体需要的参数定义成形参
# def f2(x):
#     print(x)
#
# f2(1)

# 方式二：以闭包形式定义参数
# def f1(x):
#     def f2():
#         print(x)
#     return f2
#
# f2 = f1(3)
# f2()

# import requests
# #方式一：
# def get(url):
#     return requests.get(url).text

# 方式一下载同一页面
# print(get('https://www.python.org'))
# get('https://www.python.org')
# get('https://www.python.org')

# #方式二：
# def page(url):
#     def get():
#         return requests.get(url).text
#     return get
# # 方式二下载同一页面
# # print(page('https://www.python.org')())
# python=page('https://www.python.org')
# python()
# python()
# python()

# 对比两种方式，方式一在下载同一页面时需要重复传入url，而方式二只需要传一次值，
# 就会得到一个包含指定url的闭包函数，以后调用该闭包函数无需再传url

# 闭包函数的这种特性有时又称为惰性计算。使用将值包给函数的方式