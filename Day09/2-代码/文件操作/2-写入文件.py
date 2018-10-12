# 写入文件
# w：重新写入     a：追加写入
'''
1、打开文件
'''
f1 = open(file="a.txt",mode="a",encoding="utf-8")
'''
2、写入内容
'''
# write(str)  将str写入文件
f1.write("\n 你是我的小可爱")
'''
3、关闭文件
'''
f1.close()

# 简写
with open(file="情书.txt", mode="a", encoding="utf-8") as f2:
    f2.write("喜欢你，没道理")



