print(1 + 2) # 加法运算
print("a" + "b") # 拼接

class Stu():
    def __init__(self, age):
        self.age = age

    # 运算符重载
    # 要求必须存在返回值
    # 注：返回值的类型尽量与该类型一致
    def __add__(self, other):
        return Stu(self.age + other.age)

s1 = Stu(12)
s2 = Stu(34)
s3 = s1 + s2  # s1.__add__(s2)
print(s3.age)
'''
__init__:
__del__:
__str__:
__add__: 加
__sub__: 减
__mul__: 乘
__div__: 除
__pow__: 幂
__mod__: 余
'''




