# string   list  tuple(元组)  dict(字典)  set(集合)

# tuple()
# tuple  元组
# 本质：一个有序的不可变的集合
# 特点：1、和list相似  2、不可变的   3、用()创建

# 一、创建元组
# 格式：元组名 = (元素1, 元素2, .... 元素n)
# 1、创建空元组
tuple1 = ()
print(tuple1)
print(type(tuple1))  # tuple

# 2、创建带有多个元素的元组
tuple2 = (1,2,3,4)
print(tuple2)
print(type(tuple2))

# 3、元组中的数据类型可任意是任意类型
tuple3 = (1, 2.3, "abc", True, None)
print(tuple3)
print(type(tuple3))

# 4、创建带有一个元素的元组
tuple4 = (100)
# 使用以上方式创建的数据类型为括号中的数据类型，因为：小括号()既可以
# 表示元组，也可以是数学中的普通的小括号，系统自己会产生歧义，默认为
# 普通小括号。
print(tuple4)
print(type(tuple4))  # int

# 如果元组中只有一个元素，在该元素后面添加一个逗号 , 消除括号的歧义，
# 表示元组
tuple5 = (100, )
print(tuple5)
print(type(tuple5))  # tuple

# 注意一下格式：
tuple6 = (1, 2, 3)
print("这是一个元组   %s" % (tuple6, ))
name = "Lily";age = 12
print("这是一个名称   %s  %s" % (name,age))


# 二、元组的访问
tuple7 = (1,2,3,4,5,6,7)
# 1、取值
# 格式： 元组名[下标]  下标从0开始，不能越界
print(tuple7[0])
# print(tuple7[7])  # IndexError: tuple index out of range
# 获取最后一个元素
print(tuple7[-1])
print(tuple7[len(tuple7) - 1])

# 2、修改元组元素的值  不可修改
# 元组是不可变数据类型
# tuple7[0] = 100
# TypeError: 'tuple' object does not support item assignment
# print(tuple7)


# 三、元组的操作
# 1、元组的组合  +
tu1 = (1,2)
tu2 = (3,4)
tu3 = tu1 + tu2
print(tu3)

# 2、元组的重复  *
tu4 = (1,2)
print(tu4 * 3)

# 3、判断元素是否在元组中  in  not in
tu5 = (1,2,3,4,5,6)
print(2 in tu5)  # T
print(2 not in tu5)  # F

# 4、元组的截取  产生一个新的元组，对原元组无影响
# 语法格式：元组名[[起始下标start]:[结束下标stop][:][递增基数step]]
'''
说明：
start：截取元组的起始位置（包含），可以省略该参数，默认值为0
stop：截取元组的结束位置（不包含），可以省略该参数，默认值为长度
step：步长，间隔数，默认值为1,可以写负数， -1：从右向左截取
'''
tuple8 = (1,2,3,4,5,6,7,8,9)
# 从头开始截取，截取到下标4
print(tuple8[:5])
# 从下标4开始截取，截取到末尾
print(tuple8[4:])
# 截取 下标2 至 下标5
print(tuple8[2:6])
# 反转元组
print(tuple8[::-1])
# 隔一取一
print(tuple8[::2])
# 对原元组是否有影响
print(tuple8)


# 5、元组的修改
# 面试题
tuple9 = (1,2,[100,200,300])
# tuple9[0] = 200  # 报错
print(tuple9)
print(id(tuple9[2]))
tuple9[2][0] = 999
print(tuple9)
print(id(tuple9[2]))
# 表面上看，tuple中的数据发生了改变，实际上tuple的数据没变，只是tuple中
# 的list的数据发生了变化。
# tuple里面的数据不能改变，指的是元组中数据的内存地址不能变，而更改元组
# 中的列表的数据时，列表的内存地址没有发生变化，所以，更新数据成功。

# 四、元组的方法
tuple10 = (1,2,3,4,5,6)
# 1、获取元组的元素个数  len(tuple)
print(len(tuple10))
# 2、获取元组中最大值  max(tuple)
print(max(tuple10))
# 3、获取元组中最小值  min(tuple)
print(min(tuple10))
# 4、遍历元组的数据
for i in tuple10:
    print(i)

num = 0
while num < len(tuple10):
    print(tuple10[num])
    num += 1

# 五、二维元组
tuple11 = ((1,2,3), (4,5,6), (9,8,7))
print(tuple11[0][2])
# 遍历二维元组
for i in tuple11:
    for j in i:
        print(j)

# 六、删除元组  del 将整个元组对象删除
tuple12 = (1,2,3)
del tuple12
# print(tuple12)

# 七、数据类型转换
# list -> tuple   将list转为tuple
list1 = [1,2,3]
print(list1)
tu6 = tuple(list1)
print(tu6)

# tuple -> list   将tuple转为list
tu7 = (3,4,5)
list2 = list(tu7)
print(tu7)
print(list2)












