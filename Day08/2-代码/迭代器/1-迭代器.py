# 迭代器
# iterable
'''
Iterable:可迭代对象
可以直接作用于for循环的对象，叫做可迭代对象(Iterable)。

可直接作用于for循环的对象：
1、基本数据类型：list、set、dict、tuple、string
2、generator生成器：带有yield关键字的生成器函数。

判断一个对象是否为可迭代对象：
isinstance(obj, Iterable)
'''
# Iterable   为集合类型中的一种数据类型
from collections import Iterable

# 判断一个对象是否为可迭代对象   []   ()  {}   str  100
print(isinstance([], Iterable))   # T
print(isinstance({}, Iterable))    # T
print(isinstance((), Iterable))    # T
print(isinstance("abc", Iterable))    # T
# int、float不是可迭代对象
print(isinstance(100, Iterable))   # F

print(isinstance((x for x in range(5)), Iterable))  # T
# x for x in range(n) --> 生成一个新的列表，列表的数量及值由range决定
# x for x in range(5) ===> [0,1,2,3,4]
'''
x for x in range(5):类似以下代码
list1 = []
for x in range(5):
    list1.append(x)
'''

print(x for x in range(5))


'''
迭代器： Iterator
不仅可以直接作用于for循环，也可以使用next() 函数不断调用并获取下
一个元素，直到取出最后一个元素，当获取最后一个元素的下一个元素时，
会返回一个StopIteration的错误。

可以使用next()函数调用并获取下一个元素的对象称为迭代器对象。

判断一个对象是否为迭代器对象：
isinstance(obj, Iterator)
'''

from collections import Iterator
print(isinstance([], Iterator))  # F
print(isinstance((), Iterator))    # F
print(isinstance({}, Iterator))   # F
print(isinstance("abc", Iterator))   # F
print(isinstance(100, Iterator))   # F
print(isinstance((x for x in range(5)), Iterator))   # T

list1 = (x for x in range(3))
print(list1)  # <generator object <genexpr> at 0x00000206DEF52048>
'''
for i in list1:
    print(i)
'''
# next(obj)   --> obj为迭代器对象，返回迭代器中的一个元素
print(next(list1))
print(next(list1))
print(next(list1))
# 返回StopIteration错误
# print(next(list1))   # StopIteration


# 将list、set、dict、tuple、str转为Iterator对象
# 语法格式：  iter(obj)
list2 = [1,2]
# print(next(list2))  # TypeError: 'list' object is not an iterator

list3 = iter([1,2])
print(next(list3))

print(isinstance(iter([]), Iterator))  # T
print(isinstance(iter(()), Iterator))  # T
print(isinstance(iter({}), Iterator))  # T
print(isinstance(iter("abc"), Iterator))  # T

print(isinstance(iter("abc"), Iterable))  # T

str1 = iter("abcdef")
# 下标向后移动
next(str1)  # a
next(str1)
print(next(str1))




