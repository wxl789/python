"""
1.用函数完成下面的功能：
    1.1 计算用户通过键盘录入数据中字符出现的个数，
        展示时以key = value的格式在控制台打印
        input---->String
        dict

        raw_input
"""
#获取用于键盘录入的数据
# str = input("请输入数据：")#string--->序列---》遍历---》比对
# #定义一个字典
# dict = {}
# def getdict(str):#参数  返回值  key：value--->key  value
#     #遍历
#     for temp in str:#count  key:chr  value:count
#         dict[temp] = str.count(temp)
#     return dict
#
# aa = getdict(str)
# #遍历获取所有的key  value
# for key,value in aa.items():
#     print(key + "=",value,end=" ")

"""        
        
    1.2 获取用户输入的内容，并存放到列表中，检查传入列表数据的长度，如果大于2，
       那么仅保留前两个长度的内容，并将新内容返回给调用者。
       
       input
       append
       len
       if  > 2   切割   [start,stop step],左闭右开
"""
# str = input("请输入数据：")
# #定义列表
# list = []
# #定义一个函数完成题干
# def getList(str):
#     #添加数据
#     list.append(str)
#     #遍历
#     for temp in list:
#         if len(temp) > 2:
#             temp1 = temp[0:2]
#
#         else:
#             temp1 = temp
#
#     return temp1
# aa = getList(str)
# print(aa)

"""
2.使用递归函数完成9*9乘法表
"""
#方式1：
# def demo(num):
#     for i in range(1,num + 1):
#         for j in range(1,i + 1):
#             print("%d * %d = %d"%(j,i,i*j),end="  ")
#         print("")
#
# demo(9)
#递归---》
# def demo(num):
#     i = 10-num
#     if num > 0:
#         j = 1
#         while j < i + 1:
#             print("%d * %d = %d"%(j,i,i*j),end="  ")
#             j += 1
#
#         print("")
#         demo(num - 1)
# demo(9)

"""

3.编写“学生管理系统”，要求如下：
必须使用自定义函数，完成对程序的模块化
学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询（单个查询/显示所有）、退出

键盘录入的方式：
  1：添加
  2：删除
  3：修改
  4：查询一个
  5：查询所有
  6：退出
  
  存储数据：  key:value name:张三----》list
"""
#定义一个列表，用于存储学生信息
stu_infors = []
#用于显示功能菜单
def print_menu():
    print("="*50)
    print("学生管理系统  v 1.0")
    print("1:添加一个新的学生信息")
    print("2:删除一个新的学生信息")
    print("3:修改一个新的学生信息")
    print("4:查询一个新的学生信息")
    print("5:查询所有新的学生信息")
    print("6:退出学生信息")
    print("=" * 50)


#添加学生信息
def add_new_stu_infor():
    #使用键盘录入的方式
    new_name = input("请输入新的名字：")
    new_qq = input("请输入新的qq：")
    new_weixin = input("请输入新的微信：")
    new_addr = input("请输入新的地址：")

    #定义一个新的字典，用于存储学生信息
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["qq"] = new_qq
    new_infor["weixin"] = new_weixin
    new_infor["addr"] = new_addr

    global stu_infors
    stu_infors.append(new_infor)



#查询一个名片
def find_stu_info():
    global stu_infors
    #根据姓名完成学生信息的数据查询
    find_name = input("请输入需要查询的学生姓名：")
    find_flag = 0#0表示默认没有找到

    #遍历
    for temp in stu_infors:#字典
        if find_name == temp["name"]:
            print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
            find_flag = 1#表示找到
            break
    #表示没有找到
    if find_flag == 0:
        print("查无此人！！！！")

#查询所有
def show_all_infor():
    #显示所有的信息
    global stu_infors
    # 遍历
    for temp in stu_infors:  # 字典
        print("%s\t%s\t%s\t%s" % (temp["name"], temp["qq"], temp["weixin"], temp["addr"]))


def main():
    #完成对整个程序的控制
    #打印菜单
    print_menu()
    while True:
        #2.获取用户的输入
        num = int(input("请输入需要操作的符号（1~6）："))
        #3.根据用户的数据执行相对应的功能操作
        if num == 1:
            add_new_stu_infor()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_stu_info()
        elif num == 5:
            show_all_infor()
        elif num == 6:
            break
        else:
            print("输入有误，请清新输入")

        print("")

main()





















































