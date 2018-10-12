#定义父类
class A:
    def printA(self):
        print("-----A------")

#定义一个父类
class B:
    def printB(self):
        print("------B=------")

#定义一个子类
class C(A,B):
    def printC(self):
        print("----C-----")

#创建子类的对象
obj_c = C()

obj_c.printA()
obj_c.printB()

"""
说明：
   python 中可以完成多继承
   父类中公有的属性和方法都会被子类所继承
   
思考：
     如果按照上面的例子，如果父类A和父类B中，有一个同名的方法，通过子类的对象调用父类同名的方法的时候
     ，调用哪一个   
"""

class D:
    def printA(self):
        print("-----A------")

#定义一个父类
class E:
    def printA(self):
        print("------B=------")

#定义一个子类
class F(E,D):
    def printB(self):
        print("----C-----")
#创建子类的对象
f = F()
f.printA()
print(F.__mro__)#可以查看F类的对象搜索方法时的先后顺序

"""
一个学校，人数为0，入职老师，学生，人数增加，
老师显示姓名和工资，学生显示姓名和成绩

"""
#定义学校类
class School:
    schoolNum = 0
    #初始化数据
    def __init__(self,name):
        self.name = name
        School.schoolNum += 1
        print("学校新加入的成员%s"%self.name)
        print("学校现在的人数为：%d"%School.schoolNum)

    #自我介绍
    def sayHello(self):
        print("我叫%s"%self.name)

#创建老师类
class Teacher(School):
    def __init__(self,name,wage):
        a = School(name)
        self.name = name
        self.wage = wage

    def sayHello(self):
        print("我叫%s,我的工资为%d"%(self.name,self.wage))

#创建学生类
class Student(School):
    def __init__(self, name, reslut):
        a = School(name)
        self.name = name
        self.reslut = reslut

    def sayHello(self):
        print("我叫%s,我的成绩为%d" % (self.name, self.reslut))


t = Teacher("张三",2000)
t.sayHello()

s = Student("李四",90)
s.sayHello()

# 思考：如何在子类中调用父类同名的方法







