class People(object):
    address = "杭州"#类属性
    def __init__(self):
        self.name = "laowang"#实例属性
        self.age = 20#实例属性

#创建People类的实例对象
p = People()
p.age = 12

print(p.age)
print(p.address)

print(People.address)
# print(People.age)#类对象不能访问实例属性
# print(People.name)





