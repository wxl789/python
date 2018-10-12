i = 12  # int
a = "abc"  # str
li1 = [1,2,3]  # list
# 查看变量类型
print(type(i))
print(type(a))
print(type(li1))

# 判断变量是否为某一数据类型,返回bool类型数据
# isinstance(变量,类型)
print(isinstance(i,list))

li2 = [1,2,[4,5,7],8]
for i in li2:
    # 判断类型
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(i)

# set   函数
