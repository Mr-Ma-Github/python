# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-18 23:42 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 主动控制文件内指针移动
# 大前提:文件内指针的移动都是Bytes为单位的,唯一例外的是t模式下的read(n),n以字符为单位
# with open('test_write.txt', mode='rt', encoding='utf-8') as f:
#     data = f.read(4)  # 读取4个字符
#     print(data)
#     f.seek  # 移动是以字节为单位
#
# with open('test_write.txt', mode='rb') as f:
#     data = f.read(6)  # 读取6个Bytes
#     print(data)

# 之前文件内指针的移动都是由读/写操作而被动触发的，若想读取文件某一特定位置的数据，
# 则需要用f.seek方法主动控制文件内指针的移动，详细用法如下：
# f.seek(指针移动的字节数,模式控制):
# 模式控制:
    # 0: 默认的模式,该模式代表指针移动的字节数是以文件开头为参照的
    # 1: 该模式代表指针移动的字节数是以当前所在的位置为参照的
    # 2: 该模式代表指针移动的字节数是以文件末尾的位置为参照的
    # 强调:只有0模式可以在t或者b模式使用,而1跟2模式只能在b模式下用

# f.tell()  # 获取文件指针当前位置

# 示范：
# with open('test_write.txt', mode='rt', encoding='utf-8') as f:
#     f.seek(4, 0)  # 移动4个字符
#     print(f.tell())

# with open('test_write.txt', mode='rb') as f:  # abc你好
#     f.seek(3, 0)  # 移动3个字节
#     # f.seek(4, 0)  # 移动4个字节，但是下面解码就会报错(utf-8编码一个中文等于三个字节，单独第4个字节是不完整的)
#     print(f.tell())
#     print(f.read().decode('utf-8'))

# with open('test_write.txt', mode='rb') as f:  # abc你好
#     f.seek(3, 1)  # 移动3个字节
#     f.seek(3, 1)  # 移动3个字节：1模式指针移动的字节数是以当前所在的位置为参照的3+3
#     print(f.tell())
#     print(f.read().decode('utf-8'))

with open('test_write.txt', mode='rb') as f:  # abc你好
    f.seek(-3, 2)  # 移动3个字节：1模式指针移动的字节数是以末尾为参照的-3
    print(f.tell())
    print(f.read().decode('utf-8'))