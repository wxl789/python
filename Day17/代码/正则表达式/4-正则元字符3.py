'''
x?  : ?代表0个或1个x字符   非贪婪匹配
x+  : +代表至少1个x字符     贪婪匹配
x*  : *代表任意多个x字符    贪婪匹配

n、m为正整数
x{n}    : 匹配n个x字符
x{n,}   : 匹配至少n个x字符
x{n, m} : 匹配至少n个，最多m个x字符

x|y  : 匹配x或y字符   |：代表或
(abc) : 匹配小括号中的字符   将abc作为一个整体使用
(): 还有一个组的含义

'''
import re
print(re.findall("a?", "abbaabaaac"))
print(re.findall("a+", "abbaabaaac"))
print(re.findall("a*", "abbaabaaac"))

print(re.findall("ab+", "abbaabaaac"))
print("-----------------------")
print(re.findall("a{3}", "aabbaaabbaaaaabaaaaaa"))
print(re.findall("a{3,}", "aabbaaabbaaaaabaaaaaa"))
print(re.findall("a{3,5}", "aabbaaabbaaaaabaaaaaa"))

print(re.findall("a|b", "bsvcdf"))
print(re.findall("Nice|nice", "nice Nice NICE"))

print(re.findall("[abc]", "abcdefabcd"))
print(re.findall("(abc)", "abcdefabcd"))
print(re.findall("((N|n)ice)", "nice Nice NICE"))

