"""
type()
type(name, bases, dict)
name:类名
bases:有父类名称组成的元祖（针对继承，可以为空）
dict:包含属性和方法的字典
"""
class Demo(object):
    pass

print(Demo())

demo = type("Demo",(),{})
print(demo())

