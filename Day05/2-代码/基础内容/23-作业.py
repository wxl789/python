# 1、输出1-100的和
'''
num = 0
sum1 = 0
while num <= 100:
    sum1 += num
    num +=1
print(sum1)
'''

# 2、输出100以内能被8整除的数
'''
num = 0
while num <= 100:
    # 条件
     if num % 8 == 0:
         print(num)
    # 更改循环条件
     num += 1
'''

# 3、输出100-999之间所有的水仙花数
'''
num = 100
while num < 1000:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if a**3+b**3+c**3 == num:
        print(num)
    num += 1
'''

# 4、输出2000-2999之间所有的闰年
'''
num = 2000
while num < 3000:
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        print(num)
    num += 1
'''

# 5、给定一个字符串，输出字符的下标及该下标对应的字符
'''
str1 = input("输入内容")
num = 0
while num <= len(str1):
    # print(num)
    print(num, str1[num])
    num += 1
'''

# 6、给定一个整数，判断整数的位数（不能使用len）  while
# 2345678987654
'''
numStr = input("数字")
num = int(numStr)
count = 0
if num == 0:
    count = 1
while num != 0:
    # 当num为负数，绝对值
    num = abs(num)
    num = num // 10  # 123  -- 12  -- 1  -- 0
    count += 1
print(count)
'''


# 7、给定一个字符串，判断该字符串中a的个数
# ghjkiuyaaatyiuavhjkaaghjkj
'''
num = 0  # 初始下标为0
count = 0  # 默认a的个数为0
str1 = input("字符串")
while num < len(str1):
    if "a" == str1[num]:
        count += 1
    num += 1
print(count)
'''

# 8、密码加密
# 如：abcd  ---> tuvw   : 实际将a的ASC在原本基础上+ 23
str1 = input("密码")
# print(str1)
i = 0
res = ""
# xyz   nop
while i < len(str1):
    ch = ord(str1[i]) - 10
    s = chr(ch)
    res += s
    i += 1
print(res)



# 使用for循环改写

# 864659104@qq.com

