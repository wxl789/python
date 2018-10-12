from time import ctime,sleep
"""
无参的函数
被装饰的函数有参数
"""
def timefun(func):#func--->foo
    def wrappedFunc(a,b):
        print("%s called at %s"%(func.__name__,ctime()))
        print(a,b)
        func(a,b)
    return wrappedFunc

@timefun
def foo(a,b):
    print(a + b)
foo(3,5)#foo==wrappedFunc
sleep(2)
foo(2,4)


"""
*args--->元祖
**kwargs--->字典
被装饰的函数有不定长参数
"""
def timefun(func):#func--->foo
    def wrappedFunc(*args,**kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        func(*args,**kwargs)
    return wrappedFunc

@timefun
def foo(a,b,c):
    print(a + b + c)
foo(3,5,7)#foo==wrappedFunc
sleep(2)
foo(2,4,9)







"""
装饰器中的return
"""
def timefun(func):#func--->foo
    def wrappedFunc():
        print("%s called at %s"%(func.__name__,ctime()))
        return func()
    return wrappedFunc

@timefun
def foo():
    print("haha")
    return "haha"
foo()#foo==wrappedFunc
sleep(2)
foo()
print(foo())

