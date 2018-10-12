import random
from day14.银行管理系统.card import Card
from day14.银行管理系统.user import User

class ATM(object):
    def __init__(self,allUsers):
        self.allUsers = allUsers#卡号--用户

    #开户,封装一个方法
    def createUser(self):
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号：")
        phone = input("请输入您的手机号：")

        #设定预存的金额
        perstoreMoney = int(input("请输入预存的金额："))
        if perstoreMoney < 0:
            print("预存的金额输入有误，需要重新的输入")
            return -1

        #设置密码
        onePasswd = input("请输入密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入有误，开户失败....")
            return -1
        #所有的需要的信息全了
        cardStr = self.randomCardId()
        card = Card(cardStr,onePasswd,perstoreMoney)
        user = User(name,idCard,phone,card)
        #存到用户字典
        self.allUsers[cardStr] = user
        print("开户成功！！请牢记卡号（%s）...."%(cardStr))

    #查询
    def searchUserInfo(self):
        #根据卡号进行查询
        cardNum = input("请输入您的卡号：")
        #验证是否存在卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！查询失败")
            return -1

        #判断卡是否锁定
        if user.card.cradLock:
            print("该卡已被锁定,请解锁后进行其他的操作...")
            return -1


        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！该卡已被锁定！！请解锁后进行其他的操作...")
            user.card.cradLock = True
            return -1

        print("账号：%s   余额：   %d"%(user.card.cardId,user.card.CardMoney))

    #取款
    def getMoney(self):
        cardNum = input("请输入卡号：")
        # 验证是否存在卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！查询失败")
            return -1

        #判断卡是否锁定
        if user.card.cradLock:
            print("该卡已被锁定,请解锁后进行其他的操作...")
            return -1


        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！该卡已被锁定！！请解锁后进行其他的操作...")
            user.card.cradLock = True
            return -1

        #输入取款的金额
        money = int(input("请输入取款的金额："))
        if money > user.card.CardMoney:
            print("余额不足！取款失败...")
            return -1

        #取款
        user.card.CardMoney -= money
        print("取款成功！！，余额：%d"%(user.card.CardMoney))


    #存款---》和取款一样，，-=  +=
    def saveMoney(self):
        pass
    #转账：事务，A   B
    def transferMoney(self):
        pass
    #改密   card ---属性
    def changePasswd(self):
        pass
    #锁定：
    def lockUser(self):
        cardNum = input("请输入卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！锁定失败....")
            return -1

        if user.card.cradLock:
            print("该卡已经锁定，请解锁后完成其他的功能...")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，锁定失败...")
            return -1

        tempIdCard = input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入有误！！锁定失败.....")
            return -1

        #锁定
        user.card.cradLock = True
        print("锁定成功....")

    #解锁
    def unlockUser(self):
        pass












    #alt+enter验证密码，6，随机生产一个6为数的数字密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请再次输入密码：")
            tempPasswd == realPasswd
            return True
        return False

    #生产卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord("0"),ord("9")+1))
                str += ch

            #判断是否重复
            if not self.allUsers.get(str):
                return str























