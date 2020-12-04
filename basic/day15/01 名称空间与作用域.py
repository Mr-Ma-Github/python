# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-25 22:56 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 一 名称空间：namespaces：存放名字的地方，是对栈区的划分
# 名称空间即存放名字与对象映射/绑定关系的地方。对于x=3，Python会申请内存空间存放对象3，
# 然后将名字x与3内存地址的绑定关系存放于名称空间中，del x表示清除该绑定关系。

# 名称空间是对栈区的一种划分，真正存在的是栈区，名称空间只是一种虚拟的划分。

# ​在程序执行期间最多会存在三种名称空间
# 1.1 内置名称空间
# 存放的名字：存放的python解释器内置的名字
# 比如内建函数名：
# max
# <built-in function max> # built-in内置
# 存活周期：python解释器的启动则产生，关闭则回收。因而是第一个被加载的名称空间

# 1.2 全局名称空间
# 存放的名字：只要不是函数内定义的，也不是内置的，剩下的都是全局名称
# 存货周期：python文件执行而产生，执行完毕回收，是第二个被加载的名称空间
# 文件执行过程中产生的名字都会存放于该名称空间中，如下名字：
# import sys #模块名sys
# x = 1 #变量名x
# if x == 1:
#     y = 2 #变量名y
#
# def foo(x): #函数名foo
#     y = 1  # 局部名称空间
#     def bar():
#         pass
#
# Class Bar: #类名Bar
#     pass

# 1.3 局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
# 存活周期：在函数调用时产生，调用结束后回收。函数的形参、函数内定义的名字都会被存放于该名称空间中
# def foo(x):
#     y=3 # 调用函数时，才会执行函数代码，名字x和y都存放于该函数的局部名称空间中

# 1.4 名称空间的加载顺序是：
# 内置名称空间->全局名称空间->局部名称空间

# 1.5 销毁顺序反之。

# 1.6 名称空间的查找顺序：当前所在位置向上一层一层查找
# *****名称空间只有优先级之分，本身并未嵌套关系，嵌套画图是为了便于理解
# 内置名称空间
# 全局名称空间
# 局部名称空间

# 如果当前在局部名称空间
# 查找顺序为：局部名称空间->全局名称空间->内置名称空间。
# # input = '222'
# def func():
#     # input = '333'
#     print(input)
#
# func()

# 如果当前在全局称空间
# 查找顺序为：全局名称空间->内置名称空间。
# input = '222'
# def func():
#     input = '333'
#
# func()
# print(input)

# 示范一：局部名称空间->全局名称空间
# def func():
#     print(x)
# x = 111
#
# func()

# 示范二：名称空间的嵌套关系是以函数定义阶段为准，与调用位置无关(********)
# x = 1
# def func():
#     print(x)
#
# def foo():
#     x = 222
#     func()
#
# foo()

# 示范三：函数嵌套定义
# input = 111
# def func1():
#     def func2():
#         input = 222
#         print(input)
#     func2()
#
# func1()

# 示范四：报错：定义阶段发现内置名称空间中已有x，但是调用的时候还没定义：
# x = 111
# def func():
#     print(x)
#     x = 222
#
# func()  # UnboundLocalError: local variable 'x' referenced before assignment

# 重点1:
# 名称空间的嵌套关系是以函数定义阶段为准，与调用位置无关
# 重点2:
# 名称空间只有优先级之分,本身并无嵌套关系,画图只是为了理解
# 重点3:
# 名称空间的嵌套关系决定了名字的查找顺序
# 而名称空间的嵌套关系是以函数定义阶段为准的,
# 即函数的嵌套关系与名字的查找顺序是在定义阶段就已经确定好的


# 二 作用域--》作用范围
# 2.1 全局作用域与局部作用域：
# 按照名字作用范围的不同可以将三个名称空间划分为两个区域：全局作用域、局部作用域
# 全局作用域: 全局名称空间、内置名称空间中的名字属于全局范围
# 1.全局存活（除非被删除，否则在整个文件执行过程中存活）
# 2.全局有效：被所有函数共享（在任意位置都可以使用）
# 局部作用域: 局部名称空间中的名字属于局部范围
# 1.临时存活（即在函数调用时临时生成，函数调用结束后就释放）
# 2.局部有效:只能在函数内使用

# 2.2 作用域与名字查找的优先级
# ​在局部作用域查找名字时，起始位置是局部作用域，所以先查找局部名称空间，没有找到，
# 再去全局作用域查找，再查找内置名称空间，最后都没有找到就会抛出异常
# x = 100 #全局作用域的名字x
# def foo():
#     x = 300  # 局部作用域的名字x
#     print(x)  # 在局部找x
#
# foo()  # 结果为300

# 在全局作用域查找名字时，起始位置便是全局作用域，所以先查找全局名称空间，没有找到，再查找内置名称空间，
# 最后都没有找到就会抛出异常
# x = 100
# def foo():
#     x = 300 #在函数调用时产生局部作用域的名字x
#
# foo()
# print(x) #在全局找x,结果为100
# 提示：可以调用内建函数locals()和globals()来分别查看局部作用域和全局作用域的名字，查看的结果都是字典格式。
# 在全局作用域查看到的locals()的结果等于globals()

# LEGB:
# LEGB含义解释：
# L —— Local(function)；函数内的名字空间
# E —— Enclosing function locals；外部嵌套函数的名字空间(例如closure)
# G —— Global(module)；函数定义所在模块（文件）的名字空间
# B —— Builtin(Python)；Python内置模块的名字空间

# # biuld-in
# # global
# def f1():
#     # enclosing
#     def f2():
#         # enclosing
#         def f3():
#             # local
#             pass