

import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

#创建ListBox
lb = tkinter.Listbox(window,selectmode=tkinter.BROWSE)
lb.pack()

#添加元素
for i in ["good","nice","hello","python"]:
    lb.insert(tkinter.END,i)

#在开始的添加
lb.insert(tkinter.ACTIVE,"cool")


# lb.insert(tkinter.ACTIVE,["very good"])

#删除item

lb.delete(1,3)#根据索引下标进行删除

window.mainloop()








