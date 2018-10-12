# 自定义模块：自己创建的.py文件
# 引入模块时，没有.py后缀名
import module1
import module2
# 一i行引入多个模块
import module1,module2

# 使用自定义模块中的内容
# 语法格式：  模块名.变量名/函数名
print(module1.a)
module1.getName()

print(module2.b)
module2.getName()

def getName():
    print("3-3")
getName()


