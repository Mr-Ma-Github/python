# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-04 22:19 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 一、字符串类型str
# 作用：记录描述性质的状态、名字、一段话等等
# 定义：
# msg = 'hello'  # msg = str('hello')
# print(type(msg))
# 类型转换:
# str 可以把任意其他类型都转成字符串
# res = str({'a':1})
# print(res, type(res))
# 使用：内置方法
# 优先掌握
# 1.按索引取值（正向+反向）：只能取
# msg = 'hello world'
# 正向取值
# print(msg[0])
# print(msg[5])
# 反向取值
# print(msg[-1])
# 2.切片:索引的拓展应用，从一个大字符串中拷贝出一个子字符串（顾头不顾尾，步长）
# msg = 'hello world'
# 顾头不顾尾
# print(msg[0:5])  # hello
# print(msg[:])  # 正向取所有
# 步长
# print(msg[0:5:2])  # 0 2 4  - hlo
# 反向步长
# print(msg[5:0:-1])
# print(msg[::-1])  # 反向取所有
# 3.长度len
# print(len(msg))
# 4.成员运算符in和not in
# msg = 'hello world'
# print('h'in msg)  # True
# print('h'not in msg)  # False
# print(not 'h' in msg)  # False
# 5.移除字符串左右两侧的字符strip
# 默认去掉空格
# msg = '   egon   '
# res = msg.strip()
# print(msg)  # 不会改变原值
# print(res)  # 是产生了新值   打印结果：egon
# msg = '*****egon***'
# print(msg.strip('*'))  # 只去除左右两侧的
# print(msg.lstrip('*'))  # 只去除左侧的
# print(msg.rstrip('*'))  # 只去除右侧的
# ms = '**/*=-**egon**-=()**'
# print(ms.strip('*/=-()'))  # 可以写多个
# 应用：
# inp_username = input("请输入你的账号：").strip()  # 规避空格

# 6.切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
# # 默认按照空格切分
# info = 'egon 18 male'
# print(info.split())  # ['egon', '18', 'male']
# 指定分隔符
# info = 'egon:18:male'
# print(info.split(':'))  # ['egon', '18', 'male']
# # 指定分隔符和分隔次数
# info = 'egon:18:male'
# print(info.split(':', 1))  # ['egon', '18:male']
# 7.循环
# for x in info:
#     print(x)

# 需要掌握
# 1.strip, lstrip, rstrip
# msg = '    egon   '
# print(msg.strip())  # 默认去除左右两侧的空格
# msg = '*****egon***'
# print(msg.strip('*'))  # 只去除左右两侧的
# print(msg.lstrip('*'))  # 只去除左侧的
# print(msg.rstrip('*'))  # 只去除右侧的
# 2.lower, upper()
# msg = 'AaaabBbcC'
# print(msg.lower())  # 小写
# print(msg.upper())  # 大写
# 3.startswith, endswith
# print('alex is sb'.startswith('alex'))  # 判断是否以（）中的内容开头
# print('alex is sb'.endswith('sb'))  # 判断是否以（）中的内容结尾
# 4.fomat的三种玩法
# res = "我的名字是 {0}, 我的年龄是 {1}".format('egon', 18)
# res = "我的名字是 {name}, 我的年龄是 {age}".format(name='egon', age=18)
# res = "我的名字是 {name}, 我的年龄是 {age}".format(**{'name': 'egon', 'age': 18})
# print(res)
# # 5.split, rsplit
# info = 'egon:18:male'
# print(info.split(":", 1))  # ['egon', '18:male']
# print(info.rsplit(":", 1))  # ['egon:18', 'male']
# 6.join:把列表拼接成字符串
# l = ['egon', '18', 'male']
# res = l[0]+':'+l[1]+':'+l[2]
# res1 = ':'.join(l)  # 按照某个分隔符号，把元素全为字符串的列表拼接成一个大字符串
# print(res1)
# 注意：下面这个拼接结果
# a = 'dsfg'
# b = 'xfc'
# print(','.join(a+b))  # d,s,f,g,x,f,c

# 7.replace：替换  def replace(self, old, new, count=None)
# mag = "you can you up no can no BB"
# print(mag.replace('you', 'You'))
# print(mag.replace('you', 'You', 1))

# 8.isdigit()：判断字符串是否由纯数字组成(正整数)
# print('123'.isdigit())  # True
# print('-123'.isdigit())  # False

# 了解
# 1.find，rfind，index，rindex，count
mag = 'hello egon haahah'
if mag.find('z') == -1:
    print("找不到")
else:
    print("找到了")
# find找到返回起始索引
# print(mag.find('e'))  # 返回要查找的字符串在大字符串中的起始索引
# print(mag.find('egon'))
# print(mag.rfind('egon'))
# print(mag.index('egon'))  # 返回要查找的字符串在大字符串中的起始索引
# print(mag.rindex('egon'))
# 区别在于find找不到返回-1，index找不到会报错
# x = mag.find('xxx')
# print(x, type(x))
# print(mag.find('xxx'))  # 返回-1(int)，代表找不到
# print(mag.index('xxx'))  # ValueError: substring not found
# print(mag.count('h'))  # 返回要查找的字符串在大字符串中的出现次数

# 2.center，ljust，rjust，zfill （控制打印格式）
# print('egon'.center(50, '*'))  # egon居中，其余的用*补充
# print('egon'.ljust(50, '*'))  # egon居左侧，其余的用*补充
# print('egon'.rjust(50, '*'))  # egon居右侧，其余的用*补充
# print('egon'.zfill(50))  # egon居右侧，其余的用0补充

# 3.expandtabs:控制制表符的宽度
# msg = 'hello\tworld'
# print(msg.expandtabs(2))  # 设置制表符代表的空格数为2

# 4.captalize，swapcase，title
# print('hello world egon'.capitalize())  # 字符串首字母大写
# print('hello world EGON'.swapcase())  # 字符串所有字符大小写反转
# print('hello world egon'.title())  # 每个单词的首字母大写

# 5.is数字系列
num1 = b'4' #bytes
num2 = u'4' #unicode,python3中无需加u就是unicode（阿拉伯数字）
num3 = '四' #中文数字
num4 = 'Ⅳ' #罗马数字(注意：不是IV-不可分割，罗马数字4)
# isdigit
# isdigit只能识别num1、num2
# print(num1.isdigit())  # True
# print(num2.isdigit())  # True
# print(num3.isdigit())  # False
# print(num4.isdigit())  # False
# isnumeric
# isnumeric只能识别num2、num3、num4
# print(num2.isnumeric())  # True
# print(num3.isnumeric())  # True
# print(num4.isnumeric())  # True
# isdecimal
# isdecimal只能识别num2
print(num2.isdecimal())  # True
print(num3.isdecimal())  # False
print(num4.isdecimal())  # False
# 6.is其他
# print('abC'.islower())  # 判断是否全为小写
# print('abC'.isupper())  # 判断是否全为大写
# print('Abc Egon'.istitle())  # 判断单词的首字母是否全为大写
# print('abC1122。'.isalnum())  # 判断字符串是否为字母或数字组成
# print('abC'.isalpha())  # 判断字符串是否为字母组成
# print('   '.isspace())  # 判断字符串是否全为空格组成
# print('abC'.isidentifier())  # 判断标识符是否合法
# print('abC\t'.isprintable())  # 判断是否为可打印字符。不可打印的字符可以是回车和换行符
