# python2.X与python3.X的区别

# 一、性能：p3比p2的效率要低，但p3处于开发阶段，有优化空间，后期会在
#          效率上赶上p2.

# 二、编码：p3默认使用utf-8的编码，直接支持汉字。
#           p2默认不支持汉字，想要程序支持汉字，代码文件的第一行必须写
# -*- coding: utf-8 -*-
# coding=utf-8
# (注：就是注释格式)

# 三、代码语法
# 1、去除了 <>，改为 !=
# 不等于：p2: <>   p3: !=

# 2、p3中加入了 as with  True  False  None  nonlocal等关键字

# 3、/ 除号
# p2： /  整除   p3： / 返回浮点数    // 整除

# 4、输出语句
'''
p2              p3
print a         print(a)
print a,b,c     print(a,b,c)
print a,        print(a,end="")
print           print()
'''

# 5、输入语句
# p2:raw_input       p3:input()


# 6、八进制表示
# p2:0222     p3:0o222

# 7、运算符
# p2: 2 > "3"    false   允许运算符两边的类型不一致
# p3: 2 > "3"     返回类型错误   运算符两边的类型必须一致

# 四、面向对象
# p3中新增了一个抽象类

# 五、数据类型
# 1、p2：有 long  长整型
#    p3: 没有long，只保留一个int， int的效果与long一致

# 2、p3新增了一个字节类型  bytes
str1 = "你好"
print(str1.encode("gbk"))
# 定义字节类型数据
str2 = b"abcd"
print(str2)
print(type(str2))

# 六、range
# p2: xrange(4) ==> [0,1,2,3]
# p3: range(4) ==> [0,1,2,3]

# 七、文件
# p2： 有file文件类型
# p3: 删除了file类型
# p2: 打开文件：创建file类型的对象： file(pathname)  open(file)
# p3：打开文件： open(pathname)

# 八、异常处理
'''
p2:
try:
    pass
except BaseException, e:
    pass
'''
'''
p3:
try:
    pass
except BaseException as e:
    pass
'''

# 九、url处理



















