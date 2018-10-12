# 人射击子弹
# 默认手枪中有4发子弹，人射击4次之后就没有了，每射击一次提示目前
# 还剩几发子弹，当全部射击没之后，再执行射击的操作时，提示没有子弹了，
# 人可以再次填装n发子弹，再次射击n次之后就没有了。
class Shootingbullets():
    def Person(gun):
        if True:
            print(input("是否射击"))
            print("开始射击")
    def Gun(bullentBox):
        global bullet1
        bullet1 = 4
        while bullet1 > 0:
            print("射击", "还有%s颗子弹" % (bullet1-1))
                # print("还有%s颗子弹"%bullet1)
            print(input(""))
            bullet1 -= 1
        else:
            print("没子弹了，需要装弹")
    def Bluuetbox(bulletCount):
        print("更换弹夹")
        if True:
            print("装弹成功")


person1 = Shootingbullets()
person1.Person()
person1.Gun()
person1.Bluuetbox()

