'''
*****
'''
'''
print("*")
for i in range(5):
    print("*", end="")
'''
'''
for i in range(5):  # 行
    for j in range(5):   # 列
        print("*", end="")
    print()
'''
'''
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
'''
# 输出0-20之间的数 除3的倍数  for if
for i in range(21):
    if i % 3 != 0:
        print(i)


