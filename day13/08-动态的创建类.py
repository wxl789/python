
def choose_name(name):
    if name == "haha":
        class haha(object):
            pass
        return haha#类，而不是类的实例
    else:
        class hahei(object):
            pass
        return hahei

myClass = choose_name("haha")

print(myClass)#函数返回的是类，不是类的实例
print(myClass())#返回类的实例----》对象
"""
type:内置函数  类型
"""
print(type(1))
print(type("1"))
print(type(choose_name("haha")))




