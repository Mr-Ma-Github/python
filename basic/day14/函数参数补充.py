# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-25 0:19 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 2.5 命名关键字参数
# 在定义了**kwargs参数后，函数调用者就可以传入任意的关键字参数key=value，如果函数体代码的执行
# 需要依赖某个key，必须在函数内进行判断
# def register(name, age, **kwargs):
#     if 'sex' in kwargs:
#         # 有sex参数
#         pass
#     if 'height' in kwargs:
#         # 有height参数
#         pass
# 想要限定函数的调用者必须以key=value的形式传值，Python3提供了专门的语法：需要在定义形参时，
# 用作为一个分隔符号，号之后的形参称为命名关键字参数。对于这类参数，在函数调用时，必须按照
# key=value的形式为其传值，且必须被传值
# 命名关键字参数：在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数
# 特点：
# １.命名关键字参数后，必须按照key=value的形式为其传值
# def register(name, age, *, sex, height):  # sex,height因为二者均在*后，为命名关键字参数
#     pass
#
# register('lili', 18, sex='male', height='1.8m')  # 正确使用
# register('lili', 18, 'male', '1.8m')  # TypeError:未使用关键字的形式为sex和height传值
# register('lili', 18, height='1.8m')  # TypeError没有为命名关键字参数height传值。

# 2.命名关键字参数也可以有默认值，从而简化调用
# def register(name, age, *, sex='male', height):
#     # 默认参数不能跟在位置参数后面，但是sex不是默认参数，是给命名关键字参数赋了个默认值
#     print('Name:%s,Age:%s,Sex:%s,Height:%s' % (name, age, sex, height))
#
# register('lili', 18, height='1.9m')  # Name:lili,Age:18,Sex:male,Height:1.8m
# 需要强调的是：sex不是默认参数，height也不是位置参数，因为二者均在后，所以都是命名关键字参数，
# 形参sex=’male’属于命名关键字参数的默认值，因而即便是放到形参height之前也不会有问题。

# 如果形参中已经有一个args了，命名关键字参数就不再需要一个单独的*作为分隔符号了
# def register(name, age, *args, sex='male', height):
#     print('Name:%s,Age:%s,Args:%s,Sex:%s,Height:%s' % (name, age, args, sex, height))
#
# register('lili', 18, 1, 2, 3, height='1.8m')  # sex与height仍为命名关键字参数
# # Name:lili,Age:18,Args:(1, 2, 3),Sex:male,Height:1.8m


# 2.6 组合使用
# 综上所述所有参数可任意组合使用，但定义顺序必须是：位置参数、默认参数、*args、命名关键字参数、**kwargs
# 可变参数*args与关键字参数**kwargs通常是组合在一起使用的，如果一个函数的形参为*args与**kwargs，
# 那么代表该函数可以接收任何形式、任意长度的参数
# def wrapper(*args,**kwargs):
#     pass

# 在该函数内部还可以把接收到的参数传给另外一个函数（这在4.6小节装饰器的实现中大有用处）
# def func(x,y,z):
#     print(x,y,z)
#
# def wrapper(*args,**kwargs):
#     func(*args,**kwargs)
#
# wrapper(1,z=3,y=2)  # 1 2 3
# 按照上述写法，在为函数wrapper传参时，其实遵循的是函数func的参数规则，调用函数wrapper的过程分析如下：
# 位置实参1被接收，以元组的形式保存下来，赋值给args，即args=(1,),关键字实参z=3，y=2被*接收，
# 以字典的形式保存下来，赋值给kwargs，即kwargs={'y': 2, 'z': 3}
# 执行func(args,kwargs),即func((1,),* {'y': 2, 'z': 3}),等同于func(1,z=3,y=2)
