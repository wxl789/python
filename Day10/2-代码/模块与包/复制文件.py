# 打开一个已经存在的文件
f1 = open(file="歌词.txt",mode="r",encoding="utf-8")
str1 = f1.read()
f1.close()


# 写入一个新的文件
f2 = open(file="歌词副本.txt",mode="w",encoding="utf-8")
f2.write(str1)
f2.close()



