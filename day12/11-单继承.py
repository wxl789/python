
#定义一个父类
class Cat(object):
    def __init__(self,name,color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print("%s-----在跑"%self.name)

#定义一个子类，继承Cat父类
"""
继承的格式：
  class 子类名（父类名）
  
  子类在继承的时候，在定义类时，小括号中为父的名字
  父类的属性和方法，会继承给子类（公有）
  
"""
class Bosi(Cat):
    def setNewName(self,newName):
        self.name = newName

    def eat(self):
        print("%s-----在吃"%self.name)

#创建子类对象
bs = Bosi("波斯猫")
print("bs的名字为：%s"%bs.name)
print(bs.color)
bs.eat()
bs.run()

class Animal(object):
    def __init__(self,name="动物",color="白色"):
        self.__name = name
        self.color = color

    def __run(self):
        print(self.__name)
        print(self.color)

    def run(self):
        print(self.__name)
        print(self.color)

class Dog(Animal):
    def dogRun(self):
        #print(self.__name)#不能获取父类私有的属性
        print(self.color)
    def dogRun1(self):
        # self.__run()#不能继承父类的私有的方法
        self.run()

A = Animal()
# print(A.__name)#不能访问私有属性
print(A.color)
# A.__run()#不能访问私有的方法

print("------华丽的分割线--------")
D = Dog(name="小花狗",color="花色")
D.dogRun()
D.dogRun1()

"""
继承：
     子类只能继承父类公有的属性和方法，
     私有属性和方法不能被子类继承
     
 私有的属性，不能通过对象直接进行访问，但是可以通过方法进行访问
 私有的方法：不能通过对象进行访问
 私有的属性/方法，不会被子类所继承，也不能被访问    
"""












