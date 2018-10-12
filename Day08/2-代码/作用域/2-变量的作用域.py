# 变量的作用域
'''
变量的作用域:变量可以正常使用的范围。
变量并不是在当前文件的任意位置均可使用，访问的权限范围取决于该变量定义
的位置。

在Python中，模块(module)、类(class)、函数(def)会产生新的作用域，在这些代码
块中定义的变量，在其他位置也不能使用。
其他的代码块，如if、for、while、try，不会引入新的作用域，在这些代码
块中定义的变量，在其他位置也可以使用。

变量的作用域分类：
B(built-in)  内建作用域
G(Global)    全局作用域
E(Enclosing)  闭包作用域
L(Local)      局部作用域

变量的查找规则： L -> E -> G -> B
先从局部查找，找到直接使用，找不到去闭包中找，找到直接使用，
找不到去全局中找，找到直接使用，找不到去内建中找，找到直接使用，
找不到报错。
'''
# 验证 if
if 1:
    a = 10
    print(a)
print(a)

# 验证 def
# 函数内部声明的变量，在函数外部不能使用。
def func1():
    b = 200
    print(b)
func1()
# print(b)  # NameError: name 'b' is not defined
print("********************************************************")
# 在.py文件中声明的变量为全局变量
c = 200
print(c)

# 作用域范围从大到小排列：  B -> G -> E -> L
# dir() Builtins  python的内建函数：能够使用的范围为内建作用域  内建函数/内建变量
#       内建变量或函数属于python语言环境范围的变量或函数。
'''
dir = 1  # Global 全局作用域  全局变量  在当前文件的任意位置均能使用
def outerFunc():
    dir = 2  # Enclosing  闭包作用域  在闭包范围内使用
    def innerFunc():
        dir = 3  # Local  局部作用域  只能在该局部范围内使用
    return innerFunc

def func():
    dir = 4  # Local  局部作用域  只能在该局部范围内使用
'''
print("********************************************************")
# 定义一个全局范围的变量num
num = 100
print("1==", num)

def func():
    # 定义了一个局部范围的变量num，只是该局部变量与全局变量名字相同。
    # 局部范围的变量与全局范围的变量互不影响。
    # 如果变量没有global修饰，就是一个局部变量，不能修改全局变量。
    num = 200
    print("2==", num)
func()
print("3==",num)


num1 = 100
print(num1)

def func2():
    # 在局部范围修改全局变量使用global关键字修饰变量
    # 语法规则： global 变量名
    # 使用global关键字修饰的变量为全局变量，该局部范围直接可以获取及
    # 修改全局变量。
    # 当同时使用多个全局变量时，使用 逗号 (,) 隔开
    # 注：使用global关键字，需要放在函数的最上方，函数的最开始位置。
    global num1,num
    num1 = 200
    print(num1)
    num = 800
    print(num)

func2()
print(num1)
print(num)


# nonlocal  非局部
i = 777  # 全局
def outerFunc():
    i = 666  # 局部
    def innerFunc():
        nonlocal i  # nonlocal  修饰局部变量
        i = 555  # 局部范围的局部变量
        print("inner==", i)
    innerFunc()
    print("outer==",i)

outerFunc()
print(i)

print("******************************")
def a():
    i = 1
    def b():
        nonlocal i
        i = 2
        def c():
            nonlocal i
            i = 3
            print("c==",i)
        c()
        print("b==",i)
    b()
    print("a==",i)
a()


name = "Lily" # 全局变量
def changeFunc():
    global name
    name = "Lucy"
    def inner():
        global name
        name = "张三"
        print(name)
    inner()
    print(name)
changeFunc()
print(name)





