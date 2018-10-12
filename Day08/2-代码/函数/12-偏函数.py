# 偏函数
# int()  int函数可以将字符串类型的数据转为整型,默认为十进制转换，可以
# 设置进制格式
# base=10  2  8  16
print(int("1011"))   # 10
print(int("10", base=2))   # 2

# 有一个函数，将字符串以二进制格式进行转换
# 仿写偏函数的功能
def myInt2(strData):
    # 返回的函数将某些参数固定发
    return int(strData, base=2)

# myInt2("11") == int("11", base=2)
print(myInt2("11"))
print(myInt2("110"))
print("------------------------------------------")

# 系统的偏函数
# functools 模块
import functools

# 使用 functools.partial  创建偏函数，就不用我们自己写def函数了。
# 偏函数：将函数的某个参数直接固定一个值，返回一个新的函数。

# 语法格式：
# functools.partial(即将使用或更改的原函数名称,原函数各个参数的值)
# 第一个参数：原函数变得函数名称，不能省略
# 从第二个参数开始：为原函数固定的参数的值，如果格式为关键字的
# 格式，直接给该参数赋值；如果不是关键字格式,从左向右依次给原函数的形参
# 赋值，如果偏函数中的参数个数少于原函数的形参格式，在调用偏函数时，函数的
# 参数依次赋值给原函数没有值的形参(原函数的形参对应的实参个数要求一致)

int2 = functools.partial(int, base=2)
print(int2("111"))

# 定义一个函数，返回一个商
def newDiv(num1,num2):
    return num2 / num1
print(newDiv(2, 10))
print(newDiv(3, 9.0))
print("------------------------------------------")
div2 = functools.partial(newDiv,2)
print(div2(4))

div3 = functools.partial(newDiv, 2, 12)
print(div3())

div4 = functools.partial(newDiv, num2=10)
print(div4(num1=2))

div5 = functools.partial(newDiv, num1=2)
print(div5(num2=90))



