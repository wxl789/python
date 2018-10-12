# List  集合  有序可变集合  一组数据组合到一起
# List 列表 -- 数组

# 一、创建列表
# 语法格式： 列表名 = [元素1, 元素2, ... 元素n]
# 注：不同元素之间用 , 隔开
# 注：列表中的元素类型可以不同

# 1、创建空列表
list1 = []
print(list1)
print(type(list1))  # list
# 2、创建带有元素的列表
list2 = [1, 2, 3, 4]
print(list2)
# 3、创建带有不同类型的元素的列表
list3 = [1, 2.3, "abc", None, True]
print(list3)
# 4、list中可以包含list类型的元素
list4 = [1, 2, [55, 66, 77], 8, 9]
print(list4)

# 二、访问列表中的元素
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1、取值： 格式：列表名[下标/索引/index]  下标从0开始
print(list5[1])
# 下标不能越界， 最后一个元素的下标 len(list) - 1
# print(list5[16])  # IndexError: list index out of range

# 2、取值：下标可以写负数  -1：代表最后一个元素
# 负数代表从右向左查
print(list5[-1])

# 3、更新数据
# 语法： 列表名[下标] = 新值
print(list5)
list5[0] = 200
print(list5)

# 三、列表的操作
# 1、+  列表的组合
list6 = [1, 2, 3]
list7 = [6, 7, 8]
print(list6 + list7)
# 2、*  列表的重复
print(list6 * 2)
# 3、列表的截取
# 语法格式：列表名[[起始下标start]:[结束下标stop][:][递增基数step]]
'''
说明：
start：截取列表的起始位置（包含），可以省略该参数，默认值为0
stop：截取列表的结束位置（不包含），可以省略该参数，默认值为长度
step：步长，间隔数，默认值为1,可以写负数， -1：从右向左截取
'''
list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 截取部分元素
print(list8[1 : 5])
# 从开始位置截取到数字5
print(list8[:5])
# 从数字6开始到列表末尾
print(list8[5:])
# 截取所有元素
print(list8[:])
print(list8[::])
# 反转列表
print(list8[::-1])
# 步长
print(list8[::2])
# 注：注意下标及步长的正负号
print(list8[-5:-2:1])
print(list8[-5:-2:-1])

# 4、判断元素是否在列表中  in  not in
list9 = [1,2,3,4]
print(1 in list9)  # T
print(12 in list9)  # F

# 四、n维列表
list10 = [1, 2, 3, 4]   # 一维列表
# 二维列表  list中的元素类型还是list类型
list11 = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
print(list11)  # [[1,2,3],[11,22,33],[111,222,333]]
print(list11[0])  # [1,2,3]
print(list11[0][1])  # 2

listSub = list11[0]  # ===> listSub = [1,2,3]
int1 = listSub[1]  #
print(int1)

# 三维列表
list12 = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,0],[11,12]]]
print(list12)   # [[[1,2],[3,4]],[[5,6],[7,8]],[[9,0],[11,12]]]
print(list12[0])   # [[1,2],[3,4]]
print(list12[0][1])  # [3,4]
print(list12[0][1][0])  # 3


# 获取列表的元素个数  len(list)

# 五、增删改查














