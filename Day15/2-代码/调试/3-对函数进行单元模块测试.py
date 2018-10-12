'''
单元测试：可以对一个函数、一个类、一个模块进行单独的正确性检测
结论：当单元测试正确通过，代表函数、类等无错误。
      当单元测试不通过，代表函数、类等有错误，也有可能是单元测试的
      结论有错。
'''

def addNum(num1,num2):
    return num1 + num2
print(addNum(12345, 9876543))

# 进行单元测试的模块
import unittest
# TestCase:测试用例
class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时自动调用")
    def tearDown(self):
        print("结束测试时自动调用")
    # 注：进行测试的方法必须以test开头
    # 测试addNum函数
    def test_addNum(self):
        # assert在测试函数中进行断言测试
        # self.assertEqual(测试的函数(结论), 程序员自己得出的结论, 错误提示语句)
        self.assertEqual(addNum(1, 2), 3, "addNum函数有问题")

# 启动单元测试
unittest.main()



