import os
"""
os--->模块文件的操作：

listdir()：获取当前目录下所有的文件
path:路径
join：完成拼接
isdir():判断是否是文件
"""
def getAllDirRE(path,sp = ""):#参数 路径   返回值:None
    #完成功能，获取调用者传递路径下的所有的文件（文件《直接显示》，文件夹《二次遍历》）
    #1.得到当前目录所有的文件
    filesList = os.listdir(path)
    #2.遍历获取filesList中数据
    sp += "  "
    for fileName in filesList:
        #判断是否是路径（绝对路径）
        fileAbsPath = os.path.join(path,fileName)
        #判断
        if os.path.isdir(fileAbsPath):
            print(sp+"目录：",fileName)
            #递归调用
            getAllDirRE(fileAbsPath,sp)

        else:
            print(sp+"普通的文件：",fileName)
getAllDirRE(r"F:\untitled")