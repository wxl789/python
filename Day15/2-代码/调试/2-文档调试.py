# 文档调试模块
import doctest
# doctest：可以提取注释中的代码进行运行
# 注：doctest严格按照交互模式下的输入及输出方式运行

def addNum(num1, num2):
    # 要求使用多行注释的方式
    '''
    :param num1: 第一个形参
    :param num2: 第二个形参
    :return: 返回形参的和
    要求程序员完全清楚代码逻辑
    注: 空格
    >>> print(addNum(1, 2))
    3
    '''
    return num1 + num2

print(addNum(143234567899, 223456789876))

# 开始使用文档测试
doctest.testmod()






