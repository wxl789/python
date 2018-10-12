import time


class Animal(object):
    #初始化时的动作
    def __init__(self,name):
        print("__init__方法被调用")
        self.name = name
    #析构：当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉"%self.name)
# #创建对象
# dog = Animal("哈皮狗")
# #删除对象
# del dog

cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print("----马上删除cat对象")
del cat
print("----马上删除cat2对象")
del cat2
print("----马上删除cat3对象")
del cat3
print("程序2秒后结束")
time.sleep(2)
"""
当1个变量保存了对象的引用时，此时该对象的引用计数会加1
当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如是3，那么此时只会让这个引用计数减1
变为2，当再一次调用del时，变为1，如果在调用一次del,对应的引用计数为0，当引用计数为0时候，此时对象才会被真正的删除
"""








