class Shootingbullets():
    def Gun(gun):
        bullet1 = 4
        while bullet1 > 0 :
            print("射击","还有%s颗子弹"%bullet1)
            # print("还有%s颗子弹"%bullet1)
            print(input(""))
            bullet1 -= 1
        else:
            print("没子弹了，需要装弹")
person1 = Shootingbullets()
person1.Gun()