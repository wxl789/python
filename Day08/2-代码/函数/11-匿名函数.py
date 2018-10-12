'''
普通函数使用def定义。

匿名函数：
不使用def关键字定义，用lambda关键字来创建。
语法格式： lambda 参数1,参数2...参数n:表达式
表达式：只能是一条简单的语句，不能包含循环、return、yield等，允许包含
最简单if语句，如果表达式为元组类型，使用小括号括起来。

lambda特点：
1、lambda只是一个一条语句的表达式，整个函数体语句比def简单很多。
2、lambda本质为表达式，只能封装最简单的逻辑。

'''
def sum1(num1,num2):
    print(num1+num2)
    return None
res = sum1(1,2)
print(res)

# 当定义了lambda，使用变量接收该表达式
# 函数的定义
res = lambda num1,num2:num1+num2
# 函数的调用
print(res(2,3))



# if-else在lambda中使用
# 语法格式:  结论1 if 条件表达式 else 结论2
# 解释：当条件表达式为真时，取结论1；当条件表达式为假时，取结论2

res1 = lambda num:"真棒" if num==1 else "更好"
print(res1(1))
print(res1(2))

def res2(num):
    # print(123456789)
    if num == 1:
        return "ff"
    else:
        return "gg"


