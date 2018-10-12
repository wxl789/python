'''
^ : 匹配行首  出现在中括号外  写在正则表达式的开始位置
$ : 匹配行尾  出现在中括号外  写在正则表达式的末尾位置
如果需要进行多行匹配，需要设置flags=re.M；如果没有flags=re.M，默认
只匹配一行。

\A : 匹配行首,与^的区别：\A只匹配字符串的开头，即时设置flags=re.M，
    也不会匹配其他行。
\Z : 匹配行尾，与$的区别：\Z只匹配字符串的结尾，即时设置flags=re.M，
    也不会匹配其他行。

\b : 匹配字符边界，匹配字符后面是否为空格
nice to you     ce\b  nice
nicera to you     ce\b  匹配失败
\B : 匹配非字符边界

\b本身为转义字符，如果需要使用正则中的含义，使用r将转义字符的含义去掉，
保留正则的含义。

'''
import re
print(re.findall("^nice", "nice you\nnice to you"))
print(re.findall("^nice", "to nice you\nnice to you"))
print(re.findall("^nice", "nice you\nnice to you", flags=re.M))

print(re.findall("you$", "nice you\nnice to you"))
print(re.findall("you$", "nice you\nnice to youoo"))
print(re.findall("you$", "nice you\nnice to you", re.M))

print("----------------------------")
print(re.findall("\Anice", "nice you\nnice to you"))
print(re.findall("\Anice", "to nice you\nnice to you"))
print(re.findall("\Anice", "nice you\nnice to you", flags=re.M))

print(re.findall("you\Z", "nice you\nnice to you"))
print(re.findall("you\Z", "nice you\nnice to youoo"))
print(re.findall("you\Z", "nice you\nnice to you", re.M))

print("*************************")
print(re.findall(r"ce\b", "nice you nice to you"))
print(re.findall(r"ce\b", "nicer you niceo to you"))

print(re.findall(r"ce\B", "nice you nice to you"))
print(re.findall(r"ce\B", "nicer you niceo to you"))

print(re.findall(r"\Babc\B", "qweabciu ry abcyu qweabc oiu"))
print(re.findall(r"\babc\B", "qweabciu ry abcyu qweabc oiu"))
print(re.findall(r"\Babc\b", "qweabciu ry abcyu qweabc oiu"))
