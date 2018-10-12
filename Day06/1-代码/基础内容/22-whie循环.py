# while 循环
# 作用：简化代码量
'''
语法格式：
while 条件:
    语句
条件为boolean类型
'''
'''
逻辑:当程序执行到while语句时，首先判断条件是否为真，为真则
执行语句，语句执行结束后，继续判断条件是否为真，为真则
执行语句，直到条件为假，退出while语句。

注：当使用while语句 时，循环执行的语句中一定要存在一条可以更改
while后面的条件的语句。
注：当条件一直成立时，会变成死循环，循环的语句一直执行。
'''
num = 1
while num <= 3:
    print("hello")
    num = num + 1

print("while")
'''
num =1    ==> num=2
num=2 ==> num=3
...
num=5 ==> num=6
退出
'''


# 10000米  1000米

# 输出0-10
num = 0
while num <= 10:
    print(num)
    num = num + 1

# 输出1-10的和
num = 1
sum1 = 0
while num <= 10:
    sum1 += num
    num += 1
print(sum1)

# 输出0-10，不输出3
num = 0
while num <= 10:
    if num != 3:
        print(num)
    num += 1

# while-else循环
'''
while 条件:
    语句
else:
    语句
解释：当while后面的条件不成立时，执行else语句，else语句最多只会
执行一次
'''
# 打印 1-3
num = 1
while num <= 3:
    print(num)
    num += 1
else:
    print("啦啦啦啦")





