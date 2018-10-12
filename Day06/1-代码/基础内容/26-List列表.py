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
list1 = [1,2,3,4,5]
# 1、增加数据
# append : 在列表末尾添加新的元素
# list.append(obj) : 将obj作为一个整体添加到list列表中
print(list1)
list1.append(6)
print(list1)
list1.append("abc")
print(list1)
list1.append([11, 22, 33])
print(list1)

# extend : 在列表末尾添加新的元素
# list.extend(iter) : 在列表末尾一次性追加iter里面所有的元素（将iter
# 中的元素拆开添加）
# 注：iter为集合类型
list2 = [1,2,3]
print(list2)
list2.extend([7,8,9])
print(list2)
list2.extend("abc")
print(list2)

# insert 插入数据
# list.insert(index,obj) 在指定的index下标位置新增元素，该下标
# 原来的的数据不会被覆盖，原数据依次向后顺移。
# obj:任意类型数据
list3 = [1,2,3,4]
print(list3)
list3.insert(1,999)
print(list3)
list3.insert(1,[100,200])
print(list3)

# 2、更改数据
list4 = [1, 2, 3, 4]
list4[1] = 200
print(list4)

# 3、删除数据
list5 = [1,2,3,4,5,6,7]
# pop ： 删除数据
# pop([index]) : 删除指定index位置的元素，如果不指定index，默认删除
# 最后一个元素
# pop有返回值，将删除的数据返回
print(list5)
# list5.pop()
# list5.pop(1)
print(list5.pop(1))
print(list5)

list6 = [1,2,3,4,5,2,2,3,2]
# remove  删除数据
# list.remove(obj) 删除匹配到的第一个obj
# 删除的元素要求在列表中存在，不存在报错
print(list6)
list6.remove(2)
# list6.remove(9)  # ValueError: list.remove(x): x not in list
print(list6)

list7 = [1,2,3,4]
print(list7)
# clear:清空列表
# list.clear()  清除列表中所有的元素
list7.clear()
print(list7)

# 4、查询数据
list8 = [1,2,3,2,2,4,5,6,7,8,9]
# 获取数据  下标获取数据
print(list8[0])

# in / not in  判断列表中是否存在某个元素
print(2 in list8)

# index  获取元素下标
# list.index(obj [,begin, end])  从list中查找第一个匹配到的obj的
# 下标，如果指定begin与end，在该范围内查找。
# 如果找不到obj元素，返回一个ValueError的错误。
print(list8.index(2))
print(list8.index(2, 4, 7))
# print(list8.index(100))

print("*****************************")
# 六、列表的其他方法
list9 = [1,2,2,2,2,2,2,2,3,4,5]
# 1、获取列表的元素个数  len(list)
print(len(list9))
# 2、返回列表中最大的元素  max(list)
print(max(list9))
# 3、返回列表中最小的元素  min(list)
print(min(list9))
# 4、返回列表中某个元素出现的次数
# list.count(obj)  返回list中obj出现的次数
print(list9.count(2))

# 5、排序
# list.sort()  将列表中的元素排序，默认升序/正序
# 当元素为数字类型时，按数字大小排序；当元素为字符串类型时，按ASCII
# 排序。
list11 = ["3","2","0","98","9","10","1"]
print(list11)
list11.sort()
print(list11)

# 倒序排列
list11.sort(reverse=True)
print(list11)

# 6、反转列表
# list.reverse()
list12 = [1,2,3,4]
# print(list12[::-1])  # 产生一个新列表，原列表无变化
list12.reverse()
print(list12)

print("**********************")
# 七、拷贝
# 浅拷贝 ： 同一个内存地址，拥有不同的变量名称
arr1 = [1,2,3,4]
print(arr1)
arr2 = arr1
print(arr2)
arr2[0] = 100
print(arr2)
print(arr1)

print("*************************************************")
# 深拷贝(仿深拷贝) : 复制数据，将复制的数据放到新的内存地址中
# 注：列表中的可变数据类型的内存地址一样
arr3 = [1,2,3,4]
arr4 = arr3.copy()
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))
arr3[0] = 100
print(arr3)
print(arr4)

#
print("**************************")
arr5 = [[1,2,3,4],[6,7,8,9]]
print(arr5)
arr6 = arr5.copy()
print(arr6)
print(id(arr5))
print(id(arr6))

arr5[0][0] = 100
print(arr5)
print(arr6)
print(id(arr5[0]))
print(id(arr6[0]))

# 真正的深拷贝,：初始数据一致，内存地址不一致
import copy
print("-----------------")
arr7 = [[1,2,3],[6,7,8]]
arr8 = copy.deepcopy(arr7)
print(id(arr7))
print(id(arr8))
print(id(arr7[0]))
print(id(arr8[0]))
















