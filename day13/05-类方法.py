

class People(object):
    address = "杭州"

    @classmethod
    def getAddress(cls):#cls类对象
        return cls.address

    @classmethod
    def setAddress(cls,address):
        cls.address = address




    def ss(self):
        pass
#创建实例对象
p = People()
print(p.getAddress())#可以通过实例对象引用
print(People.getAddress())#可以通过类对象引用

p.setAddress("北京")
print(p.getAddress())#可以通过实例对象引用
print(People.getAddress())#可以通过类对象引用
"""
类方法的用途，可以对类属性进行修改
"""
