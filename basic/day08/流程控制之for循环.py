# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-09-23 22:22 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 2.流程控制之for循环
'''
1、什么是for循环
循环就是重复做某件事,for循环是python提供第二种循环机制
2、为何要有for循环
理论上for循环能做的事情,while循环都可以做
之所以要有for循环,是因为for循环在循环取值(遍历取值)比while循环更简洁
3、如何用for循环
语法:
for 变量名 ig可迭代对象:#可迭代对象可以是 :列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
'''
# for循环的基本使用之循环取值
# 案例1：列表循环取值
# # 简单版
# for x in ['alex', 'lxx', 'egon']:
#     print(x)
# # 复杂版
# l = ['alex', 'lxx', 'egon']
# i = 0
# while i < 3:
#     print(l[i])
#     i += 1
# 案例2：字典循环取值
# 简单版
# dic = {'k1': 111, 'k2': 222, 'k3': 333}
# for k in dic:
#     print(k, dic[k])
# 复杂版：whlie也可以遍历字典取值，只是太麻烦了
# dic = {'k1': 111, 'k2': 222, 'k3': 333}  # 下面是自己尝试
# lis = list(dic.keys())
# i = 0
# while i < 3:
#     print(lis[i], dic[lis[i]])
#     i += 1
# 案例3：字符串循环取值
# 简单版
# msg = "you can you up,not can no bb"
# for k in msg:
#     print(k)
# 复杂版：whlie
# 总结：for循环与while循环
# 1.相同之处：都是循环，for循环可以做的事，while也可以做
# 2.不同之处：while循环可称之为条件循环，循环次数取决于条件何时变为假
#             for循环可称之为“取值循环”，循环次数取决于in后包含值的个数

# for循环控制循环次数：range
# 下面的方式有局限性：
# for x in [1, 2, 3]:  # [1, 2, 3, 4, 5, 6, 7, 8......]
#     input_name = input('your username：')
#     input_pwd = input('your password：')

# range功能介绍
''' python2
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> range(1,9) # 1...8
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
>>> range(1,9,1) # 1 2 3 4 5 6 7 8
[1, 2, 3, 4, 5, 6, 7, 8]
>>> range(1,9,2) # 1 3 5 7
[1, 3, 5, 7] I
'''
# for i in range(3):
#     print("===>")

# for+break:同while循环一样
# for+else:同while循环一样
# username = 'egon'
# password = '123'
# for i in range(3):
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         while True:
#             cmd = input("请输入命令的编号>>>:")
#             if cmd == 'q':  # 整个程序结束，退出所有while循环
#                 break
#             else:
#                 print("{x}命令正在执行中".format(x=cmd))
#         break
#     else:
#         print('账号或密码输入有误')
# else:  # else包含的代码会在for循环结束后，并且for循环是在没有被break打断的情况下正常结束，才会运行
#     print("输入错误次数超过3次")

# range补充知识（了解）
# 1、for搭配range，可以按照索引取值，但是麻烦，所以不推荐
# l = ['aaa', 'bbb', 'ccc']
# for i in range(3):
#     print(l[i])
#
# for x in l:
#     print(x)
# 2、range()在python3中得到的是一只"会下蛋的老母鸡"
# >>> range(10)  # python3
# range(0, 10)

# for+continue:结束本次循环，直接进入下一次
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)

# for循环嵌套:外层循环循环一次，内层循环需要完整的循环完毕
# for i in range(3):
#     print("外层循环-->", i)
#     for j in range(5):
#         print("内层循环-->", j)

# 补充for循环只有break一种方案

# print
# print('hello', 'world', 'egon')  # 逗号可以理解成空格
# print('hello\n')  # 换行符
# print('world')
# print('hello', end='')  # 去除换行符
# print('world')
# print('hello', end='*')  # 替换换行符
# print('world')

# 3.基本数据类型及其内置方法
# 1、数字：int   float
# 2、字符串
# 3、列表
# 4.基本数据类型及其内置方法
# 1、元祖（tuple）
# 2、字典
# 3、集合（了解）
# 5.文件处理基本操作
# 1、字符编码
# 编码与编码
# 保证不乱码：以什么编码格式存的就必须以什么编码格式
# 2、文件处理
# 文件处理基本流程
# with语法
# 操作模式
#     控制文件读写的模式：r、w、a
#     控制文件读写内容的模式：t、b
# 6.文件处理的高级部分
# 操作文件的办法
# 控制文件指针的移动
# 文件的修改的两种方式

