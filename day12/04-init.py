
"""
初始化函数，用于完成默认的设定
def __init__():
    pass
"""
#定义汽车类
# class Car:
#     def __init__(self):
#         self.color = "蓝色"
#         self.wheelNum = 4
#
#     def move(self):
#         print("车子在移动")
#
# #创建对象
# BMW = Car()
# print(BMW.color)
# print(BMW.wheelNum)

class Car:
    def __init__(self,newColor,newWheelNum):
        self.color = newColor
        self.wheelNum = newWheelNum

    def move(self):
        print("车子在移动")

#创建对象
BMW = Car("蓝色",4)
print(BMW.color)
print(BMW.wheelNum)
BMW1 = Car("红色",6)
print(BMW1.color)
print(BMW1.wheelNum)
