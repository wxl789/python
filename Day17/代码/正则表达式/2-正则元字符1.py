'''
.     : 匹配除换行符以外的所有字符
[123] : []代表集合，匹配[]里面的任意一个字符
[a-z] : 匹配小写字母  [abcdefg....xyz]
[A-Z] : 匹配大写字母  [ABCD...XYZ]
[0-9] : 匹配数字   [0123456789]
[a-zA-Z] ： 匹配任意一个字母  [a-zA-Z]  [A-Za-z]
[a-zA-Z0-9] : 匹配任意一个字母及数字
[a-zA-Z0-9]  [0-9A-Za-z]

[^0-9] : 匹配数字以外的字符
[^a-z] : 匹配小写字母以外的字符

\d  : 匹配数字   效果等同于[0-9]
\D  : 匹配数字以外的字符  效果等同于[^0-9]

\w : 匹配数字、字母及下划线  效果等同于[0-9a-zA-Z_]
\W : 匹配数字、字母及下划线以外的其他字符  效果等同于[^0-9a-zA-Z_]

\s : 匹配任意空白字符  空格、换行、换页、制表、回车   效果等同于[ \n\f\t\r]
\S : 匹配任意非空白字符  效果等同于[^ \n\f\t\r]

出现在中括号中的最前面的^称为脱字符，表示不匹配集合中的内容。
出现在中括号中其他位置的^就是普通字符。

r\R:保留原始字符的符号在正则中无效

'''
import re
print(re.findall(".", "a1#\nt"))
print(re.findall("[1ab]", "123avcdf"))
print(re.findall("[a-z]", "qweREWty1234!@#$"))
print(re.findall("[A-Z]", "qweREWty1234!@#$"))
print(re.findall("[0-9]", "qweREWty1234!@#$"))
print(re.findall("[a-zA-Z]", "qweREWty1234!@#$"))
print(re.findall("[a-zA-Z0-9]", "qweREWty1234!@#$"))
print(re.findall("[0-9a-zA-Z]", "qweREWty1234!@#$"))
print(re.findall("[0-9A-Za-z]", "qweREWty1234!@#$"))
print(re.findall("[^0-9]", "qweREWty1234!@#$"))
print(re.findall("[^adf]", "abcdef"))
print(re.findall("[\^]", "abcd^^ef"))
print(re.findall("[ab^c]", "abcd^^ef"))
print(re.findall("\d", "qweREWty1234!@#$"))
print(re.findall("\D", "qweREWty1234!@#$"))
print(re.findall(r"\d", "q\nweREWty1234!@#$"))
print(re.findall("\w", "q\nweREWty1234!_@#$"))
print(re.findall("[a-zA-Z0-9_]", "q\nweREWty1234!_@#$"))
print(re.findall("\W", "q\nweREWty1234!_@#$"))
print(re.findall("\s", "ac\n a\r \t"))
print(re.findall("\S", "ac\n a\r \t"))


