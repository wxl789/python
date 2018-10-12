# 不定长参数
# 概念：能够在函数内部处理比形参个数多的实参

# 加了 (**) 的变量，可以存放多个实参。
# 加了 ** 的形参，数据类型为字典类型，如果调用时未传入传入参数，默认
# 为一个空字典，如果传入了实参，将传入的实参按传入顺序依次放到字典中。

# 函数定义
def fun1(**kwargs):
    print(kwargs)
    print(kwargs.get("b"))
    print(kwargs.get("d"))
    # kwargs["b"] 如果b未传参数，程序报错

fun1()
print("--------------------------------------------------")
# 函数调用传入参数   key=value
fun1(a=1)
print("--------------------------------------------------")
fun1(a=1, b=2,c=3,d=9)
print("--------------------------------------------------")

# 定义一个函数，既有普通的形参，又有**的形参
def fun2(num, **kwargs):
    print(num)
    print(kwargs)
# 调用
# 当调用时如果全部使用关键字参数形式，会将普通形参按关键字赋值，其他找
# 不到普通形参的关键字默认放到**kwargs中。
fun2(300,a=400)
fun2(400,a=300,b=400)
fun2(num=555,a=999,b=33)
fun2(s=888,g=777,num=333)


# 定义一个通用函数
def fun3(*args, **kwargs):
    print(args)
    print(kwargs)
print("-------------------------")
fun3()
fun3(1,2,3)
fun3(a=1,b=2,c=3)
fun3(1,2,3,a=1,b=2,c=3)

# 定义一个函数，该函数必须传入name，age，sex，可选参数为phone，address
print("********************")


def getStu(name,age,sex,**kwargs):
    print(name,age,sex)
    print(kwargs.get("phone"),kwargs.get("address"))

getStu(name="LL",age=12,sex=0)
getStu(name="LL",age=12,sex=0,phone="110")
getStu(name="LL",age=12,sex=0,address="杭州")
getStu(name="LL",age=12,sex=0,phone="120",address="南京")














