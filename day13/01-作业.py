
"""
人开枪
项目分析：
   确定类
   确定对象

1.人类：
属性：
    姓名
    血量
    持有的枪(None)

方法：
    安子弹
    安弹夹
    拿枪（持有抢）
    开枪

2. 子弹类

    属性
        杀伤力
    方法
        伤害敌人(让敌人掉血)


3. 弹夹类

    属性
        容量（子弹存储的最大值）
        当前保存的子弹
    方法
        保存子弹（安装子弹的时候）
        弹出子弹（开枪的时候）

4. 枪类

    属性
        弹夹（默认没有弹夹，需要安装）
    方法
        连接弹夹（保存弹夹）
        射子弹
"""

#人类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name+"剩余的血量："+str(self.xue)

    # 安子弹-->保存子弹---》弹夹
    def anzidan(self,danjia,zidan):
        #保存子弹
        Danjia().baocunzidan(zidan)
    # 安弹夹--->danjia---->qiang
    def andanjia(self,qiang,danjia):
        #连接枪
        qiang.lianjiedanjia(danjia)

    # 拿枪（持有抢）
    def naqiang(self,qiang):
        self.qiang = qiang

    # 开枪
    def kaiqiang(self,diren):
        self.qiang.she(diren)
    #掉血
    def diaoxue(self,shashangli):
        self.xue -= shashangli


#弹夹类===>栈
class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为："+str(len(self.rongnaList))

    # 保存子弹（安装子弹的时候）
    def baocunzidan(self,zidan):
        #判断当前弹夹中是否可以添加子弹
        if len(self.rongnaList) < self.rongliang:
            #条件满足，可以添加子弹
            self.rongnaList.append(zidan)

    # 弹出子弹（开枪的时候）

    def chuzidan(self):
        #判断当前弹夹中是否还有子弹[1,2,3,4,5]
        if len(self.rongnaList) > 0:
            #获取最后入栈的子弹
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None

#子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

#枪类

class Qiang:
    def __init__(self):
        self.danjia = None

    def lianjiedanjia(self,danjia):
        #判断，枪是否有弹夹
        if not self.danjia:
            self.danjia = danjia
    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("没有子弹。放了空枪")

#创建一个人对象
laowang = Ren("老王")

#弹夹
danjia = Danjia(20)

i = 0
while i < 5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i += 1
#创建枪
qiang = Qiang()
laowang.andanjia(qiang,danjia)
laowang.naqiang(qiang)
diren = Ren("敌人")
laowang.kaiqiang(diren)










