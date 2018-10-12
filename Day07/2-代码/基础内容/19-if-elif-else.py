# if-elif-else
'''
语法格式：
if 条件1:
    语句1
[elif 条件2:
    语句2
elif 条件3:
    语句3
elif 条件n:
    语句n
]
[else:
    语句n+1]
'''
'''
逻辑：当程序执行到if语句时，判断条件1是否成立，成立执行语句1，不成立
判断条件2是否成立，成立执行语句2，不成立继续向下判断条件3，依次类推。
当所有条件不成立时，如果有else语句，则执行else后面的语句，没有else语句，
则结束整个if判断，向下继续执行程序。
'''
# 从控制台输入
# 班级   2000-2008   一年级
# 2009-2015   小学
# 2016-2022   中学
# 2023-2027   大学
# 2028   研究生
'''
year = int(input("请输入年份："))
if year>=2000 and year<=2008:
    print("一年级")
elif year>=2009 and year<=2015:
    print("小学")
elif year >= 2016 and year <= 2022:
    print("中学")
elif year>=2023 and year<=2027:
    print("大学")
else:
    print("研究生")

'''
year = int(input("请输入年份："))
# 班级   2000-2008   一年级
# 2009-2015   小学
# 2016-2022   中学
# 2023-2027   大学
# 2028   研究生
if year > 2027:
    print("研究生")
elif year >= 2023:
    print("大学")
elif year >= 2016:
    print("中学")
elif year>=2009:
    print("小学")
elif year>=2000:
    print("一年级")
else:
    print("未出生")

# 2009
if year>2000:
    print(12)
if year>2007:
    print(34)



