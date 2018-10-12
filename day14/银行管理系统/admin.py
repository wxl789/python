import time


class Admin(object):
    #定义用户名
    admin = "1"
    #定义一个密码
    passwd = "1"

    def printAdminView(self):
        print("***********************************")
        print("*                                 *")
        print("*                                 *")
        print("*         欢迎进入XXX银行           *")
        print("*                                 *")
        print("*                                 *")
        print("***********************************")

    def printSysFuncationView(self):
        print("***********************************")
        print("*      开户（1）  查询（2）          *")
        print("*      取款（3）  存款（4）          *")
        print("*      转账（5）  改密（6）          *")
        print("*      锁定（7）  解锁（8）          *")
        print("*      补卡（9）  销户（10）         *")
        print("*            退出（t）              *")
        print("***********************************")

    def adminOption(self):
        #通过键盘录入的方式获取用户输入的数据
        inputAdmin = input("请输入管理员账号：")
        inputPasswd = input("请输入管理账号的密码：")
        #判断用户输入的账号和密码是否正确
        if self.admin != inputAdmin:
            print("账号输入有误！")
            return -1
        if self.passwd != inputPasswd:
            print("密码输入有误！")
            return -1

        #能够执行这行语句，说明账号和密码是正确的
        print("操作成功，请稍后....")
        time.sleep(2)
        return 0
















