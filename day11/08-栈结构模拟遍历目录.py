import os
#封装一个函数，用于获取指定目录下的所有文件
def getAllDirRE(path):
    #定义一个列表
    stack = []
    stack.append(path)
    #处理栈，当栈为空时结束循环
    while len(stack) != 0:
        #从栈里去数据
        dirPath = stack.pop()
        #获取目录下所有的文件
        filesList = os.listdir(dirPath)
        #处理每一个文件，如果是普通的文件可以直接显示打印，如果是文件夹将目录的地址进栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath,fileName)
            #判断
            if os.path.isdir(fileAbsPath):
                #如果是目录就进栈
                print("目录："+fileName)
                stack.append(fileAbsPath)
            else:
                print("普通："+fileName)
getAllDirRE(r"F:\untitled")















