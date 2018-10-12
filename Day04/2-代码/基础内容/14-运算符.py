# 1、比较运算符  后期一般用于条件判断  返回True或False
# 比较运算符两边的数据类型要求一致
# ==   等于       比较两个值是否相等
# !=   不等于
# >    大于
# <    小于
# >=   大于等于
# <=   小于等于
a = 100
b = 200
print(a == b)  # F
print(a != b)  # T
print(a > b)  # F
print(a < b)  # T
print(a >= b)  # F
print(a <= b)  # T

# print(1 > "1")
# typeError: '>' not supported between instances of 'int' and 'str'
# 符号两边的数据类型有问题
print("acb" < "abcd")

# 2、逻辑运算符
# 返回boolean的值，用于条件判断
# x,y 为可以得出boolean值的表达式，或者x，y本身是可以转为boolean的值
# and  逻辑与   x and y   x，y都为True时，整体结论才为True
# or   逻辑或   x or y    x，y都为False时，整体结论才为False
# not  逻辑非   not(x)   将x的值取反

num1 = 200
num2 = 220
num3 = 300
print((num1 < num2) and (num2 > num3))  # F
print((num1 < num2) or (num2 > num3))   # T
print(not (num1 < num2))                # F

# 3、身份运算符
# is      ： 判断两个对象的内存地址是否一致，一致返回True
# is not  ： 判断两个对象的内存地址是否一致，一致返回False
# is:判断内存地址是否相等    ==:判断值是否相等
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)  # F
print(a == b)  # T
print(a is not b)  # T


# 4、范围运算符
# in   : 某个变量在范围内，返回True
# not in : 某个变量不在范围内，返回True
print("**********************************")
list1 = [1, 2, 4, 7, 9]
print(3 in list1)  # F
print(3 not in list1)  # T


