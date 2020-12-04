# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-09-23 22:22 
# @Software：PyCharm
# ----------------------------------------------------------------------------
#  3.基本运算符
# 算术运算符：+ - * / % **
# print(10 + 3)
# print(10 + 3.1)
# print(10/3)  # 结果中包含小数
# print(10//3)  # 结果中只保留整数部分
# print(10 % 3)  # 取余数/取模
# print(10 * 3)  # 10乘以3的结果
# print(10 ** 3)  # 10的三次方

# 赋值运算符:=
# 增量赋值
# age = 18
# age += 1  # age = age + 1
# print(age)
# age -= 3
# age *= 3
# age /= 3
# age %= 3  # age = age % 3
# age **= 3  # age = age ** 3（age的3次幂）

# 链式赋值
# x = 10
# y = x
# z = y
# z = y = x = 10  # 链式赋值
# print(x, y, z)
# print(id(x), id(y), id(z))

# 交叉赋值
m = 10
n = 20
print(m, n)
# 交换值
# t = m
# print(m, n, t)
# m = n
# print(m, n, t)
# n = t
# print(m, n, t)
# m, n = n, m  # 交叉赋值
# print(m, n)

# 解压赋值
# salaries = [111, 222, 333, 444, 555]
# 把5个月的工资取出来，分别赋值给不同的变量名
# mon1 = salaries[0]
# mon2 = salaries[1]
# mon3 = salaries[2]
# mon4 = salaries[3]
# mon5 = salaries[4]
# # print(mon1, mon2, mon3, mon4, mon5)
# mon1, mon2, mon3, mon4, mon5 = salaries  # 对应的变量名必须与值数量对应
# print(mon1, mon2, mon3, mon4, mon5)
# # 引入*，可以帮助我们取两头的值，无法取中间的值
# # 取前三个值
# x, y, z, *_ = salaries  # *会将没有对应关系的值存成列表然后赋值给紧跟其后的那个变量名，此处为 _
# print(x, y, z, _)
# # 取后三个值
# *_, x, y, z,  = salaries
# print(_, x, y, z)
# # 取中间三个值
# ## *_, x, y, z, *_ = salaries   # 不支持
# x, *m, z = salaries  # 这样可以，但是最好不要这样做
# print(m)
# 解压字典：默认解压出的是key
# x_dict = {'a': 1, 'b': 2, 'c': 3}
# x, y, z = x_dict
# print(x, y, z)

# 可变不可变类型：
# 可变类型：值改变，id不变，证明改的是原值，证明原值是可以被改变的
# 不可变类型：值改变，id也变了，证明是产生了新值，压根没有改变原值，证明原值是不可以被改变的
# 验证:
x = 10
print(id(x))
x = 11
print(id(x))
# 结果：
# 不可变类型: int、float、str、bool、tuple
#   可变类型：list、dict
# ps:
# int、float、str在python中都被设计成了不可分割的整体，不能够被改变
# list、dict

# 比较运算符 >  <  >=  <=  ==  !=
# print(10 > 2)

# 什么是条件？什么可以当做条件？为何要用条件？
# 条件可以是：比较运算符、布尔值
# 1.显示布尔值：True、False
# 1.1 比较运算符
#     age = 18
#     print(age > 16)  # 条件判断之后会得到一个布尔值
# 1.2 条件可以是True、False
#     is_beautiful = True
#     print(is_beautiful)
# 2.隐式布尔值：所有数据类型都可以当成条件去用，
# 其中0、None、空(空字符串、空列表、空字典)代表的布尔值为False，其余都为True

# 逻辑运算符 ： not 、and 、or
# not:就是把紧跟其后的那个条件取反(not与紧跟其后的条件是一个不可分割的整体)
# print(not 16 > 13)
# print(not False)
# and:逻辑与
# or:逻辑或
# 区分优先级：not > and > or

# 成员运算符:in
# print("egon"in "hello egon")  # 判断一个字符串是否存在于一个大字符串当中
# ps:字典默认判断的是key
# 身份运算符:is
# is：比较左右两个值身份id是否相等
# id不同的情况下，值有可能相同，即两块不同的内存空间里可以存相同的值
# id相同的情况下，值一定相同，x is y成立，x == y也必然成立

