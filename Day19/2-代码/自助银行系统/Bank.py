# 银行
# 银行---> 开户。。。。
# 管理所有已存在的用户的变量
# 开户  查询等功能
# 多个用户
# 用户--银行卡，密码，用户名。。。。
# [1,2,3]
# {key:value}   ==> 卡号：用户对象
# allUser ==> {cardID:user}

from User import User
from Card import Card
import random

class Bank():
    def __init__(self, allUser):
        # 管理已存在的用户
        self.allUser = allUser
    # 创建用户
    def createUser(self):
        print("开户，请注意输入信息格式， ready go")
        # 从控制台输入各种信息
        name = input("请输入姓名：")
        phone = input("请输入手机号：")
        idcard = input("请输入身份证号：")
        # 随机生成一个卡号
        cardID = self.createCardID()
        # 设置密码
        password = input("请设置密码：")
        password1 = input("请确认密码：")
        # 判断两次密码是否一致
        if password != password1:
            print("两次密码不一致，开户失败")
            return -1
        money = int(input("请输入预存金额："))
        # 判断金额是否正确
        if money < 0:
            print("存入金额有误，开户失败")
            return  -1

        # 创建银行卡对象
        card = Card(cardID=cardID, password=password, money=money)
        # 实例化用户对象
        user = User(name=name,phone=phone,idcard=idcard,card=card)
        # 将新的用户存入用户列表  {}
        self.allUser[cardID] = user
        print("开户成功，请记住卡号：%s" % cardID)




    # 随机生成银行卡号
    def createCardID(self):
        # 随机
        while True:
            str1 = ""
            for i in range(6):
                ch = str(random.randrange(0, 10))
                str1 += ch
            # 判断str1是否与之前的卡号有重复
            if self.allUser.get(str1) == None:
                # 返回卡号
                return str1

    # 查询用户
    def seachUser(self):
        # print(self.allUser)
        # 查询某个卡中的金额。。。
        cardID = input("请输入查询的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，查询失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，请解锁后查询")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡被锁定")
            # 锁定
            self.allUser[cardID].card.lock = True
            return -1
        print("卡号%s,余额%d" % (cardID, self.allUser[cardID].card.money))


    def getMoney(self):
        cardID = input("请输入取款的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        # 取款
        money = int(input("请输入取款金额："))
        # 判断余额与取款金额
        if money > self.allUser[cardID].card.money:
            print("余额不足，操作失败")
            return -1
        if money < 0:
            print("请输入有效金额，不要调皮，操作失败")
            return -1
        # 取款
        self.allUser[cardID].card.money -= money
        print("取款成功，当前余额为%d" % self.allUser[cardID].card.money)


    def saveMoney(self):
        cardID = input("请输入存款的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        # 存款
        money = int(input("请输入存款金额："))
        if money < 0:
            print("请输入有效金额，不要调皮，操作失败")
            return -1
        # 存款
        self.allUser[cardID].card.money += money
        print("存款成功，当前余额为%d" % self.allUser[cardID].card.money)

    def changePassword(self):
        cardID = input("请输入改密的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        # 更新密码
        password = input("请输入新密码：")
        # 请确认新密码
        password1 = input("请确认新密码：")
        if password != password1:
            print("密码确认失败，操作失败")
            return -1
        # 更新数据库中的密码
        self.allUser[cardID].card.password = password
        print("改密成功")

    def createOtherCard(self):
        cardID = input("请输入补卡的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        yn = input("是否确认补卡  y/n")
        if yn == "y":
            # 重新生成卡号
            newCard = self.createCardID()
            # 更新卡号
            self.allUser[cardID].card.cardID = newCard
            # 使用新卡号创建一个用户
            self.allUser[newCard] = self.allUser[cardID]
            # 自己写设置新的卡号的密码
            # 删除旧卡号
            del self.allUser[cardID]
            print("补卡成功，新的卡号为%s" % newCard)
        else:
            print("取消补卡")



    # 锁定
    def lockedCard(self):
        cardID = input("请输入锁定的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        idcard = input("请输入身份证号：")
        if idcard != self.allUser[cardID].idcard:
            print("身份验证错误，操作失败")
            return -1
        # phone  name
        # 锁定
        self.allUser[cardID].card.lock = True
        print("锁卡成功")


    # 解锁
    def unlockedCard(self):
        cardID = input("请输入解锁的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == False:
            print("该卡未被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            return -1
        idcard = input("请输入身份证号：")
        if idcard != self.allUser[cardID].idcard:
            print("身份验证错误，操作失败")
            return -1
        # 解锁
        self.allUser[cardID].card.lock = False
        print("解锁成功")

    def cancelUser(self):
        cardID = input("请输入销户的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1
        yn = input("是否确认销户  y/n")
        if yn == "y":
            # 删除
            del self.allUser[cardID]
            # self.allUser.pop(cardID)
            print("销户成功")
        else:
            print("取消销户")



    def transferMoney(self):
        cardID = input("请输入取款的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID) == None:
            print("卡号不存在，操作失败")
            return -1
        # 当卡号存在时：
        # 卡是否被锁住
        if self.allUser[cardID].card.lock == True:
            print("该卡已被锁定，操作失败")
            return -1
        # 密码是否输入正确
        # 输入错误次数是否大于3
        if self.checkPassword(realPass=self.allUser[cardID].card.password) == -1:
            print("输入密码错误次数过多，该卡已被锁定")
            self.allUser[cardID].card.lock = True
            return -1

        cardID1 = input("请输入存款的卡号：")
        # 判断卡号是否存在
        if self.allUser.get(cardID1) == None:
            print("卡号不存在，操作失败")
            return -1
        name = input("请输入存款的用户名：")
        if name != self.allUser[cardID1].name:
            print("用户名与卡号不匹配，操作失败")
            return -1
        money = int(input("请输入转账金额："))
        # 判断余额与取款金额
        if money > self.allUser[cardID].card.money:
            print("余额不足，操作失败")
            return -1
        if money < 0:
            print("请输入有效金额，不要调皮，操作失败")
            return -1
        # 取款
        self.allUser[cardID].card.money -= money
        self.allUser[cardID1].card.money += money
        print("转账成功，余额为%d" % self.allUser[cardID].card.money)










    # 三次错误机会
    def checkPassword(self, realPass):
        for i in range(3):
            password = input("请输入密码：")
            if password == realPass:
                return 0
        return -1


