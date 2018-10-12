# @property: 装饰器
# 作用：可以通过对象的点方法访问私有属性
# 注：公有属性不能使用@property
class Person():
    def __init__(self, name, age):
        # 公有属性
        self.name = name
        # 私有属性
        self.__age = age

    # set get
    '''
    def setAge(self, age):
        # 添加限制条件
        self.__age = age
    def getAge(self):
        return self.__age
    '''
    # 改写私有属性的get方法
    # 方法名称为私有属性去掉两个下划线的名称
    # @property:装饰器名称
    @property
    def age(self):
        return self.__age
    # 改写私有属性的set方法
    # 方法名称为私有属性去掉两个下划线的名称
    # @私有变量名称.setter:装饰器名称
    @age.setter
    def age(self, age):
        # 可以添加限制条件
        self.__age = age


p1 = Person("Lily",16)
# 当属性为公有属性时，可以通过对象直接获取或赋值，这种方式，相对
# 不安全，主要是因为没有任何条件限制。
print(p1.name)
p1.name = "Tom"
print(p1.name)

# 私有属性，不能通过对象直接赋值或取值，目前可以通过set或get方
# 法进行赋值及取值，可以在set或get中添加限制条件，相对安全。
# 使用时需要调用set及get方法
# p1.setAge(29)
# print(p1.getAge())

# 调用@property的set及get方法
# 取值 相当于调用@property的get方法
print(p1.age)
# 赋值 相当于调用@age.setter的set方法
p1.age = 66
print(p1.age)

print(p1.name)





