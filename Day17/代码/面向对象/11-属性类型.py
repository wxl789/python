# 属性类型：四种
# 公有属性  私有属性  特殊属性  公有属性中的私有属性

class Bird():
    def __init__(self, name, age, sex, color):
        # 1、公有属性：能够在本类、本类的对象、子类中均可使用
        # 格式 : self.属性名 = 值
        self.name = name
        # 2、私有属性：只能在当前类中使用
        # 格式 : self.__属性名 = 值（属性名称前有两个下划线）
        self.__age = age
        # 3、特殊属性：使用方式与公有属性一致
        # 格式 : self.__属性名__ = 值（属性名称前后各有两个下划线）
        # 系统默认存在属性一般使用该格式，以后除非属性有特殊用法，
        # 否则尽量不要使用该方式。
        self.__sex__ = sex
        # 4、特殊变量:使用方式与公有属性一致,但以后如果见到该格式
        # 的属性，把他当成私有属性使用。
        # 格式 : self._属性名 = 值（属性名称前有一个下划线）
        # （虽然_属性名 是公有属性，但请当成私有属性使用。）
        self._color = color
    def eat(self):
        print(self.name)
        print(self.__age)
        print(self.__sex__)
        print(self._color)
    # set及get方法：私有属性与公有属性均可存在
    # set及get优点：可以在方法中对传入的数据进行处理
    # set  赋值
    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age
    # get  取值   return 返回值
    def getAge(self):
        return self.__age

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
b1 = Bird("麻雀", -13, 1, "白色")
print(b1.name)
print(b1.__sex__)
print(b1._color)
b1.eat()
b1.setAge(-230)
print("--------------")
print(b1.getAge())



