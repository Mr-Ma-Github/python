# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-12-01 22:47 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 装饰器
# 1.什么是装饰器？
# 器指的是工具，可以定义成函数
# 装饰指的是为其他事务添加额外的东西来点缀
# 即：装饰器指的是定义一个函数（类等），该函数是用来为其他函数添加额外的功能

# 2.为何要用装饰器？
# 开放封闭原则：
#     开放：指的是对拓展功能是开放的
#     封闭：指的是对修改源代码是封闭的
# 装饰器：在不修改被装饰对象源代码以及调用方式的前提下，为被装饰的对象添加新功能

# 3.如何用装饰器？
# 需求：在不修改index函数源代码以及调用方式的前提下，为其添加统计时间的功能
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
#
# index(1, 2) # 函数执行
# index(x=1, y=2)

# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了源代码
# import time
#
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#     stop = time.time()
#     print(stop - start)
#
# index(1, 2) # 函数执行

# 解决方案二：失败
# 问题：没有修改被装饰对象的调用方式，也没有修改源代码，并且加上了统计时间的功能
#       但是代码冗余
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
#
# start = time.time()
# index(1, 2) # 函数执行
# stop = time.time()
# print(stop - start)
#
# start = time.time()
# index(3, 4) # 函数执行
# stop = time.time()
# print(stop - start)

# 解决方案三：失败
# 问题1：没有修改源代码，解决了方案二的代码冗余问题，但是带来新的问题-修改了被装饰对象的调用方式
# 问题2：index函数的位置实参被写死了。被装饰对象也写死了
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
# def wrapper():
#     start = time.time()
#     index(111, 222)
#     stop = time.time()
#     print(stop - start)
#
# wrapper() # 函数执行


# 如何在方案三的基础上不改变函数的调用方式
# 方案三优化一：将index的参数写活，但是被装饰对象写死的问题还存在
# 问题1：没有修改源代码，解决了方案二的代码冗余问题，但是带来新的问题-修改了被装饰对象的调用方式
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
# 装饰器
# def wrapper(*args, **kwargs):  # wrapper(args=(1, 2))
#     start = time.time()
#     index(*args, **kwargs)  # index(*(1, 2))====>>index(1, 2)
#     stop = time.time()
#     print(stop - start)
#
# wrapper(1, 2) # 函数执行

# 方案三优化二：在优化一index的参数写活的基础上把被装饰对象写活了，并解决了-修改了被装饰对象的调用方式的问题
# 问题：如果被装饰对象有返回值存在，此时返回值不正确
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
# def home(name):
#     time.sleep(2)
#     print("Welcome %s come to the page" % name)
#     return 123
#
# 装饰器
# def outter(func):
#     # func = index的内存地址
#     def wrapper(*args, **kwargs):  # wrapper(args=(1, 2))
#         start = time.time()
#         func(*args, **kwargs)  # index(*(1, 2))====>>index(1, 2)
#         stop = time.time()
#         print(stop - start)
#     return wrapper
#
# index = outter(index) # index = outter(index的内存地址)===》》index=当初那个wrapper函数的内存地址
# print(index)
# index(1, 2)
#
# home = outter(home) # home = outter(home的内存地址)===》》home=当初那个wrapper函数的内存地址
# print(home)
# home("egon")
# # ps:这两个wrapper并不是同一个wrapper，原因在于投的食物不同（index，home）

# 方案三优化三：将wrapper做的跟被装饰对象一模一样， 以假乱真
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
# def home(name):
#     time.sleep(2)
#     print("Welcome %s come to the page" % name)
#     return 123
#
# # 装饰器
# def outter(func):
#     # func = index的内存地址
#     def wrapper(*args, **kwargs):  # wrapper(args=(1, 2))
#         start = time.time()
#         res = func(*args, **kwargs)  # index(*(1, 2))====>>index(1, 2)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
#
# # 偷梁换柱
# home = outter(home) # home = outter(home的内存地址)===》》home=当初那个wrapper函数的内存地址
# home("egon")
# # 返回值
# res = home("egon")
# print("返回值==>:", res)



# # 语法糖：让你开心的语法
# import time
#
#
# # 装饰器
# def outter(func):
#     # func = index的内存地址
#     def wrapper(*args, **kwargs):  # wrapper(args=(1, 2))
#         start = time.time()
#         res = func(*args, **kwargs)  # index(*(1, 2))====>>index(1, 2)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
#
#
# # 在被装饰对象正上方的单独一行，写@装饰器名字
# # @装饰器名称 就是  下方的函数名=装饰器名称(下方的函数名)
# @outter  # index = outter(index)
# def index(x, y):
#     time.sleep(3)
#     print("Welcome to the index page %s %s" % (x, y))
#
#
# @outter  # home = outter(home)
# def home(name):
#     time.sleep(2)
#     print("Welcome %s come to the page" % name)
#     return 123

# 偷梁换柱
# index = outter(index) # index = outter(index的内存地址)===》》index=当初那个wrapper函数的内存地址
# index(1, 2)
# home = outter(home) # home = outter(home的内存地址)===》》home=当初那个wrapper函数的内存地址
# print("返回值==>:", res)

# index(1, 2)
# home("egon")




# 总结无参装饰器模板：
def outter(func):
    def wrapper(*args, **kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        res = func(*args, **kwargs)
        return res
    return wrapper

@outter
def index():
    print("from index")

index()