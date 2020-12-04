# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-09 17:11 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 元祖就是“一个不可变的列表”
# 作用：按照索引/位置存放多个值，只用于读不用于改
# 定义：()内用逗号分隔开多个任意类型的元素
# t = (1, 2.34, 'fhsdl')  # t = tuple((1, 2.34, 'fhsdl'))
# print(type(t))

# t = (10)  # 单独一个括号代表包含的意思
# print(t, type(t))
# t = (10,)  # 如果元祖中只有一个元素，必须加一个逗号
# print(t, type(t))
# 类型转换：
# 但凡能被for循环的遍历的数据类型都可以传给tuple()转换成元组类型
# print(tuple('wdad'))  # 结果：('w', 'd', 'a', 'd')
# print(tuple([1, 2, 3]))  # 结果：(1, 2, 3)
# print(tuple({"name": "jason", "age": 18}))  # 结果：('name', 'age')
# print(tuple((1, 2, 3)))  # 结果：(1, 2, 3)
# print(tuple({1, 2, 3, 4}))  # 结果：(1, 2, 3, 4)
# tuple()会跟for循环一样遍历出数据类型中包含的每一个元素然后放到元组中
# 内置方法：
tuple1 = (1, 'hhaha', 15000.00, 11, 22, 33)
# 1、按索引取值(正向取+反向取)：只能取，不能改否则报错！
# print(tuple1[0])  # 1
# print(tuple1[-2])  # 22
# tuple1[0] = 'hehe'  # 报错：TypeError:
# 2、切片(顾头不顾尾，步长)
# print(tuple1[0:6:2])  # (1, 15000.00, 22)
# 3、长度
# print(len(tuple1))  # 6
# 4、成员运算 in 和 not in
# print('hhaha' in tuple1)  # True
# print('hhaha' not in tuple1)  # False
# 5、循环
# for line in tuple1:
#     print(line)

# 6、其他内置方法
t = (1, 2, 3, 1)
# index
print(t.index(1))
# print(t.index(4))  # ValueError: tuple.index(x): x not in tuple
# count
print(t.count(1))
print(t.count(4))
