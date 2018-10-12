# 字典
# 成对出现   key-value
'''
dict概述：使用键值对(key-value)方式存储数据。
新华字典  ---  汉字-拼音  啊-a  吧-ba  阿-a
dict的key的特点：
        1、key必须是唯一的
        2、key值必须是不可变的数据类型：int float string tuple
        3、list是可变的，不能做key值
dict的value的特点：
        value的类型可以是任意类型的，可以重复。

dict的特点：
        1、无序的集合
        2、可变的集合
'''
# 保存多名学生的姓名、性别、年龄  3个
# 有可能会造成数据顺序错乱，下标对应的数据需要每次检查
list1 = [["lily",1,12],["lucy",0,14],["ll",16,0]]

# 建议使用字典存储  name:lily, age:13, sex:0

# 一、创建字典
# 格式：{key1:value1, key2:value2, ....keyn:valuen}
# 1、创建空字典
dict1 = {}
print(dict1)
print(type(dict1))  # dict
# dictionary

# 2、创建带有多个元素的字典
# 注：创建字典的顺序与输出时的顺序有可能不一致，只要key值全部存在
# 即可。
dict2 = {"name":"Lily", "age":12, "sex":0}
print(dict2)
print(type(dict2))
# 3、创建带有一个元素的字典
dict3 = {"name":"Lucy"}
print(dict3)

# 4、验证key的规则特点
# 4.1、key值不能重复
# key值在创建时可以出现重复，但只会保留最后一次赋值的value
dict4 = {"name":"Lucy", "age":12, "name":"MM"}
print(dict4)
# 4.2、字符串可以做key
dict5 = {"abc":123}
print(dict5)
# 4.3、number可以做key
dict6 = {1:"a"}
dict7 = {1.2:"b"}
print(dict6)
print(dict7)
# 4.4、tuple可以做key
dict8 = {(1,2) : "abc"}
print(dict8)
# 4.5、list不可以做key
# dict9 = {[1,2]:"abc"}  # TypeError: unhashable type: 'list'
# print(dict9)

# 5、验证value的规则
dict10 = {"a":1, "b":1.2, "c":[1,2,3], "d":(1,2), "e":None,
          "f": True, "g":{1:"abc",2:"edf"}, "h":1}
print(dict10)

# 二、取值
dict11 = {"a":1, "b":1.2, "c":[1,2,3], "d":(1,2), "e":None,
          "f": True, "g":{1:"abc",2:"edf"}, "h":1}
# 1、获取某一元素方式1： 字典名[key]
print(dict11["b"])
# 当key不存在时，使用该方法报错
# print(dict11["abc"])  # KeyError: 'abc'

# 2、获取某一元素方式2：字典名.get(key)
print(dict11.get("a"))
# 当key不存在时，使用该方法返回None
print(dict11.get("abc"))
if dict11.get("abc") == None:
    print("该key不存在")
else:
    print(dict11["abc"])

# 三、字典的操作
dict12 = {"name":"lily", "age":13, "sex":0}
print(dict12)
# 1、增  格式：字典名[新的key]=value
dict12["address"] = "北京"
print(dict12)

# 2、删  将key移出，对应的value会自动删除  字典名.pop(key)
dict12.pop("sex")
print(dict12)

# 3、改   格式：字典名[key]=新的value
dict12["name"] = "Lilei"
print(dict12)

# 4、查
print(dict12["name"])

print("********************--------------------------*")
# 四、字典的遍历
dict13 = {"name":"lily", "age":13, "sex":0,"address":"杭州"}
# 方式1
for i in dict13:
    print(i, dict13[i])
# 方式2
# 字典名.keys() : 返回一个key的列表
print(dict13.keys())  # 类似list
for i in dict13.keys():
    print(i, dict13[i])
# 方式3
# 字典名.values() : 返回一个value的列表
dict13 = {"name":"lily", "age":13, "sex":0,"address":"杭州"}
print(dict13.values())
for i in dict13.values():
    print(i)
# 方式4
# 字典名.items() : 返回一个列表,该列表中的元素为元组类型
# 元组的第一个元素为key，元组的第二个元素为value
print(dict13.items())
for i in dict13.items():
    print(i)
    print(i[0], i[1])
# 方式5
# dict13.items()==[('name', 'lily'), ('age', 13), ('sex', 0), ('address', '杭州')]
# 当list中的元素为元组类型时：for后面的变量可以写多个，用 , 隔开，
# 每个变量分别对应元组相应下标的元素
# 使用该方式时，不建议元组的元素个数过多。
for key,value in dict13.items():
    print(key,value)

'''
dict与list的优缺点：
list：1、查找或插入数据会随着数据的增加而变慢
      2、占用空间小，内存浪费少
dict: 1、查找或插入数据快，不会随着数据的增加而变慢
      2、占用内存大，内存浪费多
'''










