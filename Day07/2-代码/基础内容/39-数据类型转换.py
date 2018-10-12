# list -> set
set1 = set([1,2,3])
# tuple -> set
set2 = set((1,2,3))
# set -> list
list1 = list(set1)
print(set1)
print(list1)
# set -> tuple
tuple1 = tuple(set1)
print(tuple1)
# list -> tuple
tuple2 = tuple(list1)
# tuple -> list
list2 = list(tuple1)

# 将list中重复的数据删除
list3 = [1,2,3,4,3,2,1,6,6,6]
set3 = set(list3)
print(list3)
list4 = list(set3)
print(list4)




