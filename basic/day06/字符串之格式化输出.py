# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-02 23:18 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 字符串的格式化输出
# %
# %s:可以接收任意类型，注意：需按照位置，一一对应
# res = "my name is %s" % 'egon'
# res = "my name is %s, my age is %s" % ('egon', '18')
# 以字典的形式传值，打破位置的限制
# res = "我的名字是 %(name)s, 我的年龄是 %(age)s" % {'name': 'egon', 'age': '18'}
# res = "成功的概率是：%s%%" % 97  # %% 可以输出一个%
# print(res)
# 指定占位符宽度（左对齐）
# print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))

# %d：只能接收整型int
# res = "my name is %d, my age is %d" % (10, 18)
# print(res)

# %f：可以接收整型int和浮点型float，但是会默认保留小数点后6位
res = "my name is %f, my age is %f" % (10, 18)
print(res)
print("His height is %.2f m" % 1.83)  # 可以通过 %.小数点长度f 来控制小数点的长度

# format ：兼容性好
# 按照位置传值
# res = "我的名字是 {}, 我的年龄是 {}".format('egon', 18)
# res = "我的名字是 {0}, 我的年龄是 {1}".format('egon', 18)
# res = "我的名字是 {{{0}}}, 我的年龄是 {{{1}}}".format('egon', 18)  # {{ 可以输出一个{
# res = "我的名字是 {0}{0}, 我的年龄是 {1}{1}{1}".format('egon', 18)
# print(res)
# 打破位置的限制，按照key = value传值
# res = "我的名字是{name}, 我的年龄是 {age}".format(name='egon', age=18)
# print(res)
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name},地址 {url}".format(**site))  # 双星号（**）：**kwargs将参数以字典的形式导入
print(*site)
# 字典前双星号：双星号（**）：**kwargs将参数以字典的形式导入
# def tuple_unpack(b):
#     print(b)
# ff = {'one': 1, 'two': 2, 'three': 3}
# tuple_unpack(ff)
# 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
# print("网站名：{my_list[0]}, 地址: {my_list[1]}".format(my_list=my_list))
# print("网站名：{0}, 地址: {1}".format(*my_list))  # 列表前面加星号作用是将列表解开成两个独立的参数
# format:填充与格式化
# print('{x}======'.format(x="开始执行"))  # 开始执行======
# print('{x:=<10}'.format(x="开始执行"))  # 开始执行======
# print('{x:=>10}'.format(x="开始执行"))  # ======开始执行
# print('{x:=^10}'.format(x="开始执行"))  # ===开始执行===
# format:精度与进制
# print('{salary:.3f}'.format(salary=123456.12356))  # 精确到小数点后三位，且自动四舍五入

# f  :python3.5以后才推出
# x = input("your name:")
# y = input("your age: ")
# res = f"我的名字是{x}, 我的年龄是 {y}"
# res = f"{10+3}"  # {}中的字符串可以被当做表达式运行
# print(res)
# f'{print("aaaa")}'