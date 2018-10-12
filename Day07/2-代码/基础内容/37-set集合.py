'''
set 集合
特点：1、无序的
      2、元素不重复的集合
set：可以认为是dict的key的集合
'''
# 一、创建
# 创建set需要将一个list或tuple或dict或string作为参数传入创建
# list
set1 = set([1,2,3,4,5])
print(set1)  # {1,2,3,4,5}
print(type(set1))  # set

# 重复的元素在set中直接被过滤，只保留一份
set2 = set([1,2,2,2,3,4,4,4,4])
print(set2)  # {1，2，3，4}

# tuple
set3 = set((1,2,3,4))
print(set3)
# dict   只保留字典的key
set4 = set({"a":1,"b":2,"c":4})
print(set4)  # {"a","b","c"}
# string
set5 = set("abcdefg")
print(set5)

# set的参数要求是集合类型参数
# set6 = set(100)
# print(set6)  # TypeError: 'int' object is not iterable

# 二、set是无序的，不支持下标
# TypeError: 'set' object does not support indexing
# print(set5[1])

print("**********************************")
# 三、增加数据
set7 = set([1,2,3])
print(set7)
# 1、set.add(obj) 添加数据，add添加数据时，只能添加不可变的数据类型的数据
set7.add(8)
print(set7)
set7.add(1)  # 可以重复添加数据，但无效果
print(set7)
set7.add("abc")
print(set7)
set7.add((1,2))
print(set7)
# 添加失败，add只能添加不可变的数据类型的数据，list属于可变类型数据
# set7.add([1,2,3])  # TypeError: unhashable type: 'list'
# print(set7)
# 添加失败，add只能添加不可变的数据类型的数据，dict属于可变类型数据
# set7.add({"a":1})  # TypeError: unhashable type: 'dict'
# print(set7)

# 2、set.update(iter) 添加数据，将iter集合中的元素打碎添加
# iter：string、list、tuple、dict
set8 = set([1,2,3])
print(set8)
# list
set8.update([100,200,300])
print(set8)
# tuple
set8.update((333,444))
print(set8)
# string
set8.update("abc")
print(set8)
# dict  只能添加key
set8.update({"qw":1,"rt":9})
print(set8)
# int  错误
# set8.update(100)  # TypeError: 'int' object is not iterable
# print(set8)

# 四、删除数据
# set.remove(ele)  当数据不存在时，删除会报错
set9 = set([1,2,3,4,5])
print(set9)
set9.remove(2)
print(set9)
# 当数据不存在时，删除会报错
# set9.remove(9)  # KeyError: 9
# print(set9)

# 五、遍历set
for i in set9:
    print(i)

# 六、集合的操作
set10 = set([1,2,3,4,5])
set11 = set([4,5,6,7,8])
# 1、& 交集
print(set10 & set11)
# 2、| 并集
print(set10 | set11)
# 3、^ 补集
print(set10 ^ set11)
# 4、- 差集
print(set10 - set11)
print(set11 - set10)



