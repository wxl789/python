# 1、函数的返回值可以作为数据类型类型
def sumFunc(num1,num2):
    return num1+num2
res = sumFunc(1,2)
print(type(res))  # int

# 2、函数作为数据类型使用
# 类似给某个函数另起一个函数名称
res2 = sumFunc
print(res2)
print(type(res2))  # function
print(type(sumFunc))
print(sumFunc(1,2))
print(res2(3,4))

# sumFunc  == function 类型  函数名称
# sumFunc()  == 执行该函数





