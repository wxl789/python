# 1、[1,2,3,4,2,2,3,2,4,2]
# 清除列表中所有的数字2
list1 = [1,2,3,4,2,2,3,2,4,2,2,2,2,2,2,2,2]
'''for i in range(list1.count(2)):
    list1.remove(2)
print(list1)
'''

# 2、画一个表格对比string、list、tuple、dict、set的区别


# 3、查找字符串中所有的单词，及单词出现的次数
"Anti tracks is a complete solution to protect " \
"your privacy and enhance your PC performance. "
"With a simple click Anti tracks securely erase " \
"your internet tracks, computer activities and " \
"programs history information stored in many hidden " \
"files on your computer.Anti tracks support Internet " \
"Explorer, AOL, Netscape/Mozilla and Opera browsers. " \
"It also include more than 85 free plug-ins to extend " \
"erasing features to support popular programs such as" \
" ACDSee, Acrobat Reader, KaZaA, PowerDVD, WinZip, iMesh," \
" Winamp and much more. Also you can easily schedule " \
"erasing tasks at specific time intervals or at Windows " \
"stat-up shutdown.To ensure maximum privacy protection " \
"Anti tracks implements the US Department of "










'''
str1 = "Anti tracks is a complete solution to protect your privacy and enhance your PC performance." \
       "With a simple click Anti tracks securely eraseyour internet tracks," \
       " computer activities and programs history information stored in many hidden files on your computer." \
       "Anti tracks support Internet Explorer," \
       " AOL, Netscape/Mozilla and Opera browsers." \
       "It also include more than 85 free plug-ins to extenderasing" \
       " features to support popular programs such as ACDSee," \
       " Acrobat Reader, KaZaA, PowerDVD, WinZip, iMesh," \
       "Winamp and much more. Also you can easily schedule " \
       "erasing tasks at specific time intervals or at Windows " \
       "stat-up shutdown.To ensure maximum privacy protection " \
       "Anti tracks implements the US Department of"

str2 = str1.split(" ")
for i in str2:
    print(i,str2.count(i))

'''
'''
# 4、遍历列表（列表中的元素不一致）
list2 = [1,2,[3,4,5],"abc",(0,9,8),{"a":100,"b":200}]
# 1 2 3 4 5 abc 0 9 8 100 200
for i in list2:
    if isinstance(i,list):
        for j in i:
            print(j)
        else:
            continue
    if isinstance(i,tuple):
        for k in i:
            print(k)
        else:
            continue
    if isinstance(i,dict):
        for h in i.values():
            print(h)
        else:
            continue
    print(i)
'''