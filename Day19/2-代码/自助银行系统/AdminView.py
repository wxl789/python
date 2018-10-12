import time
def printWelcomeView():
    print("***********************************")
    print("*                                 *")
    print("*         欢迎进入潘潘银行        *")
    print("*         这是世界最大银行        *")
    print("*                                 *")
    print("***********************************")
    time.sleep(2)

# 一般当程序有错误时，函数一般返回-1或1；当功能正常，函数一般返回0
# 登陆账号及密码
def checkUserAndPassword():
    # 用户输入账号及密码
    inputUser = input("请输入账号:")
    if inputUser != "1":
        print("账号不存在！！！")
        return -1
    inputPass = input("请输入密码:")
    if inputPass != "1":
        print("密码错误！！！")
        return -1
    print("登陆成功，请稍后...")
    time.sleep(2)
    return 0

# 主程序选择提示页面
def mainFunctionView():
    print("请选择您需要进行的操作")
    print("***********************************")
    print("      开户(1)        查询(2)       ")
    print("      取款(3)        存款(4)       ")
    print("      改密(5)        补卡(6)       ")
    print("      锁定(7)        解锁(8)       ")
    print("      销户(9)        退出(0)       ")
    print("              转账(z)              ")
    print("***********************************")



