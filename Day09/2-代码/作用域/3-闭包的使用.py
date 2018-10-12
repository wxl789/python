'''
什么是闭包：就是一个返回函数的函数。
'''
# 优点：1、避免全局变量污染局部环境。
#       2、避免局部变量污染全局环境。
#       3、在全局范围内间接使用或修改局部变量。

# 变量num 初始值为100   有一个函数，第一次运行：num=101  第二次运行
# num=102
num = 100
def countOne():
    global num
    num += 1
countOne()
print(num)
countOne()
print(num)

def count():
    num1 = 100
    num1 += 1
    print(num1)
count()
count()
print("********************************************************")

# 闭包实现局部变量累加更改
def closer():
    a = 200  # 局部变量
    def inner():
        nonlocal a
        a += 1
        print(a)  # 201
    return inner

func1 = closer()  # func1 == inner
func1()   # 201
func1()   # 202
func1()   # 203

closer()()  # 201


# 在函数外部函数内部的局部变量
def myPrint():
    b = 300   # 局部变量
    return b   # 通过返回值的方式让全局范围间接使用局部变量

print(myPrint())
print("********************************************************")
def closerFunc():
    c = 400
    def innerFunc():
        # nonlocal c
        # c += 1
        # return c
        name = "lily"
        return name  # 内部函数可以将闭包范围的变量
                     # 返回，也可以将自己局部的变量返回
    return innerFunc
func4 = closerFunc()
num = func4()
print(num)  # 401
print(func4())  # 402












