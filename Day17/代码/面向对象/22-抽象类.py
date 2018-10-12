# 强类型语言：C Java   在声明变量之前将变量类型确定   int a = 1
# 弱类型语言: python  变量的数据类型根据赋值符号后面的类型确定  a = 1 

'''
抽象类：
封装
某些类中的属性或方法不能完整的描述一个对象时，可以将该类
作为抽象类。一般抽象类只是辅助其他具体的类而出现并使用的。

抽象类中可以存在抽象方法，抽象方法为不包含任何方法具有体实现
内容的函数。
一般含有抽象方法的类都是抽象类。
注：抽象类一般都当作父类使用，抽象类的子类要求实现所有的抽象方法，
否则子类也是抽象类。

类：从多个对象中抽取出来的。
抽象类：从多个类中抽取出来的。

注：抽象类不能实例化对象。
Animal
Cat
Dog
'''
'''
1、定义抽象类
a、定义抽象类需要导入模块abc中的ABCMeta（抽象类的基类）类
(Abstract BaseClass)
b、定义抽象类时，在父类列表中加入 metaclass=ABCMeta,指定
该类的基类为ABCMeta。
c、不含有抽象方法的抽象类可以实例化对象。
d、含有抽象方法的抽象类不能实例化对象。
e、抽象类一般只当作父类使用。
f、抽象类中可以包含属性及对象方法。

2、定义抽象方法
a、定义抽象方法需要导入模块abc中的abstractmethod类
b、定义抽象方法时，需要在方法之前加入@abstractmethod装饰器名称。
c、抽象方法一般不需要实现内容，函数体语句只写一个pass语句即可。

3、实现类
a、实现类为抽象类的子类。
b、实现类如果不实现父类的抽象方法，该实现类也是抽象类；
实现类如果实现父类的抽象方法，该实现类就是普通的类，可以正常
实例化对象。

'''

from abc import ABCMeta, abstractmethod
# 抽象类
class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        # 属性
        self.name = name
    # 对象方法
    def eat(self):
        print("eat")
    # 抽象方法
    @abstractmethod
    def play(self):
        pass
# TypeError: Can't instantiate abstract
# class Animal with abstract methods play
# a1 = Animal("妹妹")
# print(a1)

# 实现类
class Cat(Animal):
    # 子类实现父类的抽象方法
    def play(self):
        print("play")

c1 = Cat("Lily")









