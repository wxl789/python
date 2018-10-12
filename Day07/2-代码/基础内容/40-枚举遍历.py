list1 = [1,2,3,4]
# 枚举遍历
# 将index及对应的数据依次遍历
for i in enumerate(list1):
    print(i)

# index:代表下标   i:代表下标对应的数据
for index,i in enumerate(list1):
    print(index, i)

# tuple
tuple1 = (100,200,300)
for index,data in enumerate(tuple1):
    print(index,data)

# set
set1 = set([33,44,55])
for index,data in enumerate(set1):
    print(index,data)

# dict
dict1 = {"a":1,"b":2}
for index,data in enumerate(dict1):
    print(index,data,dict1[data])





