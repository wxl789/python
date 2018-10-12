"""
使用type函数创建带有方法的类:
type(name,bases,dict)

只需要定义一个恰当签名的函数并将其作为属性赋值

实例方法
类方法
静态方法
"""

People = type("People",(),{"name":"zhangsan"})
"""
class People:
    name = "zhangsan"
"""
print(People)
print(People.name)

p = People()
print(p)
print(p.name)

# class child(People):
#     pass

child = type("child",(People,),{})
print(child)

print(child.name)
#实现实例方法
def getName(self):
    print(self.name)

child = type("child",(People,),{"getName":getName})

print(hasattr(child,"name"))
#创建子类的对象
ch = child()
#通过子类对象调用子类中的实例方法
print(ch.getName())


# #静态方法
@staticmethod
def demo():
    print("static method")


child = type("child",(People,),{"getName":getName,"demo":demo})

ch1 = child()
print(ch1.demo())

# #类方法
@classmethod
def getAge(cls):

    print(cls.name)

child = type("child",(People,),{"getName":getName,"demo":demo,"getAge":getAge})

ch2 = child()
print(ch2.getAge())


#思考：type > object---->type("object")

"""
元类：
    就是用来创建类的事物，---》类的类
    你创建类的作用---》创建实例对象
    类----》对象
    

"""



