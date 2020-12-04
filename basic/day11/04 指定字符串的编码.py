# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-16 22:02 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
控制文件读写内容的模式：t和b（强调：t和b不能单独使用，必须跟r/w/a联用）
    t 文本（默认的模式）：
        1.读写都是以str(Unicode)为单位
        2.文本文件
        3.必须指定encoding='utf-8'
'''
# 没有指定encoding参数操作系统会使用自己默认的编码
# linux系统默认utf-8
# windows系统默认gbk
with open("a.txt", mode='rt', encoding='utf-8') as file:  # 不需要写file.close(), with会自动关闭
    res = file.read()  # t模式会将硬盘中的二进制，读出来解码成Unicode
    print(res, type(res))

# 硬盘：test.txt内容-->>utf-8格式的二进制
# 内存：utf-8格式的二进制----t(unicode)----gbk（未指定windows默认使用gbk，ios默认是utf-8）