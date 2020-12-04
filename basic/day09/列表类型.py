# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-08 22:09 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 1.作用：按位置存多个值
# 2.定义：
# l = [1, 1.23, 'ds']  # l=list([1, 1.23, 'ds'])
# print(type(l))
# 3.类型转换：但凡能够被for循环遍历的类型都可以当做参数传给list(),转换成列表
# res = list('hello')
# print(res)
# res = list({'k1': 111, 'k2': 222, 'k3': 333})
# print(res)
# 4.内置方法：
# 优先掌握的操作：
# 1.按索引存取值(正向存取+反向存取)：即可存也可以取
# 1.1 正向取(从左往右)
# my_friends = ['tony', 'jason', 'tom', 4, 5]
# print(my_friends[0])
# 1.2 反向取(负号表示从右往左)
# print(my_friends[-1])
# 1.3 对于list来说，既可以按照索引取值，又可以按照索引修改指定位置的值，但如果索引不存在则报错
# my_friends = ['tony', 'jack', 'jason', 4, 5]
# my_friends[1] = 'martthow'
# print(my_friends)
# 2.切片(顾头不顾尾，步长)
# 2.1 顾头不顾尾：取出索引为0到3的元素
# print(my_friends[0:4])  # 切片等同于拷贝行为，而且相当于浅拷贝
# 2.2 步长：0:4:2,第三个参数2代表步长，会从0开始，每次累加一个2即可，所以会取出索引0、2的元素
# print(my_friends[0:4:2])  # ['tony', 'tom']
# 3.长度
# print(len(my_friends))
# 4.成员运算in和not in
# print('tony' in my_friends)  # True
# print('xxx' not in my_friends)  # True
# 5.添加
# 5.1 append()列表尾部追加元素
# ll = ['a', 'b', 'c']
# ll.append('d')
# print(ll)  # ['a', 'b', 'c', 'd']
# 5.2 extend()一次性在列表尾部添加多个元素
# ll.extend(['a', 'b', 'c'])
# print(ll)  # ['a', 'b', 'c', 'd', 'a', 'b', 'c']
# 5.3 insert()在指定位置插入元素
# ll.insert(0, "first")  # 0表示按索引位置插值
# print(ll)  # ['first', 'a', 'b', 'c', 'alisa', 'a', 'b', 'c']
# 6.删除
# 6.1 del ： 通用的删除方法，只是单纯的删除、没有返回值
# l = [11, 22, 33, 44]
# del l[2]  # 删除索引为2的元素
# print(l)  # [11, 22, 44]
# 6.2 pop()默认删除列表最后一个元素，并将删除的值返回，括号内可以通过加索引值来指定删除元素
# l = [11, 22, 33, 22, 44]
# res = l.pop()
# print(res)  # 44
# res = l.pop(1)
# print(res)  # 22
# 6.3 remove()括号内指名道姓表示要删除哪个元素，没有返回值
# l = [11, 22, 33, 22, 44]
# res = l.remove(22)  # 从左往右查找第一个括号内需要删除的元素
# print(res)  # None
# 7.reverse()颠倒列表内元素顺序
# l = [11, 22, 33, 44]
# l.reverse()
# print(l)  # [44, 33, 22, 11]
# 8.sort()给列表内所有元素排序
# 8.1 排序时列表元素之间必须是相同数据类型，不可混搭，否则报错
# l = [11, 22, 3, 42, 7, 55]
# print(l.sort())
# print(l)  # [3, 7, 11, 22, 42, 55]  # 默认从小到大排序
# l = [11, 22, 3, 42, 7, 55]
# l.sort(reverse=True)  # reverse用来指定是否颠倒排序，默认为False
# print(l)  # [55, 42, 22, 11, 7, 3]

# 8.2 了解知识：
# 我们常用的数字类型直接比较大小，但其实，字符串、列表等都可以比较大小
# 原理相同：都是依次比较对应位置的元素的大小，如果分出大小，则无需比较下一个元素
# 比如：（注意：字典比较时，对应位置上的元素必须是同种类型）
# l1 = [1, 2, 3]
# l2 = [2, ]
# print(l2 > l1)  # True
# 字符之间的大小取决于它们在ASCII表中的先后顺序，越往后越大
# s1 = 'abc'
# s2 = 'az'
# print(s2 > s1)  # s1与s2的第一个字符没有分出胜负，但第二个字符'z'>'b',所以s2>s1成立
# 所以我们也可以对下面这个列表排序
# l = ['A', 'z', 'adjk', 'hello', 'hea']
# l.sort()
# print(l)  # ['A', 'adjk', 'hea', 'hello', 'z']
# 9.循环
# 循环遍历my_friends列表里面的值
# my_friends = ['tony', 'jason', 'tom', 4, 5]
# for line in my_friends:
#     print(line)

# # 队列：FIFO,先进先出
# l = []
# #  入队操作
# l.append('first')
# l.append('second')
# l.append('third')
# print(l)
# # 出队操作
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))

# # 堆栈：LIFO,先进后出
# l = []
# #  入栈操作
# l.append('first')
# l.append('second')
# l.append('third')
# print(l)
# # 出栈操作
# print(l.pop())
# print(l.pop())
# print(l.pop())
