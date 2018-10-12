# 值传递:传递的是一个数值，传递的是不可变数据，通常认为传递了一个常量
# str  int  float  tuple  不可变
def func1(num):
    print(num)  # 100
    # 局部变量
    num = 200
    print(num)  # 200

num = 100
func1(num)
print(num)  # 100

# 引用传递：传递的是可变数据类型，传递了一个内存地址
# list  dict  set  可变
def listChange(data):
    print("2==",data)
    data[0] = 100
    print("3==",data) # [100,2,3,4]

list1 = [1,2,3,4]
print("1==",list1)
listChange(list1)

print("4==",list1)


# 函数的内部及函数的形参与函数外部有相同的变量名
def func2(num):
    # 形参的名称
    print(num)  # 形参num
    # 在函数内部重新定义了一个变量num
    num = 200
    print(num)  # 变量num
# 总结：函数内部的变量名称与函数的形参名称一致了，在函数内部使用
# # 该名称时，看名称定义的先后顺序，在变量定义之前使用为形参的值；
# # 在变量定义之后使用为变量的值。

num = 100
func2(num)




