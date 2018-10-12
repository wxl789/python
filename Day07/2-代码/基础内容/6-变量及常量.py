# 变量：可任意更改的量
# 常量：不可以更改的值

# 变量：程序可以操作的区域(存储的内存地址)，在程序运行期间，值可以更改。
# 每个变量都有自己的内存地址，有自己的数据类型。
# 作用： 将不同的数据类型的值存储到内存中。
# 变量的定义：变量名 = 初始值
# 赋予初始值的原因：确定变量的数据类型。

# Python中的数据类型：Number(数字类型：int 整型，整数   float  浮点型 小数
#   complex 复数 a+bj)  String(字符串类型  str)  Boolean(布尔类型 True False)
# List  Set

age = 12  # 读法：将12赋值给age变量
weight = 56.77
name = "lily"

print(age)
print(weight)
print(name)
# 查看变量类型： type(变量/常量)
print(type(age))  # int
print(type(weight))  # float
print(type(name))  # str

# 查看变量的内存地址  id(变量/常量)
print(id(age))
print(id(weight))

age = 200
name = 300
print(id(age))
print(id(name))
print("-----------------------")
# 变量的使用
a = 30
print(a)  # 30
# python中的变量必须有值
# b
# print(b)  # 55

# python 属于动态型语言：变量的类型不会固定，根据等号后面的类型灵活变化
a = "张三"
print(a)


# 常量
# Python中没有规定常量的关键字，一般想要定义常量，将标识符的所有字母大写。
HEIGHT = 100.99
PI = 3.1415
print(HEIGHT)

# 删除变量  del 变量名
print(PI)
# del 删除的变量不能再继续使用
del PI
# print(PI)
# NameError: name 'PI' is not defined  某个变量未定义  当见到类似的错
# 误时，检查该变量是否在使用之前定义过。
# print(abc)


# 系统中的常量
import math
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
