# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-02 23:38 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 3.流程控制之if判断
#     if 条件：
#         代码块
#     elif 条件：
#         代码块
#     else：
#         代码块
# 一 引子：
# 流程控制即控制流程，具体指控制程序的执行流程，而程序的执行流程分为三种结构：
# 顺序结构（之前我们写的代码都是顺序结构）、分支结构（用到if判断）、循环结构（用到while与for）

# 二 分支结构
# 2.1 什么是分支结构
# 分支结构就是根据条件判断的真假去执行不同分支对应的子代码
#
# 2.2 为什么要用分支结构
# 人类某些时候需要根据条件来决定做什么事情，比如：如果今天下雨，就带伞所以程序中必须有相应的机制
# 来控制计算机具备人的这种判断能力

# 2.3 如何使用分支结构
# 2.3.1 if语法
# 用if关键字来实现分支结构，完整语法如下
# if 条件1:   # 如果条件1的结果为True，就依次执行：代码1、代码2，......
#   　代码1
#     代码2
#     ......
# elif 条件2: # 如果条件2的结果为True，就依次执行：代码3、代码4，......
#   　代码3
#     代码4
#     ......
# elif 条件3: # 如果条件3的结果为True，就依次执行：代码5、代码6，......
#   　代码5
#     代码6
#     ......
# else:　　   # 其它情况，就依次执行：代码7、代码8，......
#     代码7
#     代码8
#     ......
# 注意：
# 1、python用相同缩进(4个空格表示一个缩进)来标识一组代码块，同一组代码会自上而下依次运行
# 2、条件可以是任意表达式，但执行结果必须为布尔类型
     # 在if判断中所有的数据类型也都会自动转换成布尔类型
       # 2.1、None，0，空（空字符串，空列表，空字典等）三种情况下转换成的布尔值为False
       # 2.2、其余均为True
# 2.3.2 if应用案例
# 案例1：
# 如果：女人的年龄>30岁，那么：叫阿姨
# age_of_girl=31
# if age_of_girl > 30:
#     print('阿姨好')
# 案例2：
# 如果：女人的年龄>30岁，那么：叫阿姨，否则：叫小姐
# age_of_girl=18
# if age_of_girl > 30:
#     print('阿姨好')
# else:
#     print('小姐好')
# 案例3：
# 如果：女人的年龄>=18并且<22岁并且身高>170并且体重<100并且是漂亮的，那么：表白，否则：叫阿姨**
# age_of_girl=18
# height=171
# weight=99
# is_pretty=True
# if age_of_girl >= 18 and age_of_girl < 22 and height > 170 and weight < 100 and is_pretty == True:
#     print('表白...')
# else:
#     print('阿姨好')
# 案例4：
# 如果：成绩>=90，那么：优秀
# 如果成绩>=80且<90,那么：良好
# 如果成绩>=70且<80,那么：普通
# 其他情况：很差
# score=input('>>: ')
# score=int(score)
# if score >= 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 70:
#     print('普通')
# else:
#     print('很差')
# 案例5：if嵌套
#在表白的基础上继续：
#如果表白成功，那么：在一起
#否则：打印。。。
# age_of_girl=18
# height=171
# weight=99
# is_pretty=True
# success=False
# if age_of_girl >= 18 and age_of_girl < 22 and height > 170 and weight < 100 and is_pretty == True:
#     if success:
#         print('表白成功,在一起')
#     else:
#         print('什么爱情不爱情的,爱nmlgb的爱情,爱nmlg啊...')
# else:
#     print('阿姨好')

# ps：if else简写:
# def func(x, y, z, l=None):  # 规范：不要把默认参数写成可变类型：l=[]
#     if l is None:
#         l = []
#     l.append(x)  # 无论if是否满足，都会执行
#     l.append(y)
#     l.append(z)
#     print(l)
#
# # func(1, 2, 3)
# func(1, 2, 3, [4, 5])


# def func(x, y, z, l=None):  # 规范：不要把默认参数写成可变类型：l=[]
#     if l is None:
#         l = []
#         l.append(x)
#         l.append(y)
#         l.append(z)
#     else:
#         l.append(x)
#         l.append(y)
#         l.append(z)
#     print(l)
#
# func(1, 2, 3)
# func(1, 2, 3, [4, 5])