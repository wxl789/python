import re
re1 = "^\d{3}$"
resu1 = re.match(re1, "123")
print(resu1)

'''
re.compile(pattern, flags)
pattern:正则表达式
flags：标志位，设置特殊情况
      re.I：不区分大小写
      re.M：全局/多行匹配，会影响^及$
      re.S：匹配包括换行符等所有字符
功能：编译正则表达式，用于直接匹配对象。
'''
re2 = "^\d{3}$"
com1 = re.compile(re2, re.I)
result2 = com1.match("345")
print(result2)






