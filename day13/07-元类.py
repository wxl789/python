

class Demo(object):
    pass
demo = Demo()
print(demo)#类--》对象

def echo(o):
    print(o)
#可以作为参数进行数据的传递
echo(demo)

#可以为类增加属性hasattr
print(hasattr(Demo,"new_attribute"))#false
Demo.new_attribute = "haha"
print(hasattr(Demo,"new_attribute"))

#可以将类赋值给一个变量
dd = Demo
print(dd)



"""
元类---》类的类：通过元类来创建类
"""



