# 1、遍历一维列表 [1,2,3,4]、
# 遍历二维列表[[1,2,3,4],[6,8],[9,8,7]]
'''
list1 = [1,2,3,4]
for i in list1:
    print(i)
list2 = [[1,2,3,4],[5,6,7],[9,8]]
for i in list2:
    print(i)
    for j in i:
        print(j)
'''

# 2、输出50以内能被7整除的数
'''
for i in range(51):
    if i % 7 == 0:
        print(i) 
'''
# 3、给定一个字符串，判断该字符串中有多少个a   jhgfdsdtyaaawertyukjbvaa
'''
str1 = input('字符串')
count = 0
for i in str1:
    if i == 'a':
        count += 1
print(count)
'''

# 4、给定一个字符串，输出字符串的下标及对应下标位置的字符
'''
str1 = input("字符串")
for i in range(len(str1)):
    print(i, str1[i])
'''
# 5、输出九九乘法
'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
'''
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t"%(i,j,i*j),end="")
    print()
'''
# 6、
'''
  *
 **
***
'''
'''
for i in range(3):
    for j in range(3 - i - 1):
        print(" ",end="")
    for k in range(i + 1):
        print("*",end="")
    print()
'''
'''
  *
 ***
*****
'''
'''
for i in range(3):
    for j in range(3 - i - 1):
        print(" ",end="")
    for k in range(i*2 + 1):
        print("*",end="")
    print()
'''

# 7、将一个字符串中的小写字母转为大写，将大写字母转为小写，
# 其他字符不变  不能用swapcase
# abcED123f  ----> ABCed123F
# 97 -32   +32   for  if
'''
str1 = input("字符串")
res = ""
for i in str1:
    if i <= "z" and i >= "a":
        res += chr(ord(i) - 32)
    elif i <= "Z" and i >= "A":
        res += chr(ord(i) + 32)
    else:
        res += i
print(res)
'''

# 8、将字符串abcd变为字符串4567
# asc   -45
# 密码加密
'''
str1 = input("字符串")
res = ""
for i in str1:
    res += chr(ord(i) - 10)
print(res)
'''

# 9、随机产生一个长度为6的字符串，字符串中可能包含大写字母，
# 小写字母或数字
# s2AHr6   SaeR9T
'''

import random
str6 = ""
for i in range(6):
    ty = random.randrange(3)
    if ty == 0:
        # 随机大写
        ch = chr(random.randrange(ord("A"), ord("Z") + 1))
        str6 += ch
    elif ty == 1:
        # 随机小写
        ch = chr(random.randrange(ord("a"), ord("z") + 1))
        str6 += ch
    elif ty == 2:
        # 随机数字
        ch = chr(random.randrange(ord("0"), ord("9") + 1))
        str6 += ch
print(str6)

'''

# 10. 输出10行内容，每行的内容都是“*****”。
'''
for i in range(10):
    print("*****")
'''

# 11. 输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，
# 依此类推第10行10个星号。
'''
for i in range(10):
    for j in range(i + 1):
        print("*",end="")
    print()
'''


# 12. 输出9行内容，第1行输出1，第2行输出12，第3行输出123，
# 以此类推，第9行输出123456789。
'''
for i in range(1,10):
    str1 = ""
    for j in range(1,i + 1):
        str1 += str(j)
    print(str1)
'''

# 13. 计算10个99相加后的值并输出。
'''
num = 0
for i in range(10):
    num += 99
print(num)
'''


# 14. 计算从1加到100的值并输出。
'''
num = 0
for i in range(101):
    num += i
print(num)
'''


# 15. 计算10的阶乘（1x2x3x4x5x6x7x8x9x10）
'''
num = 1

for i in range(1,11):
    num *= i

print(num)

'''

# 16. 计算2的20次方。不允许用**和pow()
'''
num = 1
for i in range(20):
    num *= 2
print(num)
print(2**20)
'''

# 17. 计算从1到1000以内所有奇数的和并输出。
'''
num = 0
for i in range(1,1001):
    if i % 2 == 1:
        num += i
print(num)
'''

# 18. 计算从1到1000以内所有能被3或者17整除的数的和并输出
'''
num = 0
for i in range(1,1001):
    if i % 3 == 0 or i % 17 == 0:
        num += i
print(num)
'''

# 19. 计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
'''
num = 0
for i in range(1,1001):
    if i % 3 == 0 and i % 7 == 0 and i % 5 == 0:
        num += i
print(num)
'''

# 20. 计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
'''
num = 0
for i in range(1,101):
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        print(i)
        num += 1
print(num)
'''
'''
num = 0
for i in range(1,101):
    if (i % 3 == 0 or i % 7 == 0) and not(i % 3 == 0 and i % 7 == 0):
        print(i)
        num += 1
print(num)

'''

# 21. 计算1到100以内能被7整除但不是偶数的数的个数。
'''
num = 0
for i in range(1,101):
    if i % 7 == 0 and i % 2 != 0:
        num += 1
print(num)
'''

# 22. 计算从1到100临近两个整数的合并依次输出。比如第一次输出3(1+2)，
# 第二次输出5(2+3)，最后一次输出199(99+100)。
'''
for i in range(1,100):
    print("%d(%d+%d)"%(i+i+1,i,i+1))

'''


# 23. 给定一个整数n，判断是否是质数（质数是只能被1和它自身整除的数）
'''
n = int(input())
if n==0 or n == 1 or n == 2:
    print("质数")
else:
    for i in (2,n):
        if n % i != 0:
            print("质数")

'''


# 24. 给定一个不大于9的数n，打印nn乘法表
'''

k = int(input())
for i in range(1,k+1):
    for j in range(1,i+1):
        print("%d*%d=%d\t"%(i,j,i*j),end="")
    print()
'''

# 25. 五位数中，对称的数称为回文数，打印所有的回文数并计算个数。
# 如:12321
'''
count = 0
for i in range(10000,100000):
    a = i % 10
    b = i // 10 % 10

    c = i // 10000
    d = i // 1000 % 10
    if a == c and b == d:
        print(i)
        count += 1
print(count)

'''
# 26. 给定一个n位（不超过10）的整数，将该数按位逆置，
# 例如给定12345变成54321，12320变成2321.  (不能用[::-1])
'''
a = input()
str1 = ""
for i in range(len(a)):
    # print(a)
    c = int(a) % 10
    a = str(int(a) // 10)
    str1 += str(c)
print(int(str1))

'''




# 27. 输出所有的三位水仙花数，其各位数字立方和等于该数本身。
'''
for i in range(100,1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if a**3 + b**3 + c**3 == i:
        print(i)
'''


# 28. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。
# 求它在第n次落地时，共经过多少米？
'''
i = 100 / 2
b = int(input())
sum1 = 100
if b == 1:
    pass
else:
    for c in range(b-1):
        sum1 += (i * 2)
        i = i / 2

print(sum1)

'''


# 29. 给定一个数a,求s=a+aa+aaa+aaaa+aaaaa的值，其中a是一
# 个数字（1-9之间）。例如2+22+222+2222+22222
'''
i = int(input())
sum1 = 0
str1 = ""
for j in range(1,6):
    str1 += str(i)
    sum1 += int(str1)
print(sum1)
'''


# 30. 已知 abc+cba=1333, 其中的a,b,c均为一位数，编写一个程序，
# 求出a,b,c分别代表什么数字
'''
for i in range(100,1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    str1 = str(a) + str(b)+str(c)
    # print(str1)
    if i + int(str1) == 1333:
        print("%d   %d   %d" % (a,b,c))

'''



# 31. 给定一个整数n，打印3到n以下的所有质数（质数是只能被1和它
# 自身整除的数）
'''
n = int(input())
for i in range(3,n+1):
    j = 2
    while j <= i:
        if i % j == 0:
            break
        else:
            j += 1
        if i == j:
            print(i)
'''



# 32. 求整数1~100的和，但要求跳过所有个位为3的数。 3 13 23
'''
sum1 = 0
for i in range(1,101):
    if i % 10 != 3:
        sum1+=i
        print(i)
print(sum1)

'''
#请分别用while和for两种方式来实现

'''
33. 实现一个课程名称和课程代号的转换器：输入下表中的课程代号，
输出课程的名称。用户可以循环进行输入，如果输入n就退出系统。

1     PHP
2     Python
3     JS
4     JAVA
n     退出
'''

'''
34.幸运猜猜猜： 游戏随机给出一个0-99的数字，然后让你猜是什么数字。
你可以对边猜一个数字，游戏会提示太大或者太小，从而缩小结果范围。
经过几次猜测与提示后，最终推出答案。在游戏过程在中，
记录你最终猜对是所需要的次数，游戏结束后公布结果。
猜测次数最多20次。
假设随机数： 67
第一次猜 45  提示太小  46-99
第二次猜 78  提示太大  46-77
。。。
67  正确
20之后未猜到：提示：你猜我猜不猜




'''

# 864659104@qq.com
