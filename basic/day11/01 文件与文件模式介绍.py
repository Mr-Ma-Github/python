# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-12 23:05 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
1.什么是文件？
    文件是操作系统提供给用户/应用程序操作硬盘的一种虚拟的概念/接口
        用户/应用程序
        操作系统-----------------文件
        计算机硬件---------------硬盘
2.为何要用文件？
    用户/应用程序可以通过文件将数据永久保存到硬盘中，即操作文件就是操作硬盘
    用户/应用程序直接操作的是文件，对文件进行的所有操作，都是在向操作系统发送系统调用，
    然后再由操作系统将其转换成具体的硬盘操作

3.如何使用文件：open()
    控制文件读写内容的模式：t和b（强调：t和b不能单独使用，必须跟r/w/a联用）
        t 文本（默认的模式）：
            1.读写都是以str(Unicode)为单位
            2.文本文件
            3.必须指定字符编码。例如：encoding='utf-8'
        b 二进制/Bytes

    控制文件读写操作的模式：
        r 只读模式
        w 只写模式
        a 只追加模式
        +：r+、w+、a+




'''