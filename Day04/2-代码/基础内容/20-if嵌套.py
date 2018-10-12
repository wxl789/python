# 相亲
sex = input("请输入性别：")
if sex == "男":
    print("开始见面")
    face = input("颜值？")
    height = input("身高？")
    money = input("积蓄多少？")
    if face=="帅" and height=="1.80" and money=="1":
        print("约一下")
        if 1:
            print("领证")
    elif face=="帅" or height=="1.80" or money=="1":
        print("蓝朋友")
    else:
        print("好人")
else:
    print("我妈拒绝了")
