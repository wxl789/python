# 复制文件
# 歌词.txt   ---> 歌词副本.txt
import pickle
with open(file="歌词.txt", mode="a",encoding="utf-8") as str1:
    str1.write("充满鲜花的世界到底在哪里\n"
           "如果它真的存在那么我一定会去\n"
           "我想在那里最高的山峰矗立\n"
           "不在乎它是不是悬崖峭壁\n"
           "用力活着用力爱哪怕肝脑涂地\n"
           "不求任何人满意只要对得起自己\n"
           "关于理想我从来没选择放弃\n"
           "即使在灰头土脸的日子里\n")

with open(file="歌词副本.txt",mode="a",encoding="utf-8") as f2:
       pickle.dump(str1,f2)
       f2.close()
