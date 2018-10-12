# 人射击子弹

# 默认手枪中有4发子弹，人射击4次之后就没有了，每射击一次提示目前
# 还剩几发子弹，当全部射击没之后，再执行射击的操作时，提示没有子弹了，
# 人可以再次填装n发子弹，再次射击n次之后就没有了。

class Shootingbullets():
# 人：
# 类名：Person
# 属性：手枪  gun
# 行为：fire  addCount
    def Person(self):
        print("是否射击" )
# 枪：
# 类名：Gun
# 属性：弹夹  bulletBox
# 行为：shoot
    def Gun(self):
        bullet = 0
        for bullet in range(5):
            if bullet <5 :
                print("射击" )
            else:
                print("没子弹了" )
        bullet += 1

# 弹夹：
# 类名：BulletBox
# 属性：bulletCount
        def Bulletbox(self):
            print(int(input("更换弹夹")))

person1 = Shootingbullets()
person1.Person()
person1.Gun()
# 864659104@qq.com
# class Shootingbullets():
#     def Person(self):
#         print(int(input("是否射击")))
#     def Gun(self):
#         if
#         print(int(input("射击")))
#     def Bulletbox(self):
#         print(int(input("更换弹夹")))
#
# person1 = Shootingbullets()
# person1.Person()
# person1.Gun()