
"""
如果有一个对象，需要修改其属性
直接修改：对象名.属性名 = 数据
间接修改：对像名.方法名（）

将属性定义为私有，属性前面加上__
"""
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def getName(self):
        return self.__age

    def setName(self,newAge):
        self.__age = newAge

p = People("老王",35)
print(p.name)
# print(p.age)
print(p.getName())

p.name = "老宋"
print(p.name)

p.setName(45)
print(p.getName())











