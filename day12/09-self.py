
#定义一个类
class Animal:
    def __init__(self,name):
        self.name = name

    def printName(self):
        print("名字为：%s"%self.name)

#定义函数
def myPrint(animal):
    animal.printName()
dog1 = Animal("xixi")
myPrint(dog1)
dog2 = Animal("beibei")
myPrint(dog2)

"""
所谓self,可以直接理解为对象自己
某个对象调用方法时，python内部的解释器会把这个对象作为
第一个参数传递给self
"""



