# 定义一个函数，该函数有三个参数，函数内部输出三个参数
def getNameAndAgeAndSex(name,age,sex):
    print(name,age,sex)

# 调用
# 函数的关键字
# 参数的关键字：在函数调用的传参过程中将形参的名称写在赋值符号之前，将值
# 写在赋值符号之后。
# 优点：1、明确实参对应的形参
#       2、允许函数调用时实参的顺序与函数定义时形参的顺序不一致，但赋值
#         对象不会错乱

# 建议：以后再函数调用时尽量使用关键字参数的形式。
getNameAndAgeAndSex("QQ",12,1)

getNameAndAgeAndSex(name="WX", age=23, sex=0)
getNameAndAgeAndSex(age=67, sex=1, name="MoMo")