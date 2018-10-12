'''
从n个元素中取出m个元素按照一定顺序排列。
当m等于n，叫做全排列。

排列的个数：n! / (n-m)!
'''
import itertools
per = itertools.permutations([1,2,3,4], 2)
print(per)
print(list(per))

