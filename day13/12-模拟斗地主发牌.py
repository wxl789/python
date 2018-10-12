"""
模拟斗地主发牌
有3个玩家  一付扑克牌  ，留三张
将扑克牌随机分配给3个玩家并显示（四种花色，两个王）

栈   54   3   51    17   A ~ K

random

class

type
"""
import random

pai = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
huase = ["♥","♠","♣","♦"]
wang = ["🃏","🃏"]

#定义玩家
wan1 = []
wan2 = []
wan3 = []

#牌面和花色的拼接循环嵌套

for x in huase:
    for y in pai:
        s = x + y
        wang.append(s)

#洗牌
random.shuffle(wang)

#发牌
i = 1
while i <= 17:
    wan1.append(wang.pop())
    wan2.append(wang.pop())
    wan3.append(wang.pop())
    i += 1

print(wan1)
print(wan2)
print(wan3)
print(wang)






















