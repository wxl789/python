# __str__函数：__str__():当打印实例对象的时自动调用。
# 注：该方法必须有一个str类型的返回值
# __str__是给用户用来描述实例对象的方法
# 优点：当我们需要打印实例对象的多个属性时，可以使用__str__,
#       这种方式会简化我们的代码量。

class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    # 在类中重写__str__方法
    def __str__(self):
        return self.name + str(self.age) + str(self.sex)
p1 = Person('lily', 12, 23)
p2 = Person("lucy", 34, 67)
print(p1)





