# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2020-11-02 23:14 
# @Software：PyCharm
# ----------------------------------------------------------------------------
# day04：（*****）
# 1.垃圾回收机制详解(****)
# 定义:垃圾回收机制(简称GC)是python解释器自带的一种机制,专门用来回收不可用的变量值所占用的内存空间
# 垃圾回收机制原理分析:
# ​ Python的GC模块主要运用了"引用计数"(reference counting)来跟踪和回收垃圾。在引用计数的基础上，还
# 可以通过"标记-清除"(mark and sweep)解决容器对象可能产生的循环引用的问题，并且通过“分代回收”
# (generation collection)以空间换取时间的方式来进一步提高垃圾回收的效率

# 栈区堆区：
# 栈区：存放的是变量名与内存地址的对应关系，所以可以简单理解为：变量名存内存地址
# 堆区：存放的是变量值

# 强调：只站在变量名的角度去谈一件事情
# 变量名的赋值(x=y)，还有变量名的传参(print(x)),传递的都是栈区的数据，而栈区的数据是量名
# 与内存地址的对应关系 或者说是对值的引用


# 引用计数:
# 引用计数就是：变量值被变量名关联的次数
# 如：age=18
# 变量值18被关联了一个变量名age，称之为引用计数为1
# 引用计数增加：
# age=18 （此时，变量值18的引用计数为1）
# m=age （把age的内存地址给了m，此时，m,age都关联了18，所以变量值18的引用计数为2）
# 引用计数减少：
# age=10（名字age先与值18解除关联，再与3建立了关联，变量值18的引用计数为1）
# del m（del的意思是解除变量名x与变量值18的关联关系，此时，变量18的引用计数为0）
# ps：值18的引用计数一旦变为0，其占用的内存地址就应该被解释器的垃圾回收机制回收

# 直接引用和间接引用：
# 直接引用指的是从栈区出发直接引用到的内存地址
# 间接引用指的是从栈区出发引用到堆区后，再通过进一步引用才能到达的内存地址
# x = 10  # 直接引用
# print(id(x))
# l = ['a', 'b', x]  # 间接引用
# print(id(l[2]))
# d = {'m': x}  # 间接引用

# ps：引用计数机制存在着一个致命的弱点，即循环引用（也称交叉引用）

# 标记清除:
# 容器对象（比如：list，set，dict，class，instance）都可以包含对其他对象的引用，所以都可能产生循环
# 引用。而“标记-清除”计数就是为了解决循环引用的问题。
# ​标记/清除算法的做法是当应用程序可用的内存空间被耗尽的时，就会停止整个程序，然后进行两项工作，第一
# 项则是标记，第二项则是清除
# 循环引用==》导致内存泄漏
list1 = [111, ]
list2 = [222, ]

list1.append(list2)  # list1 = [值111的内存地址，l2列表的内存地址]
list2.append(list1)  # list2 = [值222的内存地址，l1列表的内存地址]
#
print(id(list1[1]))
print(id(list2))
#
# print(id(list2[1]))
# print(id(list1))

# 分代回收
# 基于引用计数的回收机制，每次回收内存，都需要把所有对象的引用计数都遍历一遍，这是非常消耗时间的，
# 于是引入了分代回收来提高回收效率，分代回收采用的是用“空间换时间”的策略
# 分代：
# 分代回收的核心思想是：在历经多次扫描的情况下，都没有被回收的变量，gc机制就会认为，该变量是常用变量，
# gc对其扫描的频率会降低，具体实现原理如下：
# 分代指的是根据存活时间来为变量划分不同等级（也就是不同的代）新定义的变量，放到新生代这个等级中，
# 假设每隔1分钟扫描新生代一次，如果发现变量依然被引用，那么该对象的权重（权重本质就是个整数）加一，
# 当变量的权重大于某个设定得值（假设为3），会将它移动到更高一级的青春代，青春代的gc扫描的频率低于
# 新生代（扫描时间间隔更长），假设5分钟扫描青春代一次，这样每次gc需要扫描的变量的总个数就变少了，
# 节省了扫描的总时间，接下来，青春代中的对象，也会以同样的方式被移动到老年代中。也就是等级（代）越高，
# 被垃圾回收机制扫描的频率越低
# 回收：
# 回收依然是使用引用计数作为回收的依据