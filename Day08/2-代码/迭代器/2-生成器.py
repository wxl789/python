'''
生成器：
generator生成器：使用yield关键字的函数被称为生成器函数。

使用yield的函数与普通函数的区别：
1、使用yield的函数返回一个生成器对象。
2、普通函数的返回值属于程序员自己设置。

yield:将一个函数拆分成多个模块，模块与模块之间为连续的。
yield可以间接控制进程或线程。

生成器可以认为是一个迭代器，使用方式与迭代器一致。
'''
# 普通函数的返回值默认为NoneType类型
def func1():
    print(1)
    print(2)
    print(3)
# print(type(func1))  # function
# print(type(func1()))   # NoneType
print("********************************************************")
# yield 关键字
def func2():
    print(1)
    yield 100
    print(2)
    yield 200
    print(3)
    yield 300
print(type(func2))   # function
print(type(func2()))  # generator
a = func2()
print(next(a))
print(next(a))
# [(print(1)-100),(print(2)-200),(print(3)-300)]

num = func2()  # generator
# next(num)
# next(num)
# next(num)
# next(num)  # StopIteration
print(next(num))   # next:会依次返回yield后面的数据





