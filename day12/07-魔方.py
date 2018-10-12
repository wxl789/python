
class Car(object):
    def __init__(self,newWheelNum,newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
    def move(self):
        print("车子在移动")

    def __str__(self):
        msg = "车子的颜色是"+self.color+"我有"+self.wheelNum+"个轮子"
        return msg

#创建对象
BMW = Car("4","白色")
print(BMW.color)
print(BMW.wheelNum)
print(BMW)
"""
在python中方法名__XXXX__()---->魔方方法
当使用print输出对象时，子要定义__str__（）就会打印该方法中return中的数据
"""











