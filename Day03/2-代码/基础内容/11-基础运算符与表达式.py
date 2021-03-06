# 什么是表达式?
# 由变量、常量及运算符组成的式子称为表达式。

# 一条语句：见到一个分号代表一条语句，如果一行上只有一条语句，分号可
# 以省略，如果一行上由多条语句，不同语句之间用分号隔开。
# 一行语句：一行上可以写多条语句，不同语句之间用分号隔开。
# 建议：一行上尽量只写一条语句

a = 100; b = 200

# 运算符

# 1、数学运算符
# 功能：进行数学运算
#  +  加号  两个对象相加
#  -  减号  两个对象相减
#  *  乘号  两个对象相乘
#  /  除号  两个对象相除   返回浮点数
#  %  取余  返回余数
#  **   x ** y  x的y次幂
#  //  整除 地板除  只保留商整数，如果返回负数，向负无穷靠近
num1 = 10
num2 = 2
print(num1 + num2)  # 12
print(num1 - num2)  # 8
print(2 - 5)    # -3
print(num1 * num2)  # 20
print(num1 / num2)  # 5.0  浮点数
print(num1 % num2)  # 0

print(-2 * 3)  # -6
print(-2 * (-3))  # 6
print(25 / 4)  # 6.25
print(-25 / 4)  # -6.25
print(-25 / (-4))  # 6.25

print(num1 ** num2)  # 100

print(25 // 4)  # 6
print(-25 // 4)  # -7
print(-25 // (-4))  # 6


print(25 % 4)   # 1
print(-25 % 4)   # 3
print(-25 % (-4))  # -1

'''
a // b = c  商
a % b = d   余数
a = b * c + d
d = a - b * c
d = -25 - 4 * (-7)
'''
# 注：非数字以外的数据类型，不支持数学运算符，强行使用，会报错。
str1 = "12"
str2 = "34"
# print(str1 - str2) # 报错

# 2、赋值运算符
# 2.1、基础赋值运算符  =
# 将等号 = 右面的值赋给左边的变量
num3 = 20
num4 = 10 + 20
print(num4)

# 2.2、组合赋值运算符
# +=  -=   *=  /=  %=  //=  **=

# a += b   ==>  a = a + b
# a -= b   ==>  a = a - b
# a *= b   ==>  a = a * b
# a /= b   ==>  a = a / b
# a //= b   ==>  a = a // b
# a %= b   ==>  a = a % b
# a **= b   ==>  a = a ** b

num5 = 3
# num5 += 10
num5 = num5 + 10
print(num5)
