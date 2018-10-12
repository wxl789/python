'''
self:代表类的实例对象，在本类中使用self表示实例对象。
self不是关键字。
'''
class Fly():
    def __init__(self, name):
        # self:对象   self.name:属性，成员变量，对象属性，实例属性
        self.name = name

    def run(self):
        print(1234)

    def flyHeight(self):
        # 在本类中调用属性或方法使用self
        # 格式： self.属性/方法
        print(self.name + "飞的高")
        self.run()
    # self:不是关键字，换成其他名称也是可以的,但是类中
    # 的成员方法至少要存在一个形参，第一个形参就是代表当前类
    # 的实例对象。实例对象在调用成员方法时，会默认将实例对象
    # 传给成员方法的第一个形参。
    # 注：帅/漂亮的人都用self。
    def eat(my):
        print("eat123")
        print(my.name)

f1 = Fly("妞妞")
f1.flyHeight()

