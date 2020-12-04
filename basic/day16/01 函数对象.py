# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-29 22:44 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''目录：
一 day17
1.1 函数可以被引用
1.2 函数可以作为容器类型的元素
1.3 函数可以作为参数传入另外一个函数
1.4 函数的返回值可以是一个函数
二 闭包函数
2.1 闭与包
2.2 闭包的用途
'''


# 一 day17
# 函数对象指的是函数可以被当做’数据’来处理，具体可以分为四个方面的使用
# 1.1 函数可以被引用,也可以当成变量去使用
# def add(x, y):
#     return x + y
#
# func = add
# print(func, add)
# func(1, 2)

# 1.2 函数可以作为容器类型的元素
# l = [add]
# # print(l)
# l[0](1, 2)

# dic = {'add': add, 'max': max}
# print(dic)  # {'add': <function add at 0x100661e18>, 'max': <built-in function max>}
# print(dic['add'](1, 2))  # add(1, 2)

# 1.3 函数可以作为参数传入另外一个函数
# def foo(x, y, f):  # foo(1, 2, add函数的内存地址)
#     return f(x, y)  # return add(1,2)
#
# foo(1, 2, add)  # foo(1, 2, add函数的内存地址)

# 1.4 函数的返回值可以是一个函数
# def bar():
#     return add
#
# func = bar()
# func(1, 2)

# 案例一：
def register():
    print("注册功能")


def login():
    print("登录功能")


def recharge():
    print("充值功能")


def transfer():
    print("转账功能")


# dic_func = {"0": ("退出", None),
#             "1": ("注册", register),
#             "2": ("登录", login),
#             "3": ("充值", recharge),
#             "4": ("转账", transfer)}

dic_func = {"0": ["退出", None],
            "1": ["注册", register],
            "2": ["登录", login],
            "3": ["充值", recharge],
            "4": ["转账", transfer]}

while True:
    # print("""
    #     0:退出
    #     1:注册
    #     2:登录
    #     3:充值
    #     4:转账
    #     """)
    for k in dic_func:
        print(k, dic_func[k][0])

    choice = input("请输入你要使用的功能-->>:").strip()
    if not choice.isdigit():
        print("请输入正确的指令：傻叉")
        continue

    if choice == "0":
        break
    # if choice == "1":
    #     register()
    # elif choice == "2":
    #     login()
    # elif choice == "3":
    #     recharge()
    # elif choice == "4":
    #     transfer()
    # else:
    #     print("输入的指令不存在")

    elif choice in dic_func:
        dic_func[choice][1]()
    else:
        print("输入的指令不存在")
