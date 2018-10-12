# 错误  异常
'''
程序运行或程序编写时，会遇到各种各样的错误，有些错误是因为程序编写有
问题出现的，这种错误一般称之为bug，bug是必须修复的。
有些错误是用户输入或错误使用时造成的，这种错误属于不可控的，但我们可以
通过检测用户输入或操作来做相应的处理。还有一些错误是无法在程序运行过程中
预测的，例如：网络中断，文件不存在等，这些错误可以认为是异常。
异常在程序运行中也是必须修复或处理的，否则，程序运行到该异常时，也会因为
异常而崩溃。
'''
# print("hello wordl")  # 语法正确，运行正常，结论错误，必须修改

# NameError: name 'num' is not defined
# print(num)  # 代码编写错误，运行错误，需要修改

# ZeroDivisionError: division by zero
# print(5 / 0)  # 语法正确，运行错误，需要修改

# 需求：当程序运行出现异常时，程序不会崩溃，跳过这些异常继续向下执行。
'''
语法格式：
try ... except .. else
try:
    语句（预测有可能会出现异常的语句）
except 错误代码1 [as e]:
    语句1(处理异常的语句)
[except 错误代码2 [as e]:
    语句2(处理异常的语句)
...
except 错误代码n [as e]:
    语句n(处理异常的语句)]
[else:
    语句n+1]

作用：检测try中的语句是否有错误，如果没有错误，正常执行语句，如果有
错误，让except捕获错误并处理错误。

逻辑：
当程序执行到try...except...else语句时：
1、如果try中的语句有错误，会跳出try语句，并执行第一个匹配到的except
语句，异常处理完毕后，程序跳出整个try并向下继续执行。
2、如果try中的语句有错误，会跳出try语句，并执行except
语句，但未匹配到正确的异常类型，程序会将异常提交给最上层的执行者，并
提出该异常，程序终止。
3、如果try中的语句有错误，会跳出try语句，并执行except语句，如果不清楚
异常类型，但想跳过该异常，except后面的异常类型可以不写。
4、如果try中的语句有错误，会跳出try语句，并执行except语句，如果
try中的语句没有错误，会正常执行try中的语句，并且执行else中的语句(
如果try写了else语句)。
'''
try:
    print(5 / 0)  # 预测
    print("中枢神经")
except ZeroDivisionError:
    print("您的除数为0，请修改")
except NameError:
    print("变量未定义")


# 匹配不到except
# try:
#     print(5 / 0)
# except NameError:
#     print("未定义")


# except无任何错误匹配类型
try:
    print(num)
except:
    print("嘿嘿嘿^_^")

try:
    print(5 / 0)
except ZeroDivisionError as e:
    # 错误代码的解释说明
    print(e)

# else语句
try:
    print("123")
except NameError:
    print("未定义num")
else:
    print("呵呵呵@_@")


# 使用except匹配多个异常
try:
    print("美人")
    print(a)
    print(5 / 0)
except (NameError,ZeroDivisionError,IndexError):
    print("有可能是num，或0，或index")

# 特殊使用
# 1、错误本质为class(类)，所有的错误都是继承于BaseException，如果在捕获
# 异常时，先匹配到正确的异常名称，执行该except中的语句。
try:
    print(num)
except NameError:
    print("NameError")
except BaseException:
    print("BaseError")

# 2、错误本质为class(类)，所有的错误都是继承于BaseException，如果在捕获
# 异常时，先匹配到BaseException，执行该BaseException except中的语句,
# 其他所有异常不再捕获。
try:
    print(num)
except BaseException:
    print("Base")
except NameError:
    print("Name")

# 3、程序可以跨越多层捕获异常，只要try能够找到并匹配到异常，程序就会
# 处理该异常。
def func1():
    print(5 / 0)
def func2():
    func1()
def func3():
    func2()
try:
    func3()
except ZeroDivisionError:
    print("Zero有可能出现")

'''
try ... except ... finally
语法格式：
try:
    语句（预测有可能会出现异常的语句）
except 错误代码1 [as e]:
    语句1(处理异常的语句)
[except 错误代码2 [as e]:
    语句2(处理异常的语句)
...
except 错误代码n [as e]:
    语句n(处理异常的语句)]
[finally:
    语句n+1]
解释：finally:无论try后面的语句有没有异常都会执行
'''

try:
    print("123")
    print(5 / 0)
except:
    print("错了！！！！！！！！！！！！")
finally:
    print("我出现了！！！")


# 断言
def divFunc(a,b):
    # 断言
    # 语法： assert 判断条件, 错误提示语句
    # 当条件成立，程序正常执行；当条件不成立，程序抛出AssertionError异常
    # 一般assert是程序员用于调试bug使用的。
    assert (b!=0), "参数b不能为0 162"
    print(a / b)
divFunc(1, 2)
# divFunc(10, 0)










print("hello 夏天")




