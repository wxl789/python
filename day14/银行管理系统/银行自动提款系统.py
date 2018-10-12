import os

from day14.银行管理系统.admin import Admin
from day14.银行管理系统.atm import ATM
import pickle#对python对象结构进行二进制序列化和反序列化的协议的实现，python数据编程流的形式


def main():
    #创建管理员的对象
    admin = Admin()
    admin.printAdminView()
    if admin.adminOption():
        return -1

    #提款机的对象getcwd():获取当前的路径
    filepath = os.path.join(os.getcwd(),"allusers.txt")
    #打开文件
    f = open(filepath,"rb")
    #加载
    allUsers = pickle.load(f)

    print(allUsers)

    #功能atm
    atm = ATM(allUsers)
    while True:
        admin.printSysFuncationView()
        #等待用户的操作
        option = input("请输入你的操作：")
        if option == "1":
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()

        elif option == "4":
            atm.saveMoney()

        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            print("解锁")
        elif option == "9":
            print("补卡")
        elif option == "10":
            print("销户")
        elif option == "t":
            if not admin.adminOption():
                #将当前系统中的用户信息保存到文件中
                f = open(filepath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()
                return -1

main()


















