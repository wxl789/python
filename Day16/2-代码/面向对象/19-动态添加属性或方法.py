# 使用方法
from types import MethodType

# 动态添加属性或方法
class Person():
    pass
    def run(self):
        print("run")
# 动态添加属性
p1 = Person()
p1.name = "p1"
print(p1.name)

# 动态添加方法
# def eating(self):
#     print(self.name)
#     print("eating")
# p1.eat = eating
# p1.eat(p1)

# MethodType(函数名， 当前类的实例对象)
def eating(self):
    print("eating")
# 把p1传递给eating的第一个形参self
p1.eat = MethodType(eating, p1)
p1.eat()

# 思考：如果需要限制动态添加的属性或方法的个数及名称怎么办？
# 动态添加name和age属性，run方法
# 为了限制动态添加的内容，需要使用__slots__属性。
# _slots__属性可以做到限制动态添加的属性或方法

# __slots__:使用元组方式赋值
# __slots__只对当前类有效，对子类无效。
# __slots__:当子类中定义了__slots__属性，slots的值为当前类的元素
# 及父类中的__slots__的元素的并集。
class A():
    __slots__ = ("name", "age", "run")
class B(A):
    __slots__ = ("sex", )

a1 = A()
a1.name = "AA"
a1.age = 12
print(a1.name)
print(a1.age)
# a1.sex = "男" # 错误，不能添加sex，被__slots__限制
# print(a1.sex)
def run(self):
    print(self.name + "run")
a1.run = MethodType(run, a1)
a1.run()


b1 = B()
b1.sex = "T"
print(b1.sex)
b1.name = 66.66
print(b1.name)
