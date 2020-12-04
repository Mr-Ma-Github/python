# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-18 17:40 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# 控制文件读写内容的模式：
# t：text模式：如果我们指定的文件打开模式为r/w/a，其实默认就是rt/wt/at
#     1.读写都是以str(Unicode)为单位
#     2.只能针对文本文件
#     3.必须指定字符编码。例如：encoding = 'utf-8'
# b: binary模式：读写都是以二进制位单位
#     1.读写都是以bytes为单位的
#     2.可以针对所有文件
#     3.一定不能指定字符编码(encoding参数)

# bytes==》二进制：得到bytes类型的三种方式：
#     1.字符串编码之后的结果
#         字符串.encode('编码格式')  # utf-8、gbk....
#         bytes('333\n', encoding='编码格式')
#     2.b'必须是纯英文字符'
#     3.b模式下打开文件，f.read()读出的内容
# 总结：
# 1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码，所以此时t模式更为方便
# 2、针对非文本文件（如图片、视频、音频等）只能使用b模式

# 错误演示：t模式只能读文本文件
# with open(r'Wildlife.mp4', mode='rt')as f:
#     f.read()  # 硬盘的二进制读入内存--》t模式会将读入内存的数据进行decode解码操作

# with open(r'car.jpg', mode='rb')as f:
#     res = f.read()  # 硬盘的二进制读入内存--》b模式下，不做任何转换，直接读入内存
#     print(res)  # bytes类型==》当成二进制
#     print(type(res))  # <class 'bytes'>

# with open(r'a.txt', mode='rb')as f:
#     res = f.read()  # utf-8的二进制
#     print(res)
#     print(res.decode('utf-8'))

# with open(r'test_write.txt', mode='wb')as f:
#     f.write('你好hello'.encode('utf-8'))

# 拷贝文件工具
# src_file = input('源文件路径>>: ').strip()
# dst_file = input('源文件路径>>: ').strip()
# with open(r"{}".format(src_file), mode='rb') as file, \
#     open(r"{}".format(dst_file), mode='wb') as file2:
#     for line in file:
#         file2.write(line)

# 循环读取文件
# 方式一：while循环：自己控制每次读取的数据量
# with open(r'test_write.txt', mode='rb') as file:
#     while True:
#         res = file.read(10)  # 字节数量
#         # res = file.readline()  # 按行读取
#         if len(res) == 0:
#             break
#         print(len(res))

# 方式二：for循环：以行为单位读取，当一行内容过长时会导致一次性读入内容的数据量过大
# with open(r'test_write.txt', mode='rt',encoding='utf-8') as file:
#     for line in file:
#         print(line)

# with open(r'test_write.txt', mode='rb') as file:
#     for line in file:
#         print(line)
