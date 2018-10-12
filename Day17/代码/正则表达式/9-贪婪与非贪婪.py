'''
. : 匹配除换行符以外的所有字符  贪婪
* ：任意多个    贪婪
? : 0个或1个    非贪婪

.*?  : 将贪婪匹配变为非贪婪匹配
'''
import re
re1 = "ni .* hao"
str1 = "ni jintian hao ni mingtian hao ni houtian hao"
resu1 = re.findall(re1, str1)
print(resu1)

re2 = "ni .*? hao"
str2 = "ni jintian hao ni mingtian hao ni houtian hao ni  hao"
resu2 = re.findall(re2, str2)
print(resu2)

# https://www.cnblogs.com/fozero/p/7868687.html
