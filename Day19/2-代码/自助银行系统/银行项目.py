# 当前项目的入口

# 设计欢迎页面  -->  登陆页面   -->  主程序功能选择页面
# 声明文件的运行函数
import time
import AdminView
import Bank
import pickle, os

def main():
    # 欢迎页面
    AdminView.printWelcomeView()
    # 进入登陆页面
    if AdminView.checkUserAndPassword() == -1:
        return -1

    # 获取用户信息：通过本地文件读取已存在用户列表
    # allUser.txt:存储用户信息的文件
    # 假设用户数量为空
    allUser = {}
    if os.path.getsize("allUser.txt") > 0:
        with open("allUser.txt", "rb") as f1:
            # 已经存在用户
            allUser = pickle.load(f1)
    print(allUser)
    # 银行的对象只有一个
    bank = Bank.Bank(allUser=allUser)
    # 进入主程序页面
    while True:
        time.sleep(1)
        AdminView.mainFunctionView()
        checkFunc = input("请按照数字输入选择的功能")
        if checkFunc == "1":
            bank.createUser()
        elif checkFunc == "2":
            bank.seachUser()
        elif checkFunc == "3":
            bank.getMoney()
        elif checkFunc == "4":
            bank.saveMoney()
        elif checkFunc == "5":
            bank.changePassword()
        elif checkFunc == "6":
            bank.createOtherCard()
        elif checkFunc == "7":
            bank.lockedCard()
        elif checkFunc == "8":
            bank.unlockedCard()
        elif checkFunc == "9":
            bank.cancelUser()
        elif checkFunc == "z":
            bank.transferMoney()
        elif checkFunc == "0":
            # 存入或更新数据
            with open("allUser.txt", "wb") as f1:
                pickle.dump(bank.allUser ,f1)
            return 0
        else:
            print("输入错误，请确认后重新输入")




if __name__ == "__main__":
    main()





