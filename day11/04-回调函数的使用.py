
#案例1：
def clean1(count):
    """
    清扫
    :param count: 清扫的次数
    :return: None
    """
    print("已完成扫地的次数",str(count))

def clean2(count):
    """
    清扫
    :param count: 清扫的次数
    :return: None
    """
    print("已完成洒水的次数", str(count))

def call_clean(count,function_names):
    """
    控制系统，
    :param count: 次数
    :param function_names: 回调函数名
    :return: 调用函数结果
    """
    return function_names(count)
call_clean(100,clean2)

#案例2:
#回调函数
#定义一个函数，生成一个2k形式的偶数
def double(x):
    return 2 * x

##定义一个函数，生成一个4k形式的偶数
def double2(x):
    return 4 * x

#中间函数
#接受一个生成偶数作为参数，返回一个奇数
def getOddNumber(k,getEvenNumber):
    return getEvenNumber(k) + 1

#定义一个起始函数，程序的主函数
def main():
    k = 1
    i = getOddNumber(k,double)
    k = 1
    j = getOddNumber(k, double2)
    #当需要一个8k
    g = getOddNumber(k,lambda x:x * 8)
"""
回调函数的使用增加程序的灵活性，通用性，调用者不知情
"""