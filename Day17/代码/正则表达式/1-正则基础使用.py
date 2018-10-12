# python1.5以后加入正则模块  re模块提供了正则的相关功能。
'''
正则表达式：是一些特殊字符组成的具有实际意义的字符串。
功能：1、判断某个字符串是否符合要求
'''
# 11  数字  1 131  155 156...  20
# 2

# 导入模块
import re
'''
1、re.match(pattern, string[, flags])
pattern:正则表达式
string：匹配的字符串
flags：标志位，设置特殊情况
      re.I：不区分大小写
      re.M：全局/多行匹配，会影响^及$
      re.S：匹配包括换行符等所有字符
功能：从头开始匹配字符串是否符合正则要求，符合返回一个特殊对象；
        不符合返回None。
'''
print(re.match("www", "www.1000phone.com"))
# "www" : 正则表达式
# <_sre.SRE_Match object; span=(0, 3)(下标位), match='www'(匹配成功的内容)>
print(re.match("www", "1000phone.www.com"))
print(re.match("www", "Www.1000phone.www.com"))
print(re.match("www", "Www.1000phone.www.com", re.I))
print(re.match("www", "1000phone.www.com", re.M))

'''
2、re.search(pattern, string[, flags])
pattern:正则表达式
string：匹配的字符串
flags：标志位，设置特殊情况
      re.I：不区分大小写
      re.M：全局/多行匹配，会影响^及$
      re.S：匹配包括换行符等所有字符
功能：匹配整个字符串中是否符合正则要求的子串，符合返回
第一个匹配到的对象；不符合返回None。
'''
print("----------------------------")
print(re.search("www", "www.100phone.com"))
print(re.search("www", "100phone.com"))
print(re.search("www", "100phone.www.com"))
print(re.search("www", "www.100phone.www.com"))
print(re.search("www", "WWW.100phone.com"))
print(re.search("www", "WWW.100phone.com", re.I))

# 获取到匹配成功的下标值
print(re.search("www", "WWW.100phone.com", re.I).span())

result1 = re.search("www", "WWW.100phone.com", re.I)
if result1 != None:
    print("符合要求")
else:
    print("不符合要求")


'''
3、re.findall(pattern, string[, flags])
pattern:正则表达式
string：匹配的字符串
flags：标志位，设置特殊情况
      re.I：不区分大小写
      re.M：全局/多行匹配，会影响^及$
      re.S：匹配包括换行符等所有字符
功能：匹配整个字符串中是否符合正则要求的子串，返回列表类型对象；
将符合要求的所有子串放到列表中，如果没有符合要求的子串返回[]。
'''
print("******************************")
print(re.findall("www", "www.1000phone.com"))
print(re.findall("www", "1000phone.com"))
print(re.findall("www", "www.www.1000phonewww.com"))
print(re.findall("www", "Www.www.1000phonewWw.com"))
print(re.findall("www", "Www.www.1000phonewWw.com", re.I))

result2 = re.findall("www", "Www.www.1000phonewWw.com", re.I)
if len(result2) != 0:
    print("有")
else:
    print("无")

'''
4、re.finditer(pattern, string[, flags])
pattern:正则表达式
string：匹配的字符串
flags：标志位，设置特殊情况
      re.I：不区分大小写
      re.M：全局/多行匹配，会影响^及$
      re.S：匹配包括换行符等所有字符
功能：匹配整个字符串中是否符合正则要求的子串，返回迭代器类型对象；
将符合要求的所有子串放到迭代器中，如果没有符合要求的子串返回一个
元素个数为0的迭代器。
'''

result3 = re.finditer("www", "www.baidi.www.Www", re.I)
result4 = re.finditer("www", "baidi", re.I)
# 将迭代类型转为列表类型
print(list(result3))
print(list(result4))















