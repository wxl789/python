# 引入模块
# 格式： import module1 [,module2...modulen]

# import :不管import同时多次引入同一个文件，系统只会编译一次
# import:防止多次引入

# 每次引入一个模块
import math
import pickle

# 一次性引入多个模块
import math,pickle,random

# 使用模块中的内容  模块名称.变量名/函数名   （该模块要存在这些内容）
print(math.pi)

