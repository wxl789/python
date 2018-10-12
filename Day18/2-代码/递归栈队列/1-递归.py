'''
递归：一个函数在自己函数内部调用自己。
循环
'''

num = 5
def func():
    global num
    if num == 0:
        return 0
    else:
        print("12345")
        num -= 1
        func()

func()
# 复习递归遍历目录
