
"""
一个父类可以有多个子类
"""
#父类
class F1(object):
    def show(self):
        print("f1.show")

#定义子类
class S1(F1):
    def show(self):
        print("S1.show")
#定义子类
class S2(F1):
    def show(self):
        print("S2.show")

f = F1()
f.show()

s = S1()
s.show()

s = S2()
s.show()
