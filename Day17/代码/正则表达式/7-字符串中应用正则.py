import re

str1 = "a b  c   d"
resu1 = str1.split(" ")
print(resu1)
# 1、使用正则切割字符串
resu2 = re.split(" +", str1)
print(resu2)


str2 = "a b  c   d"
print(str2.replace(" ", "*"))
# a*b**c***d
# 2、使用正则替换字符串
# re.sub(pattern, repl, string[, count])
'''
pattern:正则表达式
repl：新的字符
string：替换的原字符串
count:替换次数
'''
resu3 = re.sub(" +", "*", str2)
print(resu3)
resu4 = re.sub(" +", "*", str2, count=2)
print(resu4)







