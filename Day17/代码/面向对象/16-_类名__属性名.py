# _类名__属性名称  ： 私有变量
class Father():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # _Father__age
    # 私有属性在运行时会被解析成 _类名__属性名,我们可以通过
    # _类名__属性名 方式获取私有属性。
    # 建议：除紧急情况或特殊情况，不要使用这种方式。

f1 = Father("李刚", 56)
print(f1.name)
print(f1._Father__age)


