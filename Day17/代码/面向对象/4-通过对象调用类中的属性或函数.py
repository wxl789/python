# Wife的类
class Wife():
    name = ""
    height = 1.5
    weight = 50.0
    # 创建普通的成员方法的方式与之前创建def的方式一致，只是第一个形参默认
    # 为self。
    # 初始值   返回值  多个形参
    def goShopping(self):
        print("妻子能购物")
    def makeHousework(self):
        print("贤惠的做家务")
    def hideMoney(self, money):
        print("辛苦藏了%s的私房钱" % money)
# 只要通过某个类创建出来的实例对象，实例对象可以调用该类中的任意一个
# 属性或方法，实例对象可以调用任意次数。

# 实例化一个对象
wife1 = Wife()
'''
对象访问类中的属性
获取类中属性的值：对象名.属性名
修改类中属性的值：对象名.属性名 = 新值
'''
print(wife1.height)
wife1.height = 1.6
print(wife1.height)
wife1.name = "苍老师"
print(wife1.name)

'''
对象访问类中的方法
语法格式：对象名.函数名(参数列表)
注：类中的成员方法默认第一个形参叫self，当实例对象调用该方法时，
系统默认将实例对象传给self形参，不用我们手动传值。
注：实例对象调用成员方法时，第一个形参self可以忽略，但其他形参不能
省略。
'''
wife1.goShopping()
wife1.makeHousework()

wife1.hideMoney(100)
# 关键字形式
wife1.hideMoney(money=1000)

# 类中不存在的属性或变量不能直接使用
# wife1.findMoney(100)
print(wife1.name)
# 动态添加属性(后面会讲),只对当前实例对象有效
wife1.age = 22
print(wife1.age)



wife2 = Wife()
print(wife2.height)  #1.5

'''
# 调用成员方法
wife2.goShopping()


# 浅拷贝
wife3 = wife1
print(wife3.height)
print(wife3.name)
wife3.name = "小鸽子"
print(wife3.name)
print(wife1.name)
'''