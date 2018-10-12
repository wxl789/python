# 字符串内嵌函数
# 1、eval(str) : 将str中有效的表达式进行计算，并输出结果
print(eval("123"))  # --> 123
print(eval("+123"))
print(eval("-123"))
print(eval("1 + 2"))  # ---> 1+2  --> 3
# print(eval("abc"))
print(type(eval("123")))   # int

# 2、len(str) : 获取字符串长度
str1 = "abcdef"
print(len(str1))  # 6

# 3、字母大小写转换:对原字符串无影响，会产生一个新的字符串
str2 = "abCdEf sW Pt wen"
# lower() 将所有字母小写
print(str2.lower())
# upper()  将所有字母大写
print(str2.upper())
# swapcase()  将原字符串中的小写字母转为大写，大写字母转为小写
print(str2.swapcase())
# capitalize()  将首字母大写，其他小写
print(str2.capitalize())
# title()   将每个单词的首字母大写，其他小写
str3 = str2.title()
print(str3)

# 4、返回指定长度及指定前后符号的字符串,对原字符串无影响，会产生一个新的字符串
str4 = "pyc"
# str.center(width [,fillchar]) 返回指定长度width的字符串，str在中
# 间，其他位置用fillchar补全，默认fillchar为空格
print(str4.center(15, "*"))
# str.ljust(width [,fillchar]) 返回指定长度width的字符串，str在左
# 边，其他位置用fillchar补全，默认fillchar为空格
print(str4.ljust(15, "*"))
# str.rjust(width [,fillchar]) 返回指定长度width的字符串，str在右
# 边，其他位置用fillchar补全，默认fillchar为空格
print(str4.rjust(15, "*"))
# str.zfill(width) 返回指定长度width的字符串，str在右
# 边，其他位置用0补全
print(str4.zfill(15))

# 5、检测原字符串中是否含有某一个子字符串
str5 = "good good study, day day up"
# str.find(string [, begin, end]):检测str中是否存在string，如果存在，
# 返回第一次找到的下标，如果指定begin与end，在该范围内查找；如果找
# 不到，返回-1。
# 从左向右查找
print(str5.find("d"))
print(str5.find("year"))
print(str5.find("day",18, 26))
# str.rfind(string [, begin, end]):检测str中是否存在string，如果存在，
# 返回第一次找到的下标，如果指定begin与end，在该范围内查找；如果找
# 不到，返回-1。
# 从右向左查找
print(str5.rfind("d"))

# str.index(string [, begin, end]):检测str中是否存在string，如果存在，
# 返回第一次找到的下标，如果指定begin与end，在该范围内查找；如果找
# 不到，报错ValueError: substring not found。
# 从左向右查找
print(str5.index("day"))
# print(str5.index("year"))

# str.rindex(string [, begin, end]):检测str中是否存在string，如果存在，
# 返回第一次找到的下标，如果指定begin与end，在该范围内查找；如果找
# 不到，报错ValueError: substring not found。
# 从右向左查找
print(str5.rindex("day"))
# print(str5.rindex("year"))

# 6、检测原字符串中某一个子字符串出现的次数
# str.count(string [, begin, end]):检测str中string出现的次数，如果
# 指定begin与end，在该范围内查找。
print(str5.count("day"))
print(str5.count("day", 18, 24))

# 7、将字符转为ASCII，将ASCII转为字符
str6 = "A"
# ord(str)  将字符转为ASCII
print(ord(str6))   # 65
# chr(int)  将ASCII转为字符
print(chr(66))
# 汉字可以转为ASCII
print(ord("你"))
print(chr(20320))

# 8、切割字符串
str7 = "ni*hao*zai*jian"
# str.split(string [, count]) 以string切割str字符串，返回一个列表类型
# 的数据，列表中为切割之后的字符串。
# count:指定切割次数
print(str7.split("*"))
print(str7.split("*", 2))

# str.splitlines([boolean])  按照行切割字符串(\n  \r \n\r),以行为单位切割
# 字符串
# boolean: 如果值为True，有换行符；如果值为False，无换行符；
# 默认值为False
str8 = "abc\ndef\nghi"
str9 = """abc
def
ghi
jkl"""
print(str8)
print(str8.splitlines())
print(str9.splitlines())
print(str9.splitlines(False))
print(str9.splitlines(True))

# 9、链接字符串
# str.join(list) 将list列表中的字符串以str作为链接符拼接到一起
list1 = ["abc", "def", "ghi"]
str10 = "**"
print(str10.join(list1))
print(list1[0]+"**"+list1[1]+"**"+list1[2])





