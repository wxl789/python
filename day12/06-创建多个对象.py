

class Cat:
    #属性
    def __init__(self,name):
        self.name = name
    #方法
    def eat(self):
        print("猫在吃鱼")
    def drink(self):
        print("猫在喝kele.....")


#创建对象
tom = Cat("tom")
tom.eat()
tom.drink()

tom1 = Cat("tom1")
tom1.eat()
tom1.drink()


