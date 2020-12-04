# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-10 23:06 
# @Software：PyCharm
# ----------------------------------------------------------------------------
'''
# 分析过程
x = '上'
                            内存
上>----------翻译--------->0101010
上<----------翻译---------<0101010

字符编码表就是一张字符与数字对应关系的表

a-00
b-01
c-10
d-11

ASCII表:
    1.只支持英文字符串
    2.采用8位二进制数对应一个英文字符串

GBK表:
    1.支持英文字符、中文字符
    2.采用8位（8bit = 1Bytes）二进制数对应一个英文字符串
      采用16位（16bit = 2Bytes）二进制数对应一个中文字符串

unicode表:(内存中统一使用Unicode表)
    1.兼容万国字符，与万国字符编码都有对应关系
    2.采用16位二进制数对应一个中文字符串
      个别生僻会采用4Bytes、8Bytes

    unicode表:
                                    内存
        人类的字符-----------Unicode格式的数字----------------
                                    |                        |
                                  硬盘                       |
                                    |                        |
                              GBK格式的二进制        shift-JIS格式的二进制

        ps：老的字符编码都可以转换成Unicode，但是不能通过Unicode互转

utf-8：（全称Unicode Transformation Format，即unicode的转换格式）
    英文->1Bytes
    中文->Bytes



结论：
1.内存固定使用的是Unicode，我们可以改变的是存入硬盘采用格式
    英文、中文-->Unicode-->gbk
    英文、日文-->Unicode-->shift-jis
    万国字符-->Unicode-->utf-8

2.文本文件存取乱码问题
    储存乱码：编码格式应该设置成支持文件内容字符的格式
    读取乱码：文件以什么编码格式存入硬盘，就应该以什么格式读入内存

3.python解释器默认读文件的编码
    python3默认：utf-8
    python2默认：ASCII

    指定文件头修改默认的编码：
    在py文件的首行写：
        # coding:utf-8

4.保证运行python程序前两个阶段不乱码的核心法则：
    指定文件头：# 文件当初存入硬盘时所采用的编码格式

5.python3的str类型默认直接存成Unicode格式，无论如何都不会乱码
  保证python2的str类型不乱码：
            x = u'上'

6.了解：
  python2解释器有两种字符串类型：str、Unicode
    str类型：
        x = '上'  # 字符串值会按照文件头指定的编码格式存入变量值的内存空间
    Unicode类型：
        x = u'上'  # 强制存成Unicode




'''
a = 'sd'
b = 'df'
print(int(a)+int(b))