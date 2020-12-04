# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-02 23:09 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# day05：（*****）
# 短路运算（了解）：偷懒原则，偷懒到哪个位置，就把当前位置的值返回
# 深浅copy
# 如何拷贝列表？
# 浅拷贝：是把原列表第一层的内存地址不加区分完全copy一份给新列表
# 列表名.copy()
# list1 = ['egon', 'lxx', [1, 2]]
# list3 = list1.copy()
# # print(list3)
# print(id(list1))
# print(id(list3))
# print(id(list1[0]),id(list1[1]),id(list1[2][0]),id(list1[2][1]))
# print(id(list3[0]),id(list3[1]),id(list3[2][0]),id(list3[2][1]))

# 实验1:对于不可变类型的赋值,都是产生了新值，让原列表的索引指向新的内存地址，并不会影响新列表
# list1[0] = 'EGON'
# list1[1] = 'LXX'
# list1[2] = 123  # 改变list[2]为一个不可变类型，在堆区产生新的值，只会改变list1
# print(list1)
# print(list3)

# 实验2:但对于可变类型,我们可以改变可变类型中包含的值,但内存地址不变
# 即原列表的索引一指向仍然指向原来的内存地址,于是新列表也跟着一起受影响,如下
# list1[2][0]=111  # 改变list[2]这个容器中的值，list2的内存地址未变，会同步改变list1、list3
# list1[2][1]=222
# print(list1)
# print(list3)

# 综合实验1和实验2可以得出,要想copy得到的新列表与原列表的改操作完全独立开,并且针对的改操作的独立
# 而不是读操作，必须有一种可以区分开可变类型与不可变类型的copy机制,这就是深copy

# 深拷贝：
# import copy
# list1 = ['egon', 'lxx', [1, 2]]
# list3 = copy.deepcopy(list1)
# print(id(list1))
# print(id(list3))
# #       不可变       不可变       可变
# print(id(list1[0]), id(list1[1]), id(list1[2]))  # 4703360 6357792 6718848
# print(id(list3[0]), id(list3[1]), id(list3[2]))  # 4703360 6357792 6719768
# print(id(list1[2][0]), id(list1[2][1]))
# print(id(list3[2][0]), id(list3[2][1]))
#
# list1[0] = 'EGON'
# list1[1] = 'LXX'
# list1[2][0] = 111
# list1[2][1] = 222
# print(list1)
# print(list3)
