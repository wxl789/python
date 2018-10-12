# super：父类
class Father():
    def __init__(self, name):
        self.name = name
    def drink(self):
        print("F--喝酒")
class Child(Father):
    def __init__(self, name, gf):
        # Father.__init__(self, name)
        # 使用super调用父类相关方法
        # 格式：super(子类名称, self).__init__(父类的形参对应的实参)
        super(Child, self).__init__(name)
        self.gf = gf
    def drink(self):
        # Father.drink(self)
        super(Child, self).drink()
        print("C--喝酒")
c1 = Child("高富帅", "Lily")
print(c1.name, c1.gf)
c1.drink()


