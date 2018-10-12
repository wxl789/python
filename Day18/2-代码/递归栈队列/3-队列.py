'''
队列：先进先出
'''

# 创建队列
import collections
queue = collections.deque()
# 进队
queue.append(1)
queue.append(2)
queue.append(3)
# 出队
queue.popleft()
print(queue)

# 队列遍历目录为广度遍历