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

# 子类 child 继承与F  M
class Child(Father, Mother):
    def __init__(self, name, age, face):
        super(Child, self).__init__(name, age)
        super(Father, self).__init__(name, face)
# super的查找原则
# Child->Father->Mother->object
    def work(self):
        # super(Child, self).work()
        super(Father, self).work()
        print("孝敬父母")
c1 = Child("高富帅", 18, 98)
print(c1.name, c1.age)
print(c1.faceValue)
c1.work()


