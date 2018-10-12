class Student():
    name = ""
    age = 17
    # 普通成员方法
    def studyGame(self):
        print("学习刻苦")
    def eatFood(self):
        return "工作餐"
    # 构造函数
    '''
    构造函数：在实例化对象时调用
    注：如果我们自己没有在类写出构造函数，系统会自动添加一
    个空的构造函数。
    构造函数的函数名： __init__
    注：构造函数只能返回None，不能返回其他类型数据，以后__init__函数
    不要自己添加return语句。
    使用构造函数：
    def __init__(参数列表):
        语句
    '''
    # 默认的构造函数
    # def __init__(self):
    #     pass
    # 自己改写构造函数
    def __init__(self):
        print("我是student的构造函数")
        print("9")


# Student() 执行构造函数(初始化函数)__init__
stu1 = Student()
print(stu1.eatFood())
print(stu1.name)
stu2 = Student()



