# 1、
#    1.1、从控制台输入两个数，输出较大的那个数
#    1.2、从控制台输入三个数，输出较大的那个数
#     不准使用max min


# 2、判断平闰年
'''a%400=0

闰年的条件：1、能被4整除，不能被100整除
             2、能被400整除
满足以上两个条件的任意一个就是闰年。
'''
a = input("数字：")
if int(a) % 400 == 0:
    print("shi")
else:
    print("no")
# 3、中奖：从控制台输入一个数字，判断是否与随机的哪个数字一致，一致则
#    中奖；不一致，提示很遗憾


# 4、从控制台输入一个五位数，是回文数打印yes，不是打印no
# 12321    11111   11211   32523


# 5、从控制台输入一个三位数，判断当前数字是否为水仙花数，是打印yes，
# 否打印no
# 153   1^3+5^3+3^3 = 153
# 222

# String
# 循环语句
# List
