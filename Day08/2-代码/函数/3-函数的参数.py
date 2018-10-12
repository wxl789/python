# 定义一个函数，该函数有一个参数，在函数内部输出该参数

# 定义一个只有一个参数的函数
# 函数的声明
# 形参:函数定义时小括号中的变量。本质：就是变量
def myPrint(name):
    # 函数的形参在函数内部可以正常使用，使用方式类似变量名称的调用
    print(name)
    print("****************")

# 函数的调用
# 实参：函数在调用时传递给函数的形参的数据。本质：就是常量
# 注：函数在声明时有形参，那么函数调用时必须传入实参。
myPrint("张三")
myPrint("李四")

# 错误：函数定义时有形参，那么函数调用时，要求传入实参。
# myPrint()
# TypeError: myPrint() missing 1 required positional argument: 'name'


# name="张三"
# print(name)


# 需求：定义一个函数，该函数有两个参数 name/age，功能：输出"姓名是...，
# 年龄是..."
def getNameAndAgeAndSex(name, age, sex):
    print("姓名是%s，年龄是%s，性别是%s" % (name, age, sex))

# 函数的调用
getNameAndAgeAndSex("Meakelra", 18, "MM")

# TypeError: getNameAndAgeAndSex() missing 1 required positional argument: 'sex'
# getNameAndAgeAndSex("LL",23)

getNameAndAgeAndSex(23,"女", "Lily")

# 注：参数个数:目前函数调用时传入的实参个数要求与函数定义时的形参个数一致。
# 注：目前实参是从左向右依次给形参赋值。

# 建议：定义函数时，如果时多个单词的组合城的函数名，使用驼峰原则，单词的
# 首字母大写。



