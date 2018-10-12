# 定义一个无参无返回值的函数
# 函数在声明时，但未调用是不执行的

# 函数名称命名：不要使用关键字，不要使用系统已经使用过的名称

# 函数的调用
# 函数的定义之前调用会报错
# myPrint()  # NameError: name 'myPrint' is not defined

# 定义一个打印部分文字的函数
def myPrint():
    print("愤青")
    print("十几万")
    print("中国")


# 函数的调用
# 函数可以调用多次，每次调用函数都会执行该函数中的所有内容。
myPrint()
myPrint()
myPrint()

# 见到 ...() ,代表执行了一个函数
# print()


# 输出1-10
def printNum():
    for i in range(1,11):
        print(i)
    print("函数结束")
# 输出5次
printNum()
printNum()
# printNum()
# printNum()
# printNum()

