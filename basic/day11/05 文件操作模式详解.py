# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-16 23:31 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 以t模式为基础进行内存操作
# 1.r：只读模式（默认），当文件不存在会报错，存在时文件光标调到最开始位置
# with open("test3.txt", mode='rt', encoding='utf-8') as file:
#     res = file.read()  # 把所有内容从硬盘读入内存
#     print(res)

# input_name = input('your username：').strip()
# input_pwd = input('your password：').strip()
# # 验证：
# with open("user.txt.txt", mode='rt', encoding='utf-8') as file:
#     for line in file:  # 默认按行读取
#         # print(line, end='')  # egon:123\nlili:456\njack:789\ntom:444
#         username, password = line.strip('\n').split(':')
#         # print(username, password)
#         if input_name == username and input_pwd == password:
#             print('登录成功')
#             break
#     else:  # else包含的代码会在for循环结束后，并且for循环是在没有被break打断的情况下正常结束，才会运行
#         print('账号或密码输入有误')

# 2.w：只写模式:当文件不存在会创建空文件，当文件存在时会清空文件。光标位于最开始位置
# with open("test3.txt", mode='wt', encoding='utf-8') as file:
#     # res = file.read()  # 报错--只写模式下不可读
#     file.write('你好\n')
#     file.write('我好\n')
#     file.write('当文件不存在会创建空文件\n')
# with open("test3.txt", mode='rt', encoding='utf-8') as file:
#     res = file.read()  # 把所有内容从硬盘读入内存
#     print(res)
# 强调：
# 1：在以w模式打开文件没有关闭的情况下，连续写入，后写的内容一定跟在前写内容的后面
# 2 如果重新以w模式打开文件，则会清空文件内容

# 案例：w模式用来创建全新的文件
# 文本文件的copy工具：
# src_file = input('源文件路径>>: ').strip()
# dst_file = input('源文件路径>>: ').strip()
# with open(r"{}".format(src_file), mode='rt', encoding='utf-8') as file, \
#     open(r"{}".format(dst_file), mode='wt', encoding='utf-8') as file2:
# #     res = file.read()  # 内存占用过大
# #     file2.write(res)
#     for line in file:
#         file2.write(line)

# 3.a：只追加写：在文件不存在时会创建空文档,文件存在会将文件指针直接移动到文件末尾
# with open('test3.txt', mode='a', encoding='utf-8') as f:
#     # f.read()  # 报错--追加写模式下不可读
#     f.write('44444\n')
#     f.write('55555\n')
#强调 w 模式与a模式的异同：
# 1 相同点：在打开的文件不关闭的情况下，连续的写入，新写的内容总会跟在前写的内容之后
# 2 不同点：以a模式重新打开文件，不会清空原文件内容，会将文件指针直接移动到文件末尾，
#   新写的内容永远写在最后

# 案例：a模式用来在原有的文件内容的基础之上写入新的内容，比如记录日志、注册
# 注册功能：
# name = input('username>>>: ').strip()
# pwd = input('password>>>: ').strip()
# with open('db.txt', mode='a', encoding='utf-8') as f:
#     f.write('%s:%s\n' % (name, pwd))

# +:不能单独使用，必须配合r、w、a
# r+
# with open('a.txt', mode='r+t', encoding='utf-8') as f:
    # print(f.read())
    # f.write('中国')  # 直接写从开头写--覆盖，先读后写从末尾写
# w+
# with open('a.txt', mode='w+t', encoding='utf-8') as f:
#     f.write('中国\n')
#     f.write('祝福\n')
#     f.write('你\n')
#     print('=====>>', f.read())
# a+
# with open('a.txt', mode='a+t', encoding='utf-8') as f:
#     f.write('中国\n')
#     f.write('祝福\n')
#     f.write('你\n')
#     print('=====>>', f.read())
