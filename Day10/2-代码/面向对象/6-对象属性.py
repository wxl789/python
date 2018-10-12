class Student():
    # 类属性
    # name = "Lucy"
    # __init__可以修改函数体语句，也可以修改形参个数
    # def __init__(self):
    #     print("初始化")
    # 增加了形参个数
    # self:代表当前类的实例对象,哪个对象正在使用，代表哪一个对象。
    # self本身是一个可变的对象
    # 可以使用默认值的形式
    # 注：__init__在一个类中只出现一次即可，如果有多个，只会调用最后一次
    # 声明的函数。
    def __init__(self, name,age,sex=0):
        # print("初始化形参")
        # 对象属性
        # 语法格式： self.属性名=常量值
        self.name = name
        self.age = age
        self.sex = sex


# stu1 = Student()
# print(stu1.name)
# 当构造函数有行参时，需要传入实参
stu2 = Student("lily",17,0)
print(stu2.name)
print(stu2.age)
print(stu2.sex)
stu3 = Student("Lilei",34,1)
print(stu3.name)
# 建议：初始化对象时，如果需要同时传入多个实参，使用关键字形式。
stu4 = Student(name="1",age=2,sex=3)
print(stu4.name)
stu5 = Student("马云",56)
print(stu5.name)
print(stu5.sex)
stu5.name = "马化腾"  # 属性可以重复赋值
print(stu5.name)
