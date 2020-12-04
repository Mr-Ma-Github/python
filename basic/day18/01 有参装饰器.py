# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-12-02 22:58 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 一 知识储备
# 由于语法糖的限制，outter函数只能有一个参数，并且该函数只用来接收被装饰对象的内存地址
def outter(func):
    # func = index的内存地址
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@outter # index = outter(index的内存地址)
def index(x, y):
    print(x, y)

# 偷梁换柱之后：
# index的参数什么样子，wrapper的参数就应该是什么样子
# index的返回值什么样子，wrapper的返回值就应该是什么样子
# index的属性什么样子，wrapper的属性就应该是什么样子

# 需求：在功能调用之前加上文件认证功能
# def outter(func):  # func = index的内存地址
#     def wrapper(*args, **kwargs):
#         name = input('your username>>:').strip()
#         pwd = input('your password>>:').strip()
#         with open('user.txt', mode='rt', encoding='utf-8')as file:
#             for line in file:
#                 res = line.strip('\n').split(':')
#                 if name == res[0] and pwd == res[1]:
#                     print('login success')
#                     res = func(*args, **kwargs)
#                     return res
#                     # break  # 因为有return所以省略了break
#             else:  # else包含的代码会在for循环结束后，并且for循环是在没有被break打断的情况下正常结束，才会运行
#                 print("username or password error")
#     return wrapper
#
# @outter # index = outter(index的内存地址)
# def index(x, y):
#     print(x, y)
#
#
# index(1, 2)

# 需求：在功能调用之前加上认证功能（多种认证方式）
# 山炮玩法一：
# def auth(func, db_type):  # func = index的内存地址
#     def wrapper(*args, **kwargs):
#         name = input('your username>>:').strip()
#         pwd = input('your password>>:').strip()
#         if db_type == 'file':
#             print('基于文件的验证')
#             if name == 'egon' and pwd == '123':
#                 print('login success')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print("username or password error")
#         elif db_type == 'database':
#             print('基于数据库的验证')
#             ...
#         elif db_type == 'ldap':
#             print('基于ldap的验证')
#             ...
#         else:
#             print('不支持该db_type')
#     return wrapper
#
# # @auth  # 账号密码的来源是文件
# def index(x, y):
#     print(x, y)
#
# # @auth  # 账号密码的来源是数据库
# def database(x, y):
#     print(x, y)
#
# # @auth  # 账号密码的来源是ldap
# def ldap(x, y):
#     print(x, y)
#
# index = auth(index, 'file')
# database = auth(database, 'database')
# ldap = auth(ldap, 'ldap')

# index(1, 2)
# database(1, 2)
# ldap(1, 2)

# # 山炮玩法二：
# def db(db_type):
#     def auth(func):  # func = index的内存地址
#         def wrapper (*args, **kwargs):
#             name = input('your username>>:').strip()
#             pwd = input('your password>>:').strip()
#             if db_type == 'file':
#                 print('基于文件的验证')
#                 if name == 'egon' and pwd == '123':
#                     print('login success')
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print("username or password error")
#             elif db_type == 'database':
#                 print('基于数据库的验证')
#                 ...
#             elif db_type == 'ldap':
#                 print('基于ldap的验证')
#                 ...
#             else:
#                 print('不支持该db_type')
#         return wrapper
#     return auth
#
# auth = db(db_type='file')
# @auth # 账号密码的来源是文件
# def index(x, y):
#     print(x, y)
#
# auth = db(db_type='database')
# @auth # 账号密码的来源是数据库
# def database(x, y):
#     print(x, y)
#
# auth = db(db_type='ldap')
# @auth # 账号密码的来源是ldap
# def ldap(x, y):
#     print(x, y)
#
# index(1, 2)
# database(1, 2)
# ldap(1, 2)

# 语法糖：
from functools import wraps
def db(db_type):
    def auth(func):  # func = index的内存地址
        def wrapper(*args, **kwargs):
            name = input('your username>>:').strip()
            pwd = input('your password>>:').strip()
            if db_type == 'file':
                print('基于文件的验证')
                if name == 'egon' and pwd == '123':
                    print('login success')
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("username or password error")
            elif db_type == 'database':
                print('基于数据库的验证')
                ...
            elif db_type == 'ldap':
                print('基于ldap的验证')
                ...
            else:
                print('不支持该db_type')
        return wrapper
    return auth
# 账号密码的来源是文件
@db(db_type='file')  # @auth  # index=auth(index)  # index=wrapper
# @db(db_type='file')先执行db(db_type='file')得到db函数返回值放在@后==》@auth
# @auth就是下方的函数名=装饰器名称(下方的函数名)==》index=auth(index)==》wrapper(wrapper的内存地址)
# wrapper==》index=wrapper==》index()
def index(x, y):
    print(x, y)
# 账号密码的来源是数据库
@db(db_type='database')  # @auth  # database=auth(database)  # database=wrapper
def database(x, y):
    print(x, y)
# 账号密码的来源是ldap
@db('ldap')  # @auth  # ldap=auth(ldap)  # ldap=wrapper
def ldap(x, y):
    print(x, y)

index(1, 2)
database(1, 2)
ldap(1, 2)


# 有参装饰器模板:
# def 有参装饰器(x, y, z):
#     # db_type = ''
#     def outter(func):
#         def wrapper(*args, **kwargs):
#             if x == '':
#                 res = func(*args, **kwargs)
#                 return res
#         return wrapper
#     return outter
#
# @有参装饰器(1, 2, 3)
# def 被装饰对象():
#     pass
