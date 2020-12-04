# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-12-04 0:01 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# import time
# from functools import wraps
#
# def outter(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#     return wrapper
#
# @outter
# def index(x, y):
#     time.sleep(3)
#     print("index==>>%s, %s" % (x, y))
#
# @outter
# def home(x, y):
#     time.sleep(3)
#     print("home==>>%s, %s" % (x, y))
#
#
# # index = outter(index)
# index(1, 2)

import time
from functools import wraps
def auth(db_type):
    def outter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if db_type == 'file':
                name = input("please input your username==>>:").strip()
                pwd = input("please input your password==>>:").strip()
                if name == 'egon' and pwd =='123':
                    start = time.time()
                    res = func(*args, **kwargs)
                    end = time.time()
                    print(end - start)
                    return res
                else:
                    print("you input username or password is error!")
            elif db_type == 'database':
                pass
        return wrapper
    return outter

outter = auth('file')
@outter  # index = outter(index)
def index(x, y):
    time.sleep(3)
    print("index==>>%s, %s" % (x, y))

@outter
def home(x, y):
    time.sleep(3)
    print("home==>>%s, %s" % (x, y))


# index = outter(index)
index(1, 2)
