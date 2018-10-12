# 不定长参数
# 概念：能够在函数内部处理比形参个数多的实参
def sum1(a,b):
    print(a + b)
def sum2(a,b,c):
    print(a + b + c)

# 加了 (*) 的变量，可以存放多个实参。
# 加了 * 的形参，数据类型为元组类型，如果调用时未传入传入参数，默认
# 为一个空元组，如果传入了实参，将传入的实参按传入顺序依次放到元组中。
def fun1(*args):
    print(args)
fun1()
fun1(1)
fun1(1,2,3)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# 计算传入的实参的和
def fun2(*args):
    res = 0
    for i in args:
        res += i
    print(res)
fun2(1)
fun2(1,2)

# 有普通形参及不定长参数
def fun3(num1,num2, *args):
    print(num1)
    print(num2)
    print(args)
# fun3(1) # error
fun3(1,2)
fun3(2,3,4)
fun3(4,5,6,7,8,9)
# 不能使用关键字参数
# TypeError: fun3() got multiple values for argument 'num1'
# fun3(7,8,9,num1=1,num2=8)
# fun3(num1=1,num2=2,7,8,9)  # 语法错误

# 当不定长参数在前面时，函数调用需要使用关键字格式
def fun4(*args,num1):
    print(num1)
    print(args)
print("-------------------------------")
fun4(1,2,3,4,num1=200)











