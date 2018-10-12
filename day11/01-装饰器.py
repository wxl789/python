#
# #第一波
def foo():
    print("foo")

# foo#表示函数
# foo()#表示执行foo函数

#第二波：
# foo = lambda x:x + 1
#
# foo() #就近原则


# 简单的装饰器
def func1():
    print("haha")

def outer(func):
    def inner():
        print("----------")
        func()
    return inner

f = outer(func1)
f()


"""
需求：
    初创公司有N个业务部门，1个基础平台部门，基础平台部门负责提供底层的功能：数据库的操作
    业务部门使用基础功能时，只需要调用基础平台提供的功能
"""
#基础平台部门实现的功能
def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

def f4():
    print("f4")
print("-----------------------------------------------------------------")
#业务部门A
f1()
f2()
f3()
f4()
print("------------------ccccccccccccccccccc-------------------------------")
#业务部门B
f1()
f2()
f3()
f4()
print("-------------------bbbbbbbbbbbbbbb----------------------------")
#老宋把工作交给狗蛋，
# 基础平台部门实现的功能,是否有参数  是否有返回值
def f1():
    #验证1
    #验证2
    print("f1")

def f2():
    # 验证1
    # 验证2
    print("f2")


def f3():
    # 验证1
    # 验证2
    print("f3")

def f4():
    # 验证1
    # 验证2
    print("f4")
print("------------------------aaaaa----------------------------")
#业务部门A
f1()
f2()
f3()
f4()

#业务部门B
f1()
f2()
f3()
f4()

print("---------------dddddddddddddddddddddddddddddd--------------------")
#小王

def check_login():
    #验证1
    #验证2
    pass

def f1():
    check_login()
    print("f1")
def f2():
    check_login()
    print("f1")
def f3():
    check_login()
    print("f1")

def f4():
    check_login()
    print("f1")


#封闭：已实现的功能模块
#开放：对扩展开放

def w1(func):#func--->f1
    def inner():
        #验证
        #验证
        func()
    return inner
print("------------------ffffffffffffffffffffffffffffffffff----------")
#装饰器，@
@w1#语法糖
def f1():
    print("f1")
@w1
def f2():
    print("f2")
@w1
def f3():
    print("f3")
@w1
def f4():
    print("f4")


f1()
"""
新的f1 = def inner():
            #验证1
            #验证2
        return inner    




"""















