
class People(object):
    name = "tom"#公有的类属性
    __age = 12#私有类属性

    # def __init__(self,name):
    #     self.name = name

p = People()
print(p.name)
# print(p.__age)

print(People.name)
# print(People.__age)

"""
注意：
   不能在类的外面通过实例对象和类对象访问私有的类属性
"""