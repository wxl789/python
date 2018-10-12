

"""
创建对象的基本格式
对象名 = 类名()
"""
class Cat:
    #属性
    #方法
    def eat(self):
        print("猫在吃鱼")
    def drink(self):
        print("猫在喝kele.....")

bosi = Cat()#产生Cat类的实例对象
jiafei = Cat()

bosi.color = "黑白"
bosi.tui = 4
jiafei.color = "花色"

print(bosi.color)
bosi.eat()
"""
bosi/jiafei   拥有属性和方法
"""



