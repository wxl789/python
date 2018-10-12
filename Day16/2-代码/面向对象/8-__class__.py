# __class__ : 代表当前类的类名，是类的默认存在的属性
class Net():
    def run(self):
        print("123")
        print(self.__class__)

n1 = Net()
print(n1.__class__)
n1.run()
