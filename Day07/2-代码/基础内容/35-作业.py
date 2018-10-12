# 1、[1,2,3,4,2,2,3,2,4,2]
# 清除列表中所有的数字2
list1 = [1,2,3,4,2,2,3,2,4,2,2,2,2,2,2,2,2]
# 判断有几个2，删除几次
'''
for i in range(list1.count(2)):
    list1.remove(2)
print(list1)
'''
# 类似复制一次list1，遍历并删除list1的元素2
'''
for i in list1[:]:
    if i==2:
        list1.remove(2)
print(list1)
'''
'''
for i in list2   [1,2,3,4,2,2,3,2,4,2,2,2,2,2,2,2,2]

'''

# 2、画一个表格对比string、list、tuple、dict、set的区别


# 3、查找字符串中所有的单词，及单词出现的次数
str1 = "Anti tracks is a complete solution to protect " \
"your privacy and enhance your PC performance. " \
"With a simple click Anti tracks securely erase " \
"your internet tracks, computer activities and " \
"programs history information stored in many hidden " \
"files on your computer.Anti tracks support Internet " \
"Explorer AOL Netscape/Mozilla and Opera browsers. " \
"It also include more than 85 free plug-ins to extend " \
"erasing features to support popular programs such as" \
" ACDSee, Acrobat Reader, KaZaA, PowerDVD, WinZip, iMesh," \
" Winamp and much more. Also you can easily schedule " \
"erasing tasks at specific time intervals or at Windows " \
"stat-up shutdown.To ensure maximum privacy protection " \
"Anti tracks implements the US Department of"

# 切割字符串
str1 = str1.replace(",", " ")
str1 = str1.replace(".", " ")
print(str1)
list2 = str1.split(" ")
# 创建空字典，用于存储单词及个数
dict1 = {}
for i in list2:
    # dict1[i] = list2.count(i)
    # 当前key不存在
    if dict1.get(i) == None:
        # 添加新的key，并赋值为1
        dict1[i] = 1
    else:
        dict1[i] += 1

print(dict1)




# 4、遍历列表（列表中的元素不一致）

list2 = [1,2,[3,4,5],"abc",(0,9,8),{"a":100,"b":200}]
for i in list2:
    if isinstance(i,list) or isinstance(i,tuple):
        for j in i:
            print(j)
    elif isinstance(i,dict):
        for k in i:
            print(i[k])
    else:
        print(i)

