# from...import 语句
# 作用：可以从一个模块中引入部分功能
# 格式： from 模块名 import name1[ ,name2....namen]

# import module2,module1
# module1.getName()
# module1.run()

# 就近原则：在变量或函数的使用中，会使用离他最近的已经声明的变量或函数。

from module1 import getName,run
getName()
from module2 import getName
getName()
run()

def getName():
    print("4444---444")
getName()








