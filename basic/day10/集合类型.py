# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-09 23:28 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 集合
# 定义：
# 1. 作用：集合是一个无序的，不重复的数据组合，主要用于：去重、关系运算
# 1.1 关系运算:测试两组数据之间的交集，差集，并集等关系
# friend1 = ['zero', 'kevin', 'jason', 'egon']  # 用户1的好友们
# friends2 = ["Jy", "ricky", "jason", "egon"]   # 用户2的好友们
# 求共同好友
# l = []
# for x in friend1:
#     if x in friends2:
#         l.append(x)
# print(l)
# 1.2 去重:把一个列表变成集合，就自动去重了

# 2. 定义：在{}内用逗号分隔开多个元素，集合具备以下三个特点：
#      1：集合内元素必须是不可变类型
#      2：集合内没有重复的元素
#      3：集合内元素无序
# s = {1, 2, 3, 4}  # 本质 s = set({1, 2, 3, 4})
# 注意1：列表类型是索引对应值，字典是key对应值，均可以取得单个指定的值，而集合类型既没有索引也没有key与值对应，
# 所以无法取得单个的值，而且对于集合来说，主要用于去重与关系运算，根本没有取出单个指定值这种需求。
# 注意2:{}既可以用于定义dict，也可以用于定义集合，但是字典内的元素必须是key:value的格式，
# 现在我们想定义一个空字典和空集合，该如何准确去定义两者?
# d = {}  # 默认是空字典
# s = set() # 这才是定义空集合
# 3.类型转换
# s = set({1, 2, 3})  # {1, 2, 3}
# print(s, type(s))
# 字符串转
# s = set('hellolllll')
# print(s, type(s))
# 列表转
# s = set([1,1,1,1,1,1])
# print(s, type(s))
# 字典转
# s = set({'k1':111,'k2':222})
# print(s, type(s))

# 4.内置方法
# =======================================关系运算===========================================
# friends1 = {"zero", "kevin", "jason", "egon"}  # 用户1的好友们
# friends2 = {"Jy", "ricky", "jason", "egon"}  # 用户2的好友们
# 4.1 合集/并集(|)：求两个用户所有的好友（重复好友只留一个）
# res = friends1 | friends2
# print(res)  # {'kevin', 'ricky', 'zero', 'jason', 'Jy', 'egon'}
# print(friends1.union(friends2))
# 4.2 交集(&)：求两个用户的共同好友
# print(friends1 & friends2)  # {'jason', 'egon'}
# print(friends1.intersection(friends2))
# 4.3 差集(-)：
# print(friends1 - friends2)  # 求用户1独有的好友  # {'kevin', 'zero'}
# print(friends1.difference(friends2))
# print(friends2 - friends1)  # 求用户2独有的好友  # {'ricky', 'Jy'}
# print(friends2.difference(friends1))
# 4.4 对称差集(^) # 求两个用户独有的好友们（即去掉共有的好友）
# print(friends1 ^ friends2)  # {'kevin', 'zero', 'ricky', 'Jy'}
# print(friends1.symmetric_difference(friends2))
# 4.5 值是否相等(==)
# print(friends1 == friends2)  # False
# 4.6 父集：一个集合是否包含另外一个集合
# 4.6.1 包含则返回True
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1 > s2)  # True
# print(s1.issuperset(s2))
# print(s1 >= s2)  # True  # 当s1大于或等于s2的时候，才能说是它的爹
# s1 = {1, 2}
# s2 = {1, 2}
# print(s1 == s2)  # True  # s1与s2互为父子
# print(s1.issuperset(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# 4.6.2 不存在包含关系，则返回False
# print({1, 2, 3} > {1, 3, 4, 5})  # False
# print({1, 2, 3} >= {1, 3, 4, 5})  # False
# 7.子集
# s1 = {1, 2}
# s2 = {1, 2, 3}
# print(s1 < s2)  # True
# print(s1.issubset(s2))
# print({1, 2} <= {1, 2, 3})  # True

# =======================================去重===========================================
# 集合去重复有局限性
# 1. 只能针对不可变类型
# print(set([1, 2, 3, 4, 4, 4]))
# 2. 集合本身是无序的，去重之后无法保留原来的顺序
# l = ['a', 'b', 1, 'a', 'a']
# s = set(l)
# print(s)  # 将列表转成了集合  # {'b', 'a', 1}
# l_new = list(s)  # 再将集合转回列表
# print(l_new)  # ['b', 'a', 1] # 去除了重复，但是打乱了顺序

# 针对不可变类型，并且保证顺序则需要我们自己写代码实现，例如
l = [
    {'name': 'lili', 'age': 18, 'sex': 'male'},
    {'name': 'jack', 'age': 73, 'sex': 'male'},
    {'name': 'tom', 'age': 20, 'sex': 'female'},
    {'name': 'lili', 'age': 18, 'sex': 'male'},
    {'name': 'lili', 'age': 18, 'sex': 'male'},
]
# new_l = []
# for dic in l:
#     if dic not in new_l:
#         new_l.append(dic)
# print(new_l)
# 结果：既去除了重复，又保证了顺序，而且是针对不可变类型的去重
'''
[
    {'age': 18, 'sex': 'male', 'name': 'lili'},
    {'age': 73, 'sex': 'male', 'name': 'jack'},
    {'age': 20, 'sex': 'female', 'name': 'tom'}
]
'''
# 其他操作
# 1.长度
# s = {'a', 'b', 'c'}
# print(len(s))  # 3
# 2.成员运算
# print('c' in s)  # True
# 3.循环
# for item in s:
#     print(item)

# 其他内置方法:
# 需要掌握的内置方法：1.discard  2.update  3.pop  4.add
# discard： 删除元素
# s = {1, 2, 3}
# s.discard(1)
# print(s)
# s.discard(4)  # 容错性好，删除元素不存在不会报错
# s.remove(4)  # 删除元素不存在则报错

# update:把新数据加到老数据里，并且去重
# s.update({4, 5, 3})
# print(s)

# pop:随机删除
# s.pop()
# print(s)

# add：添加
# s.add(4)
# print(s)

# 了解
# difference_update:求差集，并把差集赋值给原变量
# s.difference_update({3, 4, 5})  # s = s.difference_update({3, 4, 5})
# print(s)

# isdisjoint: 两个集合完全独立，没有共同部分，返回True
# res = s.isdisjoint({4, 5, 6})
# print(res)
