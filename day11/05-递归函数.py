"""
定义：
    一个函数在其内部不调用其他的函数，而是调用自身---》递归函数
    类似循环--》死循环

"""

# def demo():
#     demo()
#     print("haha")
# def demo1():
#     print("hahei")
#
# demo()
"""
例子：
   计算n阶乘
   
   n! = 1*2*3...*n
   
   1！= 1
   2！= 2 * 1 = 2 * 1！
   3！= 3 * 2 * 1 = 3 * 2！
   4！= 4 * 3！
   
"""
def calnum(num):
    i = 1
    reslut = 1
    while i <= num:
        reslut *= i
        i += 1
    return reslut
ret = calnum(3)
print(ret)

#递归
def calnum1(num):
    if num >= 1:
        reslut = num * calnum1(num-1)
    else:
        reslut = 1
    return reslut

ret = calnum1(4)
print(ret)

#自己玩自己，防止死递归，一定要给一个出口（判断条件）