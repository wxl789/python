import re
# 判断一个字符串是不是11位的数字，第一个数字为1
'''
^1 ==> 以1开头
\d{10} ==> 10个数字
\d{10}$  ==> 以10个数字结尾
'''
re1 = "^1\d{10}$"
print(re.findall(re1, "13456789000"))

# 判断格式  xxx-xxxxxxxx   x:代表任意数字
re2 = "^\d{3}-\d{8}$"
print(re.findall(re2, "789-00000000"))

# 判断qq邮箱   123456@qq.com
# . ^ $ 在正则中存在实际意义，如果将该符号作为普通字符使用，需要使用 \
# 将其转为普通字符。

re3 = "^\d{6}@qq\.com"
print(re.findall(re3, "123456@qq.com"))
print(re.findall(re3, "123456@qqacom"))

# 1.1$
re4 = "^\d{1}\.\d{1}\$$"
print(re.findall(re4, "1.1$"))
print(re.findall(re4, "1.1"))

