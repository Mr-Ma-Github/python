# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-12-02 23:14 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 偷梁换柱：即 将原函数名指向的内存地址换成wrapper(闭包函数)函数的内存地址
#         所以应该将wrapper做的跟原函数一样才行
from functools import wraps

def outter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        res = func(*args, **kwargs)
        return res
    # 将原函数的属性赋值给wrapper函数
    # 函数wrapper.__name__ = 原函数.__name__
    # 函数wrapper.__name__ = 原函数.__name__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@outter
def index():
    """这个是主页功能"""
    print("from index")

# index()
# print(index)  # index装饰前后指向的内存地址是不一致的：
#               # 装饰前：<function index at 0x00553930>
#               # 装饰后：<function outter.<locals>.wrapper at 0x006337C8>
#
# print(index.__name__)  # index装饰前后的函数名也是不一致的：
#                        # 装饰前：这个是主页功能
#                        # 装饰后：wrapper

# print(help(index))   # help(函数名)：查看函数的注释信息。index装饰前后的注释信息也是不一致的：
# print(index.__doc__)
#                        # 装饰前：index
#                        # 装饰后：None

# 解决方法：将原函数的属性赋值给wrapper函数
# 函数wrapper.__name__ = 原函数.__name__
# 函数wrapper.__name__ = 原函数.__name__

# 函数的属性有很多，手写太繁琐：
# from functools import wraps
# @wraps(原函数名)  # @wraps(func)

print(index)
print(index.__name__)
print(index.__doc__)  # print(help(index))

