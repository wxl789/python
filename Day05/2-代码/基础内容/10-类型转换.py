# 数据类型转换
# int -> float  float->int int->str  str->int  float->str str-float
# 语法格式： 转换的类型(即将转换的对象)

# 1、int->float
int1 = 10
print(int1)
print(type(int1))  # int

f1 = float(int1)
print(f1)
print(type(f1))  # float

# 2、float->int
# 在数据类型转换中，不存在四舍五入，只保留整数
f2 = 2.99
int2 = int(f2)
print(int2)  # 2

# 3、str->int  字符串转为整型
# 当字符串中只有数字时，转换成功
str1 = "123"
int3 = int(str1)
print(int3)
# 当 + 或 -作为符号位时，可以转换成功， + 或 - 代表正负号
print(int("+1234"))
print(int("-1234"))

# 当字符串中有非数字的其他任意字符时，转换失败，报错
# print(int("1.99"))
# print(int("abc"))
# print(int("123abc"))
# print(int("韩"))
# print(int("1+2"))


# 4、str->float
# 字符串中的第一个 . 是有意义的，如果包含其他非数字以外的字符，转换失败
print(float("12"))  # 12.0
print(float("12.3"))  # 12.3
# print(float("12.34.56")) # 失败
# print(float("12.3abc"))  # 失败

# 5、int -> str  float -> str
int4 = 200
print(type(int4))  # int
str4 = str(int4)
print(str4)
print(type(str4))  # str

print(str(1.2222))

# input 获取到的数据为字符串类型
a = input("请输入数字：")
print(a)
print(type(a))











