# list  dict
# 存储
# pickle
'''
pickle支持存储list、dict、str等类型的数据。
pickle：实现了数据的序列化与反序列化操作。
数据的序列化操作可以实现数据的存储。
数据的反序列化操作可以实现数据的读取。
'''

# 导入pickle
import pickle
list1 = [1,2,3,4,5,7,8,9]
f1 = open(file="file.data", mode="wb")
# 将信息写入文件
# 语法格式： pickle.dump(obj,file)
# obj:写入的数据
# file:被写入的文件
pickle.dump(list1, f1)
f1.close()

# 读取文件
f2 = open(file="file.data", mode="rb")
# 读取文件  有返回值
# 语法格式:pickle.load(file)  file为读取的文件
l = pickle.load(f2)
print(l)
f2.close()

# 文件的后缀名常见的类型：txt  doc  docx  xls ，
# 文件的后缀名可以任意 : .abc   .ttt  .data

# 建议：当存储的数据不想通过文件双击直接打开，可以将后缀名设置
# 为系统不能直接打开的格式，如：.data   .list