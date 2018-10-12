'''
创建设计一个类的步骤：
1、类名：遵循标识符的命名规则，见名知意，类名尽量不要太长。建议：单词
的第一个字母大写
2、属性：遵循标识符的命名规则，见名知意，变量  写在类中的变量
成员属性  成员变量
3、行为：遵循标识符的命名规则，见名知意，方法/函数/功能  写在类中的函数
成员方法   成员函数
'''
name = "123"  # 普通的全局变量，属于模块内容
def eat():    # 普通的函数，属于模块内容
    pass

'''
创建类：
语法规则：
class 类名(父类列表):
    成员属性(个数不定)
    成员方法(个数不定)
解释说明：
1、class : 创建类的关键字，不能省略
2、类名：遵循标识符的命名规则。建议：单词的第一个字母大写，
一般情况下一个类的类名就是一个单词
3、() : 父类列表的开始与结束，如果没有父类列表，不能省略。
4、父类列表：不同的父类用逗号(,)隔开。
5、: ：类的开始
6、成员属性：变量
7、成员方法：函数(类中的方法至少有一个形参，该形参名称默认为self)

注：class只是一种数据类型，不占用内存，之前的数据类型:list  str tuple...
通过类创建的变量(对象)是占内存的，存在内存地址。
'''
# 创建一个Student类
class Student():
    # 定义成员属性(变量)
    # 创建成员属性时要同时赋予初始值
    name = "Lily"
    age = 19
    # 定义成员方法(函数/行为)
    # 默认至少有一个形参self
    # self：代表当前类的实例对象
    def studyClass(self):
        print("study各种学科")

'''
类名：Wife
属性：name  height  weight
方法：购物   做家务   藏私房钱(钱的数量)

类名：Husband
属性：faceValue  height  
方法：做饭   找私房钱(钱的数量)

类名：电脑
属性：color  price  
方法：玩游戏  写代码   关机  开机
'''
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
class Husband():
    faceValue = 6.0
    height = 1.6
    def makeCooking(self):
        print("男士做饭")
    def findMoney(self,money):
        print("轻松找到了%s的私房钱" % money)
class Computer():
    color = "white"
    price = 1000
    def playGame(self):
        print("可以用来打游戏")



