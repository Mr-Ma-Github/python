# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-19 23:25 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
1、什么是函数
    函数就相当于具备某一功能的工具
    函数的使用必须遵循一个原则:先定义,后调用
2、为何要用函数
    1、组织结构不清晰,可读性差
    2、代码冗余
    3、可维护性、扩展性差
3、如何用函数
    先定义
        三种定义方式
    后调用
        三种调用方式
    返回值
        三种返回值的形式
4.函数分为两大类，分别是什么？二者在使用时有何区别？
    内置函数：直接可以调用
    自定义函数：需要先定义，才能调用
'''
# 1.定义函数的语法
# def 函数名(参数1,参数2,...):
#     """文档描述"""
#     函数体
#     return 值
# 1.def: 定义函数的关键字；
# 2.函数名：函数名指向函数内存地址，是对函数体代码的引用。函数的命名应该反映出函数的功能；
# 3.括号：括号内定义参数，参数是可有可无的，且无需指定参数的类型；
# 4.冒号：括号后要加冒号，然后在下一行开始缩进编写函数体的代码；
# 5."""文档描述""": 描述函数功能，参数介绍等信息的文档，非必要，但是建议加上，从而增强函数的可读性；
# 6.函数体：由语句和表达式组成；
# 7.return 值：定义函数的返回值，return是可有可无的。

# 一.定义函数
# 形式一：无参函数
# def func():
#     print('哈哈哈')
# 定义函数发生的事情：
# 1.首先申请内存空间将函数体代码保存起来
# 2.然后将内存地址赋值给函数名，函数名就是对这段代码的引用
# 3.定义函数不会执行函数体代码，但是会检测函数体语法

# print(func)  # 打印的是函数的内存地址 # <function func at 0x006128A0>
# func()  # 调用函数，触发函数体代码的执行
# 调用函数发生的事情：
# 1.通过函数名找到函数的内存地址
# 2.然后加括号就是在触发函数体代码的执行

# 示范一：
# def bar():  # bar=函数的内存地址
#     print('from bar')
#
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
#
# foo()

# 示范二：
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
#
# def bar():  # bar=函数的内存地址
#     print('from bar')
#
# foo()

# 示范三：会报错：调用的时候还未定义
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
#
# foo()  # NameError: name 'bar' is not defined
#
#
# def bar():  # bar=函数的内存地址
#     print('from bar')


# 形式二：有参函数
# def func(x, y):
#     print(x, y)
#
# func(1, 2)

# 形式三：空函数，函数体代码为pass
# def func(x, y):
#     pass
#
# func(1, 2)

# 三种定义方式各用在何处：
# 1.无参函数的应用场景
# def interactive():
#     username = input("username>>:")
#     password = input("password>>:")
#     res = ("账号:{} 密码:{}".format(username,password))
#     return res
#
# print(interactive())

# 2.有参函数的应用场景
# def add(x, y):  # 参数---》原材料
#     # x = 10
#     # y = 20
#     res = x + y
#     # print(res)
#     return res  # 返回值--》产品
#
# print(add(10, 20))

# 3.空函数的应用场景：构思代码的时候，罗列功能
# def auth_user():
#     """user.txt authentication function"""
#     pass
#
# def download_file():
#     """download file function"""
#     pass
#
# def upload_file():
#     """upload file function"""
#     pass
#
# def ls():
#     """list contents function"""
#     pass
#
# def cd():
#     """change directory"""
#     pass


# 二.调用函数
# 1.语句的形式：只加括号调用函数
# interactive()
# 2.表达式形式:
# def add(x, y):  # 参数---》原材料
#     res = x + y
#     return res  # 返回值--》产品
# 赋值表达式
# res = add(1, 2)
# print(res)
# 数学表达式
# res = add(1, 2)*10
# print(res)

# 3.函数调用可以当做参数：
# res = add(add(1, 2), 2)
# print(res)

# 三.函数返回值：
# return:return是函数结束的标志,即函数内代码一旦运行到return会立刻终止函数的运行，
# 并把return后定义的值作为本次运行的结果返回
# return后无值或直接省略return,默认返回None,return的返回值无类型限制,且可以将多个返回值放到一个元组内
# 1.返回None：函数体内没有return
#             return
#             return None
# def func():
#     return
#
# print(func())
# 2.返回一个值：return 值
# def func():
#     return 10
#
# print(func())
# 3.返回多个值：return 值1, 值2....# 用逗号分隔开多个值，会被return返回成元祖
def func():
    return 1, '哈哈', [1, 2, 3]  #等同于return (1, '哈哈', [1, 2, 3])

res = func()
print(res, type(res))
