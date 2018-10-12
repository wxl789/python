# 多继承： 一个子类拥有多个父类
# 父类
class Father():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def merry(self):
        print("爸爸和妈妈结婚了")
    def work(self):
        print("F--挣钱养家")
class Mother():
    def __init__(self, name, faceValue):
        self.name = name
        self.faceValue = faceValue
    def makeChild(self):
        print("生宝宝")
    def work(self):
        print("M--貌美如花")
# 注：如果父类们的方法或属性有重名的，默认执行列表前面的
# 类中的属性或方法 --- 就近原则

# 子类 child 继承与F  M
class Child(Father, Mother):
    def __init__(self, name, age, face):
        Father.__init__(self, name, age)
        Mother.__init__(self, name, face)
    def work(self):
        Father.work(self)
        Mother.work(self)
        print("孝敬父母")
c1 = Child("c1", 12, 89)
c1.work()
c1.merry()
c1.makeChild()
print(c1.name, c1.age, c1.faceValue)






