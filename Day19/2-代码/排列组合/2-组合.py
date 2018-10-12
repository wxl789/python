'''
从n个元素中取出m个元素作为一个组合。
组合的个数：n! / (m! * (n-m)!)
'''
import itertools

com = itertools.combinations([1,2,3,4], 2)
print(com)
print(list(com))


