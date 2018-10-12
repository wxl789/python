'''# 1、
a = 1
b = 0
while a <= 100:
    b = b + a
    a = a + 1
    print(b)


# 2、
a = 0
while a <= 100:
    if a % 8 == 0:
        print(a)
    a= a+1



# 3、
num = 100
while num <= 999:
    if num == (num// 100)**3 + (num // 10 % 10)**3 + (num % 10)**3:
        print(num)
    num = num + 1
# 4、
num = 2000
while num <= 2999:
    if (num % 4 == 0 and num % 100 != 0) or num % 400 ==0:
        print(num)
    num = num + 1

# 5、
str1 = input("请输入一个字符串：")
num = 0
while num < len(str1):
    print(num, str1[num])
    num = num + 1

# 6、给定一个整数，判断整数的位数（不能使用len）  while
# 2345678987654
'''
num = int(input("请输入一个整数："))
a = 10
b = 0
while (num / a) > 1:
    b = b + 1
    a = a * 10
print(b + 1)





# 7、给定一个字符串，判断该字符串中a的个数
# ghjkiuyaaatyiuavhjkaaghjkj
num = "ghjkiuyaaatyiuavhjkaaghjkj"
print(num.count("a"))
# 8、密码加密
# 如：abcd  ---> tuvw   : 实际将a的ASC在原本基础上+ 23
str1 = input("输入要加密的字符串：")
num = 0
print("加密后的数字：")
while num < str1:
    print(ord((str1[num]) + 23))
# 864659104@qq.com