import collections
import os
"""
collections:
deque()


"""
# collections.deque()
def getAllDirRE(path):
    #获取队列对象
    queue = collections.deque()
    #进队
    queue.append(path)

    #循环遍历获取数据
    while len(queue) != 0:
        #出队数据，先进先出
        dirPath = queue.popleft()
        #找到所有的文件
        filesList = os.listdir(dirPath)
        #遍历获取所有的数据
        for fileName in filesList:
            #绝对路径
            fileAbsPath = os.path.join(dirPath,fileName)
            #判断是否是目录，是目录进队，反之直接打印显示
            if os.path.isdir(fileAbsPath):
                print("目录：",fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件："+fileName)

getAllDirRE(r"F:\untitled")

























