# break与continue一般就出现在循环中

# break 语句
# 作用：结束for或while循环，当执行到break语句时，循环彻底结束。
# break:只能控制离他最近的那一层循环
# break:当循环语句执行到break时，语句彻底结束，else语句不再执行。
'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''
'''
num = 0
while num < 10:
    if num == 3:
        break
    print(num)
    num += 1
'''
'''
for i in range(5):
    if i == 2:
        break  # 控制i
    for j in range(5):
        if j == 2:
            break  # 控制j
        print("i=%d,j=%d" % (i,j))
'''
'''
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("你好")
'''


# continue 语句
# continue:作用：终止本次循环，不影响下一次循环
# continue对else语句无任何影响
# continue:只能控制离他最近的那一层循环
#
'''
for i in range(10):
    if i == 3:
        continue
    print(i)
'''
'''
for i in range(5):
    if i == 4:
        continue
    print(i)
else:
    print("没了")
'''

for i in range(5):
    if i == 2:
        continue  # 控制i
    for j in range(5):
        if j == 2:
            continue # 控制j
        print(i, j)






