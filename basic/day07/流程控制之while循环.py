# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-02 23:09 
# @Software：PyCharm
# 1.流程控制之while循环
# 1）while循环的基本使用：
"""
while 条件：
    代码1
    代码2
    代码3
"""
# 2）死循环与效率问题
# count = 0
# while count < 5:
#     print(count)

# while True:
#     name = input('your name >>>>')
#     print(name)

# 纯计算无IO的死循环会导致致命的效率问题
# while True:
#     1+1

#  3）循环的应用
# username = 'egon'
# password = '123'
# while True:
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#     else:
#         print('账号或密码输入有误，请重新输入')

# 4）退出while循环的两种方式：
#     方式一：条件改为false（等到下次循环判断条件时才会生效）
# username = 'egon'
# password = '123'
# tag = True
# while tag:
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         tag = False  # 之后的代码还会运行，下次循环判断条件时才会生效
#     else:
#         print('账号或密码输入有误，请重新输入')
#     print('==========end=========')

#     方式二：while+break，只要运行到break就会立即终止本层循环
# username = 'egon'
# password = '123'
# while True:
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         break  # 立刻终止本层循环
#     else:
#         print('账号或密码输入有误，请重新输入')
#     print('==========end=========')

# 5）while循环嵌套
"""
在最内层一次性把所有循环终止
tag = True
while tag:
    while tag:
        while tag:
            tag = False

每一层都必须配一个break
while True:
    while True:
        while True:
            break
        break
    break  # 立刻终止本层循环
"""
# 多层循环案例：
# break的方式：
# username = 'egon'
# password = '123'
# while True:
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         while True:
#             cmd = input("请输入命令的编号>>>:")
#             if cmd == 'q':
#                 break
#             print("{x}命令正在执行中".format(x=cmd))
#         break  # 立刻终止本层循环
#     else:
#         print('账号或密码输入有误，请重新输入')

# 改变条件的方式
# username = 'egon'
# password = '123'
# tag = True
# while tag:
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         while tag:
#             cmd = input("请输入命令的编号>>>:")
#             if cmd == 'q':
#                 tag = False
#             else:  # 改变条件的方式会把同一级别下的代码都执行完才结束循环，这里为q不应该执行下面的print，所以加上else
#                 print("{x}命令正在执行中".format(x=cmd))
#     else:
#         print('账号或密码输入有误，请重新输入')

# while+continue：结束本次循环，直接进入下一次
# 强调：在continue之后添加同级代码毫无意义，因为永远无法运行(continue之后的本次都不会运行)
# count = 0  # 打印0,1,2,3,5
# while count < 6:
#     if count == 4:
#         count += 1
#         continue
#     print(count)
#     count += 1

# while+else: 针对break
# else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下正常结束，才会运行
# count = 0
# while count < 6:
#     if count == 4:
#         count += 1
#         continue
#     print(count)
#     count += 1
# else:
#     print('else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下正常'
#           '结束，才会运行')

# count = 0
# while count < 6:
#     if count == 4:
#         break
#     print(count)
#     count += 1
# else:  # 不会运行
#     print('else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下正常'
#           '结束，才会运行')

# 应用案例：
# 版本一：
# username = 'egon'
# password = '123'
# tag = True
# count = 0
# while tag:
#     if count == 3:
#         print("输入错误次数超过3次")
#         break
#     input_name = input('your username：')
#     input_pwd = input('your password：')
#     if input_name == username and input_pwd == password:
#         print('登录成功')
#         while tag:
#             cmd = input("请输入命令的编号>>>:")
#             if cmd == 'q':
#                 tag = False
#             else:  # 改变条件的方式会把同一级别下的代码都执行完才结束循环，这里为q不应该执行下面的print，
#                   所以加上else
#                 print("{x}命令正在执行中".format(x=cmd))
#     else:
#         print('账号或密码输入有误，请重新输入')
#         count += 1
# 版本二：优化
# username = 'egon'
# password = '123'
# count = 0
# tag = True
# while count < 3:
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
#         count += 1
# else:
#     print("输入错误次数超过3次")