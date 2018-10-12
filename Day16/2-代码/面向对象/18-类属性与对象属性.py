class Person():
    # 直接写到class中的属性叫类属性(可以通过类名直接调用)
    name = "lily"
    def __init__(self, name, age):
        # 写在init中的属性叫对象/实例属性
        # self.name = name
        self.age = age
# 1、调用类属性
# 类名.属性名
print(Person.name)

# 2、对象属性的优先级高于类属性
# 当对象调用属性时，如果存在对象属性，直接使用对象属性；如
# 果不存在对象属性，去找相同名称的类属性；如果没有相同名称
# 的类属性，返回错误。
p1 = Person("lucy", 24)
print(p1.name)

# 3、对象动态添加属性,动态添加的属性在取值之前必须有赋值的过程
# 对象动态添加的属性对其他对象无效。
p1.weight = 50.0
print(p1.weight)

# p2 = Person("tom", 45)
# print(p2.weight)

print("----------------------------------")
# 4、删除对象属性
# 格式： del 对象名.属性名
# 当对象属性存在时，第一次删除对象属性；当
# 对象属性不存在时，第一次删除类属性。
p3 = Person("花花", 12)
print(p3.name)
# del p3.name
# print(p3.name)

# 注：以后尽量不要将类属性与对象属性重名，对象属性会覆盖类
# 属性，只有当对象属性删除时，才能找到类属性。


