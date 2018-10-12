# 1、拆分字符串：
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1
# &tn=baidu&rsv_pq=d87daf&rqlang=cn
# 拆分的结论为：
# {"ie":"utf-8", "f":"8", "rsv_bp":"0", "rsv_idx":"1", "tn":"baidu",
# "rsv_pq":"d87daf", "rqlang":"cn"}
'''
def checkUrl(strUrl):
    print(strUrl)
    # 1、以？拆分字符串，只取用第二个元素
    list1 = strUrl.split("?")
    # print(list1[1])
    str1 = list1[1]  # ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&rsv_pq=d87daf&rqlang=cn
    list2 = str1.split("&")
    dict1 = {}  # 存放key-value
    for i in list2:
        list3 = i.split("=")
        dict1[list3[0]] = list3[1]
    return dict1

str1 = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&rsv_pq=d87daf&rqlang=cn"
dict1 = checkUrl(str1)
print(dict1)
'''




'''
1.简述普通参数、关键字参数、默认参数、可变长参数的区别
2.写函数，计算传入字符串中[数字]、[字母]、[空格] 以及
[其他]的个数
3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个
元素是否含有空内容(空字符串、元素个数为0等)。
5.定义一个函数，输入不定个数的数字，返回所有数字的和
'''
# 2.写函数，计算传入字符串中[数字]、[字母]、[空格] 以及[其他]的个数
'''
def checkCount(str1):
    # 默认所有字符个数均为0
    numCount = 0
    wordCount = 0
    spaceCount = 0
    otherCount = 0
    for i in str1:
        if i == " ":
            spaceCount += 1
        elif (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            wordCount += 1
        elif i >= "0" and i <= "9":
            numCount += 1
        else:
            otherCount += 1
    print(numCount, wordCount, spaceCount, otherCount)

strInput = input("请输入字符串：")
checkCount(strInput)
'''

# 3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
'''
def check(data):
    # 当前只判断了int，自己添加float等类型
    if isinstance(data,int):
        return 2
    else:
        if len(data) > 5:
            return 1
        else:
            return 0
res = check(123)
if res==1:
    print(">>>>>>")
elif res == 2:
    print("int")
else:
    print("<<<<<<")
'''
# 4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容(空字符串、元素个数为0等)。
def countZero(data):
    if isinstance(data,str):
        if len(data)==0:
            print("空字符串")
        else:
            print("字符串")
    if isinstance(data,list):
        # for
        if len(data)==0:
            print("空list")
        else:
            print("list")
    if isinstance(data,tuple):
        if len(data)==0:
            print("空tuple")
        else:
            print("tuple")

countZero([1,2])

# 5.定义一个函数，输入不定个数的数字，返回所有数字的和
'''
def sum1(*args):
    res = 0
    for i in args:
        res += i
    return res
print(sum1(1,2,3,4))
'''



'''
学生信息管理：
用一个列表存储所有学员信息：学员信息如下：姓名name、年龄age、年级grade、
成绩score(成绩默认60)

1、打印所有学员信息
2、新增一个学员信息
3、计算所有学员年龄的和
4、将所有学员的年龄及年级加1
5、将所有学员成绩置为0，并打印所有学员信息
6、通过年龄对学员排序，可以设置升序或降序，并打印所有学员信息  (选作)
(选择排序   冒泡排序  快速排序   插入排序)
百度  排序方式  自学
'''
dict1 ={"name":"张三", "age":20, "grade":11, "score":60}
dict2 ={"name":"李四", "age":21, "grade":11, "score":60}
dict3 ={"name":"王五", "age":22, "grade":11, "score":60}
list1 = [dict1,dict2]
# 1、
# print(list1)
def stu(list):
    print(list)
stu(list1)
# 2、新增一个学员信息
list1.append(dict3)
stu(list1)
# 3、计算所有学员年龄的和

def sumAge9():
    sum2 = 0
    for i in list1:
        pass
        # print(i.get("age"))
        sum2 += (i.get("age"))
    return sum2
print(sumAge9())
# 4、将所有学员的年龄及年级加1
for i in range(len(list1)):
    list1[i].get("grade")==(list1[i].get("grade"))+1
    print()






'''
学员信息用什么保存  
'''
'''
[{name:lily,age:12,grade:1,score:34},{}]
'''


#
# def Sum1(num1,num2):
#     print(num1+num2)
#     return "wwww"
# a = Sum1(1,2)
# print(a)

def fun1(*args):
    print(args)
fun1()
fun1(1)
fun1(1,2,3)















