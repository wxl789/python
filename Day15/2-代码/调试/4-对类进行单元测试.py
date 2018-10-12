class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
per1 = Person("Lily", 23)
print(per1.getName())

import unittest
class Test(unittest.TestCase):
    # 用于测试的方法
    def test_init(self):
        per = Person("Tom", 23)
        self.assertEqual(per.name, "Tom", "init方法有问题")
    def test_getName(self):
        per = Person("Jerry", 34)
        self.assertEqual(per.getName(), "Jerry", "getName有问题")

# 开始进行测试
unittest.main()






