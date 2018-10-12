
People = type("People",(),{"name":"zhangsan"})
"""
class People:
    name = "zhangsan"
"""
print(People)
print(People.name)

p = People()
print(p)
print(p.name)

# class child(People):
#     pass

child = type("child",(People,),{})
print(child)

print(child.name)
"""
注意：
   1.type函数时，第二个参数---》元祖中是父类的名字，而不是一个字符串
   2.type函数，在添加属性时，属性---》类属性，而不是实例属性
"""



