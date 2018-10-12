# Number 数字类型
# 分类： int 整型  float 浮点型  complex 复数

# 整型：整数 分正负数
# 定义：num1 = 1       =:赋值符号  读法：将1赋值给变量num1
num1 = 100
print(num1)   # 100
print(type(num1))  # <class 'int'>

# 用一个变量给另一个变量赋值,将内存地址赋给变量
num2 = num1
print(num2)  # 100

# 连续给多个变量赋值
num3 = num4 = num5 = 200
print(num3)  # 200
print(num4)  # 200

num6 = 111;num7 = 222; num8 = 333
print(num6)
print(num7)
print(num8)

# 交互式赋值  注：变量的个数与常量的个数一致，不一致可能会有以下错误提示
# ValueError: not enough values to unpack (expected 3, got 2)
# ValueError: too many values to unpack (expected 2)
num9, num10, num11 = 666, 777, 888
print(num9)
print(num10)

a = 120
b = 119
# 交换两个变量的值
c = a    # c = 120
a = b    # a = 119
b = c    # b = 120
print(a)
print(b)

d = 333
e = 444
d, e = e, d  # d,e = 444, 333
print(d)
print(e)


print("*****************************************")
# float 浮点型   小数
f1 = 1.23
print(f1)
print(type(f1))
f2 = f1
f3 = f4 = f5 = 6.98
f6, f7 = 2.4, 6.7
# 在计算机，浮点型的运算会有误差，误差对结论的影响不大
print(f1 + f2)  # 2.46
# 2.1     ---  2.099999999

# complex 复数
# 定义： complex(x,y)    x:代表实数  y：代表虚数部分  x+yj
# 真正使用几率很小，仅作了解
com = complex(2, 3)
print(com)  # (2+3j)





