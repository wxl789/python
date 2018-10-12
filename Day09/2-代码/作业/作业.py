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
'''
学员信息用什么保存  
'''

# 设置初始学员信息及个数
# 姓名name、年龄age、年级grade、成绩score(成绩默认60)
stuList = [{"name":"无理","age":18,"grade":1,"score":78},
           {"name":"取闹","age":19,"grade":2,"score":90},
           {"name":"娇弱","age":20,"grade":3,"score":67}]
# 1、打印所有学员信息
def showAllStu():
    for stu in stuList:
        print("姓名是%s,年龄是%s,年级为%s,成绩为%s" % (stu["name"],
                                           stu["age"],stu["grade"],stu["score"]))
    print("********学员信息展示完毕**********")
showAllStu()
# 2、新增一个学员信息
def addNewStu(name,age,grade,score=60):
    stuList.append({"name": name,"age": age,"grade": grade,"score":score})
addNewStu(name="Lily",age=19,grade=2,score=100)
addNewStu(name="文宁",age=18,grade=1)
showAllStu()

# 3、计算所有学员年龄的和
def sumAge():
    count = 0
    for stu in stuList:
        count += stu["age"]
    print(count)
sumAge()


# 4、将所有学员的年龄及年级加1
def addAgeAndGrade():
    for stu in stuList:
        stu["age"] += 1
        stu["grade"] += 1
    showAllStu()
addAgeAndGrade()


# 5、将所有学员成绩置为0，并打印所有学员信息
def scoreToZero():
    for stu in stuList:
        stu["score"] = 0
scoreToZero()
showAllStu()


list1 = [6,0,3,45,87,1,4]
# 升序排序
# 冒泡排序
print(list1)
for i in range(0,len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
'''
6,0,3,45,87,1,4
i=0,j=1  0,6,3,45,87,1,4
i=0,j=2  0,6,3,45,87,1,4
i=0,j=6  0,6,3,45,87,1,4
i=1,j=2  0,3,6,45,87,1,4
i=1,j=3  0,3,6,45,87,1,4
i=1,j=4  0,3,6,45,87,1,4
i=1,j=5  0,1,6,45,87,3,4
i=1,j=6  0,1,6,45,87,3,4
i=2,j=3  0,1,
...
i=5,j=6  0,1,3,4,6,45,87

'''
# 6、通过年龄对学员排序，可以设置升序或降序，并打印所有学员信息  (选作)
def sortAge(up=True):
    for i in range(0,len(stuList) - 1):
        for j in range(i + 1, len(stuList)):
            if stuList[i]["age"] > stuList[j]["age"]:# 按年龄比较
                # 交换整个学员信息
                stuList[i],stuList[j] = stuList[j],stuList[i]
    # 按降序排
    if up == False:
        stuList.reverse()
    showAllStu()
sortAge()
sortAge(False)


