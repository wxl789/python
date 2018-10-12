

import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")
def showInfo():
    print(entry.get())

#创建一个输入框
entry = tkinter.Entry(window)

#创建button
button = tkinter.Button(window,text="按钮",command=showInfo)

entry.pack()
button.pack()

window.mainloop()


