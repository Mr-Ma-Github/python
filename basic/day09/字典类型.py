# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-09 17:46 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 字典
# 作用：是用来记录多个值的，但是这多个值是通过key对应值。key通常是str类型，对value有描述性的功能
# 定义：定义：在{}内用逗号分隔开多元素，每一个元素都是key:value的形式，其中value可以是任意类型，
# 而key则必须是不可变类型且不能重复
# info = {'name': 'tony', 'age': 18, 'sex': 'male'}  # 本质info=dict({....})
# 也可以这么定义字典
# info1 = dict(name='tony', age=18, sex='male')  # info1={'age': 18, 'sex': 'male', 'name': 'tony'}
# 类型转换：
# 转换1:
# info = dict([['name', 'tony'], ('age', 18)])
# print(info)  # {'name': 'tony', 'age': 18}
# 转换2：
# 快速初始化一个字典
# keys = ['name', 'age', 'gender']
# 需求：{'name': None, 'age': None, 'sex': None}
# fromkeys会从元组中取出每个值当做key，然后与None组成key:value放到字典中
# print({}.fromkeys(('name', 'age', 'sex'), None))  # {'age': None, 'sex': None, 'name': None}
# 内置方法：
# 1.优先掌握的操作
# 1、按key存取值：可存可取
# 1.1 取
# dic = {'name': 'xxx', 'age': 18, 'hobbies': ['play game', 'basketball']}
# print(dic['name'])  # 'xxx'
# print(dic['hobbies'][1])  # 'basketball'
# 1.2 对于赋值操作，如果key原先不存在于字典，则会新增key:value
# dic['gender'] = 'male'
# print(dic)  # {'name': 'tony', 'age': 18, 'hobbies': ['play game', 'basketball'],'gender':'male'}
# 1.3 对于赋值操作，如果key原先存在于字典，则会修改对应value的值
# dic['name'] = 'tony'
# print(dic)  # {'name': 'tony', 'age': 18, 'hobbies': ['play game', 'basketball']}
# 2、长度len
# print(len(dic))  # 3
# 3、成员运算in和not in
# print('name' in dic)  # 判断某个值是否是字典的key    # True
# 4、删除
# 4.1 通用删除
# del dic['age']
# print(dic)
# 4.2 pop():通过指定字典的key来删除字典的键值对,会返回删除key对应的value
# x = dic.pop('name')
# print(dic)  # {'age': 18, 'hobbies': ['play game', 'basketball']}
# print(x)  # 返回删除key对应的value
# 4.2 popitem()：随机删除，返回元祖（删除的key, 删除的value）
# dic.popitem()
# print(dic)
# 5、键keys()，值values()，键值对items()==》在python3中得到的是老母鸡
# dic = {'age': 18, 'hobbies': ['play game', 'basketball'], 'name': 'xxx'}
# 获取字典所有的key
# print(dic.keys())  # dict_keys(['name', 'age', 'hobbies'])
# print(list(dic.keys()))  # 可直接转换成列表
# 获取字典所有的value
# print(dic.values())  # dict_values(['xxx', 18, ['play game', 'basketball']])
# 获取字典所有的键值对
# print(dic.items())  # dict_items([('name', 'xxx'), ('age', 18), ('hobbies', ['play game', 'basketball'])])
# 6、循环
# 6.1 默认遍历的是字典的key
# for key in dic:
#     print(key)
# 6.2 只遍历key
# for key in dic.keys():
#     print(key)
# 6.3 只遍历value
# for key in dic.values():
#     print(key)
# 6.4 遍历key与value
# for key in dic.items():
#     print(key)
# for key, value in dic.items():  # 解压操作
#     print(key, value)

# 需要掌握的内置方法：
# 1.clear:清空字典
# d = {'k1': 111}
# d.clear()
# print(d)
# 2.update()
# 用新字典更新旧字典，有则修改，无则添加
# dic = {'k1': 'jason', 'k2': 'Tony', 'k3': 'JY'}
# dic.update({'k1': 'JN', 'k4': 'xxx'})
# print(dic)  # {'k1': 'JN', 'k3': 'JY', 'k2': 'Tony', 'k4': 'xxx'}
# 3.get:根据key取值，容错性好
# dic = {'k1': 'jason', 'k2': 'Tony', 'k3': 'JY'}
# dic.get('k1')  # 'jason'  # key存在，则获取key对应的value值
# res = dic.get('xxx')  # key不存在，不会报错而是默认返回None
# print(res)  # None
# res = dic.get('xxx', 666)  # key不存在时，可以设置默认返回的值
# print(res)  # 666
# ps:字典取值建议使用get方法
# 4.setdeafault()
# info = {'name1': 'egon'}
# if 'name' in info:
#     ...  # 等同于pass
# else:
#     info['name'] = 222
# print(info)
# 4.1:如果key有则不添加，返回字典中key对应的值
info = {'name': 'egon'}
res = info.setdefault('name', 'sdg')
print(info)
print(res)
# 4.2:如果key没有则添加，返回字典中key对应的值
info = {'name': 'egon'}
res = info.setdefault('name1', 'egon1')
print(info)
print(res)
