'''
# 1、拆分字符串：
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1
# &tn=baidu&rsv_pq=d87daf&rqlang=cn
# 拆分的结论为：
# {"ie":"utf-8", "f":"8", "rsv_bp":"0", "rsv_idx":"1", "tn":"baidu",
# "rsv_pq":"d87daf", "rqlang":"cn"}
str1 = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&rsv_pq=d87daf&rqlang=cn"
print(str1.find("?"))
str2 = str1[24:]
list1 = str2.split("&")
print(list1)
dict1 = {}
a = " "
for i in range(len(list1)):
    a = list1[i].split("=")
    dict1[a[0]]=a[1]
print(dict1)
'''
# 1.简述普通参数、关键字参数、默认参数、可变长参数的区别
# 2.写函数，计算传入字符串中[数字]、[字母]、[空格] 以及
# [其他]的个数
# 3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
# 4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个
# 元素是否含有空内容(空字符串、元素个数为0等)。
# 5.定义一个函数，输入不定个数的数字，返回所有数字的和
'''
'''
# 2、写函数，计算传入字符串中[数字]、[字母]、[空格] 以及[其他]的个数
# def checkCount(data):
#     num = 0
#     zimu = 0
#     kongge = 0
#     other = 0
#     for i in str1:
#         if isinstance(data.int):
# /            num +=1
#         elif:
#      /       isinstance(data.list)
#             zimu += 1

# 3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
def checkN(date):
    if 5 <= len(date):
        print("y")
    else:
        print("n")

checkN("sdfdfgdgd")
checkN([1,2,3])
checkN([1,2,3,4,5,65])
checkN((1,2,3))
checkN((1,2,3,4,5,6,7,8,9,0))
checkN({1:2,3:4,5:6})
checkN({1:2,3:4,5:6,7:8,9:0})