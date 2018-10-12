'''
# 1、
#    1.1、从控制台输入两个数，输出较大的那个数
#    1.2、从控制台输入三个数，输出较大的那个数
#     不准使用max min
a = input("")
b = input("")
c = input("")
max == a
if b > a:
    max == b
    if c > b:
        max = c
print(max)


print("**************")

# 2、判断平闰年
'''
# 闰年的条件：1、能被4整除，不能被100整除
#              2、能被400整除
# 满足以上两个条件的任意一个就是闰年。
'''
a = int(input(":"))
if (a % 4 == 0 and a % 100 != 0) or a % 100 == 0:
    print("y")
else:
    print("n")
'''
'''
# 3、中奖：从控制台输入一个数字，判断是否与随机的哪个数字一致，一致则
#    中奖；不一致，提示很遗憾
import random
res = random.randrange(20)
print(res)
b = int(input(""))
if res == b:
    print("g")
else:
    print("s")
'''
# 4、从控制台输入一个五位数，是回文数打印yes，不是打印no
# 12321    11111   11211   32523
'''
a = int(input())  # 12321
ge = a % 10
shi = (a // 10) % 10
qian = (a // 1000) % 10
wan = a // 10000
if ge==wan and qian==shi:
    print("yes")
else:
    print("no")
'''

# 5、从控制台输入一个三位数，判断当前数字是否为水仙花数，是打印yes，
# 否打印no
# 153   1^3+5^3+3^3 = 153
# 222
'''
a = int(input())  # 153
ge = a % 10
shi = (a // 10) % 10
bai = a // 100
if ge**3+shi**3+bai**3 == a:
    print("yes")
else:
    print("no")
'''

# String
# 循环语句
# List
