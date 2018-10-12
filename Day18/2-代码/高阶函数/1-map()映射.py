# map()  映射
# map():映射，将函数依次作用于传入的序列的每个元素。
# map():将结果作为新的对象返回。

# 格式：map(func, iter1[, iter2,iter3.....])
# 当有一个函数，只有一个iter时：函数只有一个形参
# 当有一个函数，有多个iter时：函数会依次作用于每个序列的相同位置的元素
# 注：当有多个列表时，并且列表的元素个数不同时，以最短的列表为基准。

# 简化的循环的代码

def func1(x):
    return x**2
res = map(func1, [1, 2, 3, 4])
print(res)
print(list(res))  # [1, 4, 9, 16]

def func2(x,y):
    return x+y
res2 = map(func2, [1,2,3,4], [5,6,7,8])
print(list(res2))

def func3(x,y):
    return x+y
res3 = map(func3, [1,2], [5,6,7,8])
print(list(res3))


# [1,2,3,4]
# ["a", "b", "c", "d" ]
def func4(x):
    # asc
    dict1 = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}
    return dict1[x]
res4 = map(func4, [1,2,3,4,1,2])
print(list(res4))







