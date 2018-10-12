'''
正则中存在组的概念：以()提取组。
提取规则：从左向右、从外向里
注：系统默认将整个正则表达式作为第一组
'''
import re
# 判断格式  xxx-xxxxxxxx   x:代表任意数字
re1 = "^\d{3}-\d{8}$"
print(re.findall(re1,"123-12345678"))

re2 = "^(\d{3})-(\d{8})$"
print(re.findall(re2,"123-12345678"))

# 获取正则的组
re3 = "^(\d{3})-(\d{8})$"
result1 = re.match(re3,"123-12345678")
print(result1)
# groups(): 获取所有的分组情况
print(result1.groups())
# group() : 获取单个分组的情况
# group(0) : 永远代表匹配到的整体字符串
# 注：系统默认将整个正则表达式作为第一组
print(result1.group())
print(result1.group(0))
print(result1.group(1))
print(result1.group(2))

# 0  ==> ^(\d{3})-(\d{8})$
# 1 ==>  (\d{3})
# 2 ==> (\d{8})

re4 = "^(((\w{1})(\w{1}))\.((\d{3})@(\w{2})))((\.)(com))$"
result2 = re.match(re4, "ab.123@qq.com")
'''
0：ab.123@qq.com
1：ab.123@qq
2：ab
3：a
4: b
5:123@qq
6:123
7:qq
8:.com
9:.
10:com

'''
print("---------------------")
print(result2.group(0))
print(result2.group(1))
print(result2.group(2))
print(result2.group(3))
print(result2.group(4))
print(result2.group(5))
print(result2.group(6))
print(result2.group(7))
print(result2.group(8))
print(result2.group(9))
print(result2.group(10))


re5 = "^(?P<love>\d{3})-(?P<like>\d{8})$"
# 给组起名称
# 语法格式：(?P<名称>正则)
# ?P<名称>  ： 不参与正则的规则判断
result5 = re.match(re5, "123-12345678")
print(result5.group(0))
print(result5.group(1))
print(result5.group(2))
print(result5.group("like"))







