'''
os模块：包含普通操作系统的功能
os：包含了处理目录或文件的相关方法
'''

import os

# 查看操作系统类型
# nt-->windows 新技术  new technology
# posix--> Linux、Unix、Mac os  可移植操作系统  portable operation system
# interface of unix
# print(os.name)

# 查看系统环境变量
print(os.environ)
# 获取部分环境变量
print(os.environ.get("APPDATA"))
# set：只写     get：只读
# 环境变量   系统变量   用户变量

# 返回当前目录   （.）
# . : 代表当前目录    .. ：上一级目录
print(os.curdir)

# 返回当前目录的路径   **
print(os.getcwd())

# 返回指定目录下的目录或文件   **
# 如果listdir没有参数，默认展示当前目录下的所有文件及目录
# (包含隐藏文件)
# 如果listdir有参数，默认展示该目录下的所有文件及目录
# (包含隐藏文件)
print(os.listdir())
print(os.listdir(path=r"C:\Users\xlg\Desktop\面向对象"))
print(os.listdir(path="C:\\Users\\xlg\\Desktop\\面向对象"))

# 创建目录   **
# 注：当文件已存在时，无法创建该文件。
# os.mkdir(path)
# os.mkdir("aa")
# os.mkdir(r"C:\Users\xlg\Desktop\os模块\bb")
# os.mkdir(os.getcwd() + r"\cc")
# os.mkdir("C:\\Users\\xlg\\Desktop\\dd")

# r"C:\Users\xlg\Desktop\面向对象"
# 创建文件  windows下不支持
# os.mknod()
# open("", "w")

# 删除目录 (不会放到垃圾箱中，删除时请注意)  **
# 注：删除的目录路径要求存在，不存在报错。
# os.rmdir("aa")
# os.rmdir("C:\\Users\\xlg\\Desktop\\dd")

# 删除文件  **
# os.remove(os.getcwd() + r"\a.txt")

# 获取文件信息
# print(os.stat(os.getcwd()+r"\os模块.py"))

# 重命名  **
# os.rename("初始的文件路径", "新的文件名")
# os.rename("bb", "dd")


# os模块下存放创建等直接方法，还有一部分方法是放在os.path下
# 判断当前路径是否为文件 **
# os.path.isfile(path)  是文件返回True，不是返回False
# 当文件不存在时返回False
# print(os.path.isfile(os.getcwd()+r"\os模块.py"))
# print(os.path.isfile(os.getcwd()))
# print(os.path.isfile(os.getcwd() + r"\abc.txt"))

# 判断当前路径是否为目录  **
# os.path.isdir(path)  是目录返回True，不是返回False
# 当目录不存在时返回False
# print(os.path.isdir(os.getcwd()+r"\os模块.py"))
# print(os.path.isdir(os.getcwd()))
# print(os.path.isdir(os.getcwd()+r"\oo"))

# 判断当前文件或目录是否存在  **
# 存在返回True，不存在返回False
print(os.path.exists(os.getcwd()))
print(os.path.exists(os.getcwd() + r"\os模块.py"))
print(os.path.exists(os.getcwd() + r"\os"))

# 获取文件大小
# 如果路径为目录/文件夹：返回4096/0
print(os.path.getsize(os.getcwd() + r"\os模块.py"))
print(os.path.getsize(os.getcwd()))

# 判断当前路径是否为绝对路径
print(os.path.isabs("os模块.py"))
print(os.path.isabs(os.getcwd() + r"\os模块.py"))

# 返回绝对路径
print(os.path.abspath(r".\aa"))

# 拆分路径   **
# 将最后一个目录或文件隔离
print(os.path.split(r"C:\Users\xlg\Desktop\os模块\os模块.py"))
# ('C:\\Users\\xlg\\Desktop\\os模块', 'os模块.py')

# 分离文件名与扩展名
print(os.path.splitext(r"C:\Users\xlg\Desktop\os模块\os模块.py"))
# ('C:\\Users\\xlg\\Desktop\\os模块\\os模块', '.py')

# 拼接路径  **
print(os.getcwd() + r"\abc.txt")
# os.path.join(path, *path) 第二个参时开始不用写 \
print(os.path.join(os.getcwd(), "abc.txt"))


# 返回文件名  **
print(os.path.basename(os.getcwd() + r"\abc.txt"))

# 返回目录名
print(os.path.dirname(os.getcwd() + r"\abc.txt"))















