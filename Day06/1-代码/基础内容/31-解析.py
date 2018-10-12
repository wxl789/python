'''
34.幸运猜猜猜： 游戏随机给出一个0-99的数字，然后让你猜是什么数字。
你可以对边猜一个数字，游戏会提示太大或者太小，从而缩小结果范围。
经过几次猜测与提示后，最终推出答案。在游戏过程在中，
记录你最终猜对是所需要的次数，游戏结束后公布结果。
猜测次数最多20次。
'''
'''
import random
right = random.randint(0, 99)
count = 20
print(right)
start = 0
stop = 99
while True:
    if count > 0:
        count -= 1
        num = int(input("请输入猜测数字"))
        if num == right:
            print("恭喜，猜对了，数字就是%d" % right)
            print("您在第%d次猜对了，棒棒哒" % (20-count))
            break
        elif num > right:
            print("过大,范围变成%d-%d之间" % (start, num-1))
            stop = num - 1
            print("您还剩%d次" % count)
        elif num < right:
            print("过小,范围变成%d-%d之间" % (num + 1, stop))
            start = num + 1
            print("您还剩%d次" % count)
    else:
        print("20机会已过，猜数失败")
        break

'''

'''
33. 实现一个课程名称和课程代号的转换器：输入下表中的课程代号，
输出课程的名称。用户可以循环进行输入，如果输入n就退出系统。
1     PHP
2     Python
3     JS
4     JAVA
n     退出
'''

print("请选择书籍编号，编号为1，2，3，4；输入n可退出选择")
while True:
    num = input("请输入编号：")
    if num == "1":
        print("PHP")
    elif num == "2":
        print("Python")
    elif num == "3":
        print("JS")
    elif num == "4":
        print("JAVA")
    elif num == "n":
        print("ByeBye,谢谢使用")
        break
    else:
        print("书籍编号错误，请重新输入")




