def func1():
    print("123")
def func2():
    print("456")
    # 函数内部可以调用其他函数，但要保证该函数被声明过
    func1()
func2()

# 在函数内部可以声明另一个函数
def func3():
    print("abc")
    def func4():
        print("def")
    func4()
func3()

# 闭包：在函数内部定义一个函数，并且外部函数将内部函数作为返回值，该内部
# 函数叫做闭包函数。
# 什么是闭包：就是一个返回函数的函数。

# 最简单的闭包
def closer():
    def inner():
        print("inner")
    return inner

resFunc = closer()   # resFunc === inner
print(type(resFunc))  # function
resFunc()

# 整合写法
closer()()


def closerFunc():
    def innerFunc():
        print("qaz")
        return "inFunc"
    # 将内部函数的返回值作为外部函数的返回值使用
    return innerFunc()
res = closerFunc()
# res = innerFunc()
print(res)





