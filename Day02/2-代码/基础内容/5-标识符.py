# 什么是标识符？就是一个不带引号的字符串
# 标识符作用：给文件、变量、常量、函数、类、对象等命名的
# 标识符命名规则：
# 1、只能包含数字、字母、下划线
# 2、不能以数字开头
# 3、不能是python中的关键字
# 4、见名知意
# 5、区分大小写

# 注：python3以后支持汉字，不建议过多使用

a = 30
A = 40
print(a)  # 30
print(A)   # 40

name = "lily"
name1 = "lucy"
# 1name = "c++"

_age = 12
a_b = 34
# a@b = 67
# class = 78

# 获取python中的关键字
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']  33个

# 仅作娱乐
中国 = "china"
print(中国)

# 年龄 -- 作用者 -- 原因
age = 45




