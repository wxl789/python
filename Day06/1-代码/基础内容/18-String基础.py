'''
python中字符串是以 单引号 ' 或 双引号 " 引起来的任意的一个或
多个字符，如：'abc' 、"abc"
引号要求成对出现。
注：单引号或双引号只是表现形式，不属于字符串的一部分。
注：字符串是不可变的。
注：python中没有字符的概念，都是字符串。
'''
# 一、创建一个字符串
str1 = "窗前"
str2 = '没人'
print(str1)
print(str2)
print("str2")
print(type(str1))  # str
print(type(str2))  # str
str3 = 'a'
print(type(str3))  # str
# 输出一个单引号
str4 = "'"
print(str4)
# 输出一个双引号
str5 = '"'
print(str5)

# 二、字符串的运算
print(1 + 2)  # 加法
# 1、字符串拼接：将加号两边的字符串拼接到一起
str6 = "中国哟"
str7 = "母亲"
print(str6 + str7)

num1 = 20
str8 = "年龄为"
# 注：python中的字符串不能直接与数字类型进行拼接，需要将整型转为
# 字符串
# print(str8 + num1)  # TypeError: must be str, not int
print(str8 + str(num1))

# 2、重复输出字符串  *
print(str8*3)

# 3、通过索引/下标获取字符串中的某一个字符
# 语法格式： 字符串[索引]
# 注：索引/下标/index：从0开始
str9 = "我的愿望是好有钱"
print(str9[0])
print(str9[7])
# 注：在python中索引不能越界，越界会提示out of range错误
# print(str9[8]) # IndexError: string index out of range

# 获取最后一个字符
print(str9[len(str9) - 1])

# 索引可以写负数,负数代表从右向左查，
# -1：代表最后一个字符
print(str9[-1])

# 4、获取字符串长度  len(str)
print(len(str9))

print("-------华丽的分割线---------")
# 5、字符串是不可变的
str10 = "hello"
# 更改字符串中的字符或报错
# TypeError: 'str' object does not support item assignment
# str10[0] = "a"
print(str10)
# 更改变量的值，不会报错
str10 = "world"
print(str10)


# 6、截取字符串，会产生一个新的字符串，对原数据无影响
str11 = "我的愿望是世界和平以及目标是一夜暴富"
# 语法格式：字符串[[起始下标start]:[结束下标stop][:][递增基数step]]
'''
说明：
start：截取字符串的起始位置（包含），可以省略该参数，默认值为0
stop：截取字符串的结束位置（不包含），可以省略该参数，默认值为长度
step：步长，间隔数，默认值为1,可以写负数， -1：从右向左截取
'''
print(str11)
# 截取字符串的某一范围
str12 = str11[2:5]
print(str12)
# 从0开始截取，截取到下标5（不包含）
str13 = str11[:5]
print(str13)
# 从5开始截取，截取到末尾
str14 = str11[5:]
print(str14)
# 获取所有字符
str15 = str11[:]
str20 = str11[::]
print(str15)
# 可以写负数
str16 = str11[-4:-1]
print(str16)
# 递增基数
str17 = str11[::2]
print(str17)
# 反转字符串
str18 = str11[::-1]
print(str18)

# 从右向左查，起始下标比结束下标大
str19 = str11[5:2:-1]
print(str19)

print(str11)

# 7、判断原字符串中是否含有子字符串  in  not in
print("世界" in str11)  # T
print("故宫" in str11)  # F

# 8、格式化字符串
name = "lily"
age = 12
weight = 54.3
print("姓名是：",name,"，年龄是：",age,",体重是：",weight,"kg")
print("姓名是："+name+"，年龄是："+str(age)+",体重是："+str(weight)+"kg")
'''
格式化字符串语法格式：
字符串(字符串中包含格式化字符) % (格式化字符对应的数据)
%s : 可以作为字符串、整型、浮点型的占位符
%d : 可以作为整型、浮点型的占位符，如果作为浮点型占位符，默认保留整数部分
%f : 可以作为整型、浮点型的占位符，默认保留六位小数， %f可以写成
    %.nf格式，n代表保留的小数位数。
'''
print("姓名是：%s，年龄是：%d,体重是：%.1fkg"%(name, age, weight))
# 只有一个占位符,小括号可以省略
print("姓名是%s" % name)
# 当有多个占位符,小括号不可以省略，小括号代表元组类型数据，不同元素用 , 隔开
print("姓名是：%s，年龄是：%d,体重是：%.1fkg"% (name, age, weight))

f1 = 2.45
#  2.45%
print("%")
print("%%")
print("2.45%")
# 当字符串中出现格式化字符时，要求%后面有其他字符， 两个%%，输出一个%
print("%s%%"%(f1))

print("------------------------")
# 9、转义字符
# \(将原本无意义的字符转换为有意义的字符；将原本有意义的字符转换为无意义的字符)
# 9.1、\n  ---> 换行
print("abc\ndef")
print("**********************")
# 可以用多行注释的方式换行打印文本内容不过
print('''鹅鹅鹅
        曲项向天歌
        白毛浮绿水''')
# 9.2、 \'  ---> '   单引号
print('I\'m a')
# 9.3、\" ---> "     双引号
print("\"")
print("\"\"")
# 9.4、\\  ---> \    一个斜线
print("C:\\Users\\xlg\\Desktop")
# C:\Users\xlg\Desktop

# 9.5、保留原始字符串，不转义
# r / R ： 将所有转义的字符作为普通字符使用，不转义
print(r"\\\\\\\\")
print("\n")
print(r"\n")
print(R"\n")
print(r"C:\Users\xlg\Desktop")
print("C:\An\的\A")
# a b x 0 o r n t



