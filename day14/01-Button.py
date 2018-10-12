"""
button--->按钮
按钮功能：
   当点击按钮时发生对应的事
"""
import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

def func():
    print("haha")

#创建按钮
button1 = tkinter.Button(window,text = "按钮1",command = func)
button2 = tkinter.Button(window,text = "按钮2",command = window.quit)

button1.pack()
button2.pack()

window.mainloop()









