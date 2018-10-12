# for - in 循环
'''
语法格式：
for 变量 in 集合:
    语句
逻辑：按照顺序依次取出集合中的元素，取出的元素给变量赋值，执行for下面的
语句，直到取出最后一个元素，循环结束。
'''
list1 = [1,2,3,4]
'''
# while
num = 0
while num < len(list1):
    print(list1[num])
    num += 1
'''
'''
for i in list1:
    print(i)
'''
# 输出 0-4
'''
num = 0
while num<5:
    print(num)
    num += 1
'''
'''
range([start,] stop [,step])
说明：
start：起始位置（包含在取值范围内），可以省略该参数，默认值为0
stop：结束位置（不包含在取值范围内）
step：步长，间隔数，默认值为1
功能：生成一个列表(数字类型的集合列表)
range(5) ==> [0,1,2,3,4]
'''
a = range(5)
print(a)  # range(0,5)
print(a[0])
print(a[2])
# print(a[5])  # IndexError: range object index out of range 下标越界报错

b = range(10,20) # [10,11,...19]
print(b[1])  # 11

c = range(10,20,3)  # [10,13,16,19]
print(c[1])  #

# 0-4
for i in range(5):
    print(i)
# 5遍hh
for i in range(5):
    print("hh")

list2 = ["温柔", "粗暴", "美丽", "富有", "多金"]
# 三种方式
#
num = 0
while num < len(list2):
    print(list2[num])
    num += 1

for i in list2:
    print(i)

for i in range(len(list2)):
    print(i, list2[i])

'''
for - else 
语法格式：
for 变量 in 集合:
    语句1
else:
    语句2
注：else语句:当集合中的元素全部遍历结束后执行，最多只会执行一次
'''
for i in range(3):
    print(i)
else:
    print("结束")


# 输出1-100的和
sum1 = 0
for i in range(101):
    sum1 += i
print(sum1)

# 字符串为不可变的有序的集合
str1 = "abc"
for i in str1:
    print(i)

