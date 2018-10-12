# 遍历列表
list1 = [1,2,3,4]
for i in list1:
    print(i)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# 遍历二维列表
list2 = [[1,2,3,4],[5,6,7,8],[9,0,1,2]]
'''
for i in list2:
    print(i)
    for j in i:
        print(j)
'''
'''
for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(list2[i][j])
'''

# 三维列表
# 作业： range()
list3 = [[[1,2],[4,5],[6,7],[9,0]]]
'''
for i in list3:
    for j in i:
        for k in j:
            print(k)
'''



