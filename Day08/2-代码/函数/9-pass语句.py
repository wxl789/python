# pass语句
# pass 代表一条空语句，本身无任何意义,可以用作代码的占位语句
# 可以出现在当前文件的任意位置
print("124")
pass
print("456")

# 定义一个函数，该函数的功能不确定
def count():
    # 此功能未完善
    # 后期有可能会新增功能或修改功能
    pass
count()

if True:
    # 占位语句
    pass
else:
    print("哈哈")