'''
sorted()  排序
格式：sorted(iter[, reverse][, key])
sorted：返回一个新的序列，可以根据key的条件进行排序。
reverse：值为True或False，默认升序，默认值为False。
key：函数类型的参数，函数只有一个形参。
'''

# list1 = [8,4,2,9,6]
# list1.sort(reverse=True)
# print(list1)

# 1、只有一个iter参数,默认升序
list1 = [8,4,2,9,6]
list2 = sorted(list1)
print(list1)
print(list2)
# 2、设置reverse参数
list3 = sorted(list1, reverse=True)  # 倒序
list4 = sorted(list1, reverse=False)  # 正序
print(list3)
print(list4)

# 3、设置key
list5 = [1,8,-9,3,-4,6,-7]
# 按照绝对值排序
def func1(num):
    if num < 0:
        return -num
    return num
# [1,8,-9,3,-4,6,-7]
# [1,8,9,3,4,6,7]  ==> [1,3,4,6,7,8,9]
list7 = sorted(list5, key=func1)
print(list7)
list8 = sorted(list5, key=func1, reverse=True)
print(list8)
# 使用系统的函数
list8 = sorted(list5, key=abs, reverse=True)
print(list8)

# 4、字符串默认使用ascii排序
list9 = ["b", "a", "bc", "cd", "ac"]
list10 = sorted(list9)
print(list10)

# 5、按字符串长度排序
list11 = ["bwer", "akjhg", "bcqwertyu", "cdpo", "ac"]
def func2(str1):
    return len(str1)  # [4,5,9,4,2]   ==> [2,4,4,5,9]
list12 = sorted(list11, key=func2)
print(list12)





