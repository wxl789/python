# filter:作用：对序列中的元素进行筛选过滤

# 格式：filter(func, iter)
# func返回值为True或False，当函数返回True，代表保留该元素；
# 当函数返回False，代表删除该元素。

# filter的返回值为一个新的序列，返回的列表中的元素类型与原列表中的元素
# 类型一致。
list1 = [1,2,3,4,5,6,7]
def func(num):
    # 保留偶数
    if num % 2 == 0:
        return True
    # 奇数
    return False
res1 = filter(func, list1)
print(res1)
print(list(res1))


