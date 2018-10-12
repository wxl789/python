'''
__init__:构造方法   创建时调用
__del__:析构方法    对象销毁时调用
'''

class Person():
    def __init__(self,name):
        self.name = name
        print(self.name+"出生")
    # 析构方法
    def __del__(self):
        print(self.name + "销毁")

p1 = Person("lily1")
p2 = Person("lily2")
p3 = Person("lily3")
# 当我们不执行del 销毁时，程序运行结束时会自动销毁创建的对象。

# 当del 删除对象时，会自动调用析构方法
del p3
del p1


# 在函数内部定义的变量，当函数执行结束后会自动销毁，将变对象的
# 创建及使用放到函数中，会相对减少内存的浪费。
def func1():
    p4 = Person("lily4")
    print(p4.name)
func1()