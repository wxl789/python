# package
# 初始化包的文件  目前不使用
# 可以认为是一个文件夹，只不过该文件夹默认有一个__init__.py文件

# 解决问题：防止文件名称冲突
# 只要整个项目下包名不冲突，不同包的文件名是否一致就不重要了。

# 只要导入包，会立即执行该包下的__init__.py中的内容

# 引入包下的模块
# 格式：包名.模块名
import newPackage.module1
import new1.pyc

# 使用包下的模块中的内容
# 格式：包名.模块名.变量名/函数名
newPackage.module1.run()


# from 包名 import 模块
from newPackage import module1
# 格式：模块名.变量名/函数名
module1.run()



# 将模块所属的包写全
import a.b.c.pyc

print(a.b.c.pyc.num)







