# 随机数

# 想要获取随机数，需要导入random模块
import random

# 1、从一个列表中随机选出一个元素,内容任意，可以不连续
print(random.choice([1, 2, 5, 6, 8, 3]))
print(random.choice(["Lily", "Lucy", "Lilei", "HMM"]))

# 2、range(x)
# range(5)  ==  [0, 1, 2, 3, 4]
print(random.choice(range(10)))

# 3、从字符串中随机选择一个字母
print(random.choice("meakelra"))

# 4、从指定范围随机数字
# 语法格式：random.randrange([start,] stop [,step])
# start: 指定开始的值，该值包含在取值范围内；如股票不写该参数，默认为0。
# stop：指定结束的值，该值不包含在取值范围内。
# step：指定递增基数，默认为1

# 从0-9之间任意选择一个数字
print(random.randrange(10))
# 从5-10之间任意选择一个数字
print(random.randrange(5, 11))
# 随机一个四位数
print(random.randrange(1000, 10000))
# 设置递增基数
print(random.randrange(0, 10, 2))  # 0 3 6 9


# 5、随机生成 0(包含) 到 1(不包含) 之间的实数
print(random.random())
# 0-10之间的任意整数
print(int(random.random() * 10))

# 6、随机整数  random.randint(x, y)
# 随机生成 x(包含) 到 y(包含) 之间的整数
print(random.randint(0, 4))

# 7、随机整数  random.uniform(x, y)
# 随机生成 x(包含) 到 y(包含) 之间的实数
print(random.uniform(1, 2))

# 8、将一个序列随机排列
list1 = [1, 2, 3, 4, 5]
print(list1)
random.shuffle(list1)
print(list1)

# 7  11
# 写一个随机挑选人员的数，1-7排  1-11列
print("第1排，第1列")





