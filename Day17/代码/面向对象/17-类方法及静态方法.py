# 类方法  静态方法
class Person():
    # 对象方法，使用实例对象调用
    def eat(self):
        print("eat")

    # 类方法
    # 类方法一般使用类名调用。
    # 类方法可以使用类或实例对象调用,但cls永远代表类。
    # cls不是关键字，换成其他名称也可以，但尽量使用cls。
    @classmethod
    def drinkWater(cls, a):
        print("drink")
        print(cls)
        print(a)
    # 静态方法
    # 静态方法一般使用类名调用。
    # 静态方法就是一个普通函数，定义时有几个形参，调用时就传
    # 入几个实参。
    # 静态方法可以使用类或实例对象调用,但一般使用类名调用。
    @staticmethod
    def run(num1):
        print("跑" + num1)
p1 = Person()
p1.eat()
# 对象方法可以用类名调用，但需要传入一个实例对象的实参
# 建议：对象方法尽量使用对象调用
Person.eat(p1)

# 类方法
Person.drinkWater(12)
p1.drinkWater(45)

# 静态方法
Person.run("fff")
p1.run("mmm")


