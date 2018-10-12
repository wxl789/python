# Wife的类
class Wife():
    name = ""
    height = 1.5
    weight = 50.0
    def goShopping(self):
        print("妻子能购物")
    def makeHousework(self):
        print("贤惠的做家务")
    def hideMoney(self, money):
        print("辛苦藏了%s的私房钱" % money)
'''
实例化对象
语法格式： 对象名称 = 类名(参数列表)
注：无参数时，小括号也不能省略
'''
# 实例化对象
wife1 = Wife()
print(wife1)
print(type(wife1))
print(id(wife1))
print("**************")
wife2 = Wife()
print(wife2)
print(type(wife2))
print(id(wife2))

# Wife() 执行了一个叫构造函数(初始化函数)的方法
wife3 = Wife()

class Animation():
    pass
an1 = Animation()


