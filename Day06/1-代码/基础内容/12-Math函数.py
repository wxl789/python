import math
# 基本数学函数
# 1、绝对值  abs()
print(abs(10))
print(abs(-10))

# 2、比较两个数的大小   (数字1 > 数字2) - (数字1 < 数字2)
# 当数字1小于数字2：返回-1
# 当数字1大于数字2：返回1
# 当数字1等于数字2：返回0
a = 20
b = 10
# a > b  ==> 1
# a < b  ==> 0
res = (a > b) - (a < b)
print(res)

# 3、返回最大值或最小值   max()   min()
print(max(1, 2, 3, 4, 5, 6, 7, 8))  # 8
print(min(2, 3, 1, 4, 6, 3))        # 1

# 4、求幂   pow(x， y)  x的y次幂
print(pow(2, 3))  # 8

# 5、返回浮点数的四舍六入的整数值
# round(x [,n])  x：即将四舍六入的值  n：可选参数，代表保留几位小数
# python3 中，当小数为5时，距离两边的整数大小一致，取偶数。
print(round(3.3))   # 3
print(round(3.6))   # 4
print(round(3.5))   # 4
print(round(2.5))   # 2
print(round(1.5))   # 2

# 当保留n位小数时，距离两边的数大小一致，取奇数。
print(round(2.335, 2))



# 数学函数

# 当写了import math，可以调用math里面所有的内容
print(math.pi)
# 1、向上取整  ceil()
print(math.ceil(1.02))   # 2
# 2、向下取整  floor()
print(math.floor(3.9))  # 3
# 3、返回绝对值  fabs()  返回浮点型
print(math.fabs(-10))   # 10.0
# 4、开方  返回浮点数
print(math.sqrt(9))  # 3.0
# 5、返回整数部分与小数部分，返回的数据都是浮点型，
# 返回的数据格式元组类型
# (小数部分, 整数部分)
print(math.modf(4.33))
tu1 = math.modf(4.33)
print(tu1[1])

# *******************三角函数*************
# math.sin(x)   x为任意数值
# math.cos(x)   x为任意数值
# math.acos(x)   x为-1 至 1 之间的任意数
# math.asin(x)   x为-1 至 1 之间的任意数










