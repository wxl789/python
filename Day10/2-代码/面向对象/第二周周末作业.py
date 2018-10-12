# 人射击子弹

# 默认手枪中有4发子弹，人射击4次之后就没有了，每射击一次提示目前
# 还剩几发子弹，当全部射击没之后，再执行射击的操作时，提示没有子弹了，
# 人可以再次填装n发子弹，再次射击n次之后就没有了。

'''
人：
类名：Person
属性：手枪  gun
行为：fire  addCount
枪：
类名：Gun
属性：弹夹  bulletBox
行为：shoot
弹夹：
类名：BulletBox
属性：bulletCount
'''
# 864659104@qq.com
'''
class Person():
    def fireGun(self,gun):
        print("")
class Gun():
    def bulletBox(self,count = 4):
        print("开火")
class BulletBox():
    def getBulletBox(self,bulletCount):
        print("")
count1 = 4
while count1<=4:
    print("是否射击")
'''
    
    





class Shootingbullets():
    def Person(gun):
            print(input("是否射击"))
            print("开始射击")

class BulletBox():
    def getBulletBox(self,bulletCount):
# def Bluuetbox(bulletCount):
        print("更换弹夹")
        print("装弹成功")

class Gun():
    def getGun(bulletBox):
        pass
bullet1 = 4

while bullet1 > 0:
    print("射击", "还有%s颗子弹" % (bullet1-1))
    bullet1 -= 1
else:
    print("没子弹了，需要装弹",intinput(("装了%s颗子弹" % bullet1)))
    # print(input("装了%s颗子弹" % bullet1))

