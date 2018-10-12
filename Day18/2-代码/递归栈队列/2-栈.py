'''
栈：先进后出
python中不存在栈，我们可以仿写栈的功能。
'''

# 模拟栈
stack = []
# 入栈
stack.append(1)
stack.append(2)
stack.append(3)
# [1,2,3]
# 出栈
stack.pop()
print(stack)
stack.pop()
print(stack)

# 栈遍历目录为深度遍历
'''
a --> f1.txt  b  c
b --> f2.txt   d
c --> f3.txt   e
d --> f4.txt
e --> f5.txt
[a] [b c]  [b e] [b]

'''



