# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-18 23:00 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 1.读操作
# f.read()  # 读取所有内容,执行完该操作后，文件指针会移动到文件末尾
# f.readline()  # 读取一行内容,光标移动到第二行首部
# f.readlines()  # 读取每一行内容,存放于列表中
# with open(r'test_write.txt', mode='rt', encoding='utf-8') as f:
#     # print(f.read())
#     print(f.readline())  # 一次读一行
#     print(f.readline())
#     print(f.readlines())
# 强调：
# f.read()与f.readlines()都是将内容一次性读入内存  ，如果内容过大会导致内存溢出，若还想将内容全读入内存，
# 则必须分多次读入，有两种实现方式：
# 方式一
# with open('test_wtite.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line)  # 同一时刻只读入一行内容到内存中

# 方式二
# with open('1.mp4', mode='rb') as f:
#     while True:
#         data = f.read(1024)  # 同一时刻只读入1024个Bytes到内存中
#         data = f.readline()  # 同一时刻只读入一行数据到内存中
#         if len(data) == 0:
#             break
#         print(data)

# 2.写操作
# f.write('1111\n222\n')  # 针对文本模式的写,需要自己写换行符
# f.write('1111\n222\n'.encode('utf-8'))  # 针对b模式的写,需要自己写换行符

# f.writelines(['333\n', '444\n'])  # 文件模式
# with open(r'test_write.txt', mode='wt') as f:
#     l = ['12334aaa\n', 'dsdf2323\n', 'dfsc3423\n']
#     # for line in l:
#     #     f.write(line)
#     f.writelines(l)

# 字符串.encode('utf-8')等同于bytes('333\n', encoding='utf-8')
# f.writelines([bytes('333\n', encoding='utf-8'), '444\n'.encode('utf-8')])  # b模式

# wb模式下，如果写入的是纯英文字符，可以直接加b前缀得到bytes类型---》来省略encode
# with open(r'test_write.txt', mode='wb') as f:
#     # l = ['12334aaa'.encode('utf-8'), 'dsdf2323'.encode('utf-8'), 'dfsc3423'.encode('utf-8')]
#     l = [b'12334aaa', b'dsdf2323', b'dfsc3423']
#     f.writelines(l)

# 3.flush:立刻将文件内容从内存存到硬盘
# with open(r'test_write.txt', mode='wt', encoding='utf-8') as f:
#     f.write('哈哈哈哈哈')
#     f.flush()

# 4.了解
# with open(r'test_write.txt', mode='wt', encoding='utf-8') as f:
#     print(f.readable())  # 判断文件是否是可读的
#     print(f.writable())  # 判断文件是否是可写的
#     print(f.encoding)  # 查询编码格式
#     print(f.name)  # 查询文件名称
# print(f.closed)  # 判断文件是否是关闭状态