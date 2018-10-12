
class People(object):
    address = "杭州"#类属性

#通过实例对象去修改类属性
print(People.address)

#创建实例对象
p = People()
print(p.address)

#直接方式
p.address = "北京"
print(p.address)

print(People.address)

del p.address
print(p.address)

People.address = "北京"
print(p.address)






