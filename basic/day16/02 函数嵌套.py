# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-30 22:00 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 函数嵌套
# 1.函数的嵌套使用：在调用一个函数的过程中又调用其他函数
def bar():
    pass

def foo():
    bar()

foo()
# 2.函数的嵌套定义：在函数内定义函数
def f1():
    def f2():
        pass
    f2()

# 案例：圆形
# 1.求圆形的周长:2*pi**radius
def circle(radius, action):
    from math import pi

    def perimiter(radius):
        return 2*pi**radius

    # 2.求圆形的面积:pi*(radius**2)
    def area(radius):
        return pi*(radius**2)

    if action == 0:
        return perimiter(radius)

    elif action == 1:
        return "面积", area(radius)

    else:
        return "你的输入有误"

print(circle(12, 1))