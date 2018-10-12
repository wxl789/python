'''
继承：封装，为了简化代码量，更好的维护代码
父类：object（所有类的父类，祖宗）
子类：父类的衍生类
子类可以继承父类中所有的属性及方法(私有属性或私有方法除外)

一个父类可以存在多个子类。


子类可以继承父类的共有属性及方法。
子类可以拥有自己独有的属性及方法
注：__init__:如果本类中存在构造方法，实例化对象会调用自己本
类中的构造方法，如果需要执行父类中构造方法中的内容，需要在子
类中调用父类的构造方法。
建议：以后创建的所有的类全部写出构造方法，具体构造方法中的内容，
视情况而定。

就近原则：当对象调用的属性或方法时，先去查看自己本类中是否
存在，存在直接使用，不存在，再去父类中查找。如果所有的祖先类中
均不存在，则报错。

方法重写：子类中中存在与父类相同名称的方法，并且子类实现了
该方法，这种操作叫做方法的重写。

'''
'''
语法格式：
class 类名(父类列表):
    属性
    方法
'''
# Animal : name color age  run()  play()
# Cat：name color age miao run()  play()  getMouse()
# Dog：name color age wang run()  play()  watchHome()

class Animal():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        # 私有属性
        self.__age = age
    def run(self):
        print(self.name + "跑")
class Cat(Animal):
    def __init__(self, name, color, age, miao):
        # 调用父类的__init__方法
        # 父类名称.__init__(self,根据父类的形参个数赋值)
        # 相当于将父类的函数中所有的内容复制过来
        Animal.__init__(self, name, color, age)
        # 子类自己的属性
        self.miao = miao
    # 子类自己的方法
    def getMouse(self):
        Animal.run(self)
        print("猫捉老鼠")
    # 子类重写父类的方法
    def run(self):
        # 父类名称.方法名(self,根据父类的形参个数赋值)
        Animal.run(self)
        print(self.name+"跑得快")
c1 = Cat("弟弟","煤球", 1,"喵")
print(c1.miao)
print(c1.name)
c1.getMouse()
c1.run()



# object:所有类的父类,如果父类列表为空，默认继承object

# class Per():
#     pass
class Per(object):
    pass



# class object:
#     def __init__(self):
#     def __str__(self):