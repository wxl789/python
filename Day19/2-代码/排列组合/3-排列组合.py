
#

import itertools
import time

pro = itertools.product([1,2,3,4], repeat=3)
print(pro)
print(list(pro))

# 数字  大写字母  小写字母  _     6-18位
pro1 = itertools.product(["0","1","2","3","4","a","z","A","Z","_"], repeat=6)
# list1 = list(pro1)
# for i in list1:
#     time.sleep(1)
#     str1 = "".join(i)
#     print(str1)

pro2 = itertools.product([1,2,3], [4,5,6])
print(list(pro2))



