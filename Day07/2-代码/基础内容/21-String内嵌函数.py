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

# 10、返回字符串中最大字母或最小字母,比较的是ASCII的值
str11 = "Aasdfghjoiuytrcvbnmz"
# max() 返回最大的字母
print(max(str11))   # z
# min() 返回最小的字母
print(min(str11))   # a

# 11、截掉指定位置的指定元素
str12 = "      MM is Girl       "
str13 = "########GG is Boy##########"
print(str12)
print(str13)
# string.lstrip([str])   截掉字符串string左边位置的指定的字符str元素，
# 默认str为空格
print(str12.lstrip())
print(str13.lstrip("#"))

# string.rstrip([str])   截掉字符串string右边位置的指定的字符str元素，
# 默认str为空格
print(str12.rstrip())
print(str13.rstrip("#"))

# string.strip([str])   截掉字符串string左边及右边位置的指定的字符str元素，
# 默认str为空格
print(str12.strip())
print(str13.strip("#"))

# 12、替换字符串
# str.replace(old,new [,count])  将str中的old子串替换为new子串，默认
# 全部替换，如果指定count，则替换count个
str14 = "nice good nicegood handsome good handsome"
print(str14)
print(str14.replace("good", "bad"))
print(str14.replace("good", "bad", 6))

# str.maketrans("noi", "abc")   创建映射表
# 创建映射表方式一
# 第一个参数代表原本的字符，第二个为替换的字符
# 注：两个参数的字符个数要求一致
t = str.maketrans("noixyz", "abc123")
print(str14.translate(t))
# 创建映射表方式二
# 只写一个参数：参数类型为字典类型  {key : value}
# key:为原始字符   value：为替换的字符
t2 = str.maketrans({"n" : "a", "o" : "b"})

# string.translate(t)  : 根据映射表中的要求替换string中的字符
print(str14.translate(t2))


# 13、用于判断的函数
# 13.1、isalpha()  判断字符串中至少有一个字符，并且所有字符都是字母
# print("abc".isalpha())  # T
# print("abc123".isalpha())  # F
# print("".isalpha())   # F

# 13.2、isalnum() 判断字符串中至少有一个字符，并且所有字符都是数字或字母
# print("".isalnum())   # F
# print("123".isalnum())  # T
# print("abc".isalnum())  # T
# print("12as".isalnum())  # T
# print("12#$".isalnum())  # F

# 13.3、isdigit() 判断字符串中至少有一个字符，并且所有字符都是数字
# print("123".isdigit())  # T
# print("abc123".isdigit())  # F
# print("".isdigit())  # F

# 13.4、isspace() 判断字符串中至少有一个字符，并且所有字符都是空格
# print("    ".isspace())  # T
# print("  abc  ".isspace())  # F

# 13.5、isupper()  判断字符串中至少有一个区分大小写的字符，
# 并且所有区分大小写的字符都是大写
# print("".isupper())   # F
# print("ABC123".isupper())   # T
# print("acAA".isupper())   # F

# 13.6、islower()  判断字符串中至少有一个区分大小写的字符，
# 并且所有区分大小写的字符都是小写
# print("abc12".islower())  # T
# print("124".islower())   # F
# print("acSD".islower())   # F

# 13.7、istitle()  判断字符串中至少有一个区分大小写的字符，
# 并且所有字符都是标题化字符,单词的首字母大写
# print("Ass Wdf".istitle())  # T
# print("Ass edf".istitle())  # F

# 14、判断开头与结尾
# 14.1、string.startswith(str [,start, end])  判断string是否以str开头，
# 返回True或False，如果指定start与end，在该范围内判断。
str15 = "http://www.1000phone.com"
print(str15.startswith("http://"))   # T
print(str15.startswith("ttp"))  # F
print(str15.startswith("ttp", 1, 13))  # T
# 14.2、string.endswith(str [,start, end])  判断string是否以str结尾，
# 返回True或False，如果指定start与end，在该范围内判断。
print(str15.endswith("com"))  # T
print(str15.endswith(".con"))  # F


# 15、编码解码
str16 = "MM123好人"
print(str16)
# python3.X 默认为utf-8编码 utf-8可以支持解析汉字
# 15.1、编码  string.encode(encoding)  以encoding方式对string进行编码
print(str16.encode("utf-8"))
print(str16.encode("GBK"))

# 15.2、解码  string.decode(encoding)  以encoding方式对string进行解码
# 以什么方式编码,以什么方式解码
strUTF = str16.encode("GBK")
print(strUTF.decode("GBK"))


