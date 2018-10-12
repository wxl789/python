# 定义一个函数，该函数有两个参数，返回值为两个参数的和

# 函数的定义
def getSum(num1,num2):
    # print(num1+num2)
    # return : 一般用于函数的结束，将信息返回给函数的调用者
    # return 表达式：将表达式作为函数的返回值
    # 表达式可以是任意类型的数据或计算式

    # return:将表达式返回给函数的调用者,表达式为什么数据类型，目前函数就
    # 可以认为是什么类型，函数的调用者就是什么类型。
    return num1 + num2
    # return "abcdef"
# 函数的调用
# getSum(1,2)
res = getSum(1,2)
print(res)
print(type(res))

getSum(3,4)  # 函数的调用者为整个文件
res = getSum(9,8)  # 可以认为函数的调用者为res


# 定义
def printText():
    print("123呵呵456")
    return "abc"
    # 当函数执行到return时，代表该函数执行结束，return后面的代码不再执行
    # return的作用：1、可以用作函数的返回值
    #               2、可以用来终止函数
    # print("鹅鹅鹅")

# 调用
printText()
res2 = printText()
print(res2)


def panduanNum(num1):
    if num1 == 1:
        print("正确")
        return 0
    if num1>0:
        print("数字大了")
    else:
        print("数字太小了")
panduanNum(1)
panduanNum(0)

# 默认返回值  None
def getNum():
    print("我爱工作")
    # return None:当我们的函数体内部的的最后一行为return None时，
    # 可以省略该行语句，系统在执行函数时，会默认自动添加这行代码
    return None

# getNum()
print(getNum())




