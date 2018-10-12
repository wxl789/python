

import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

def updata():
    print(r.get())
r = tkinter.IntVar()

#创建单选按钮的控件
radio1 = tkinter.Radiobutton(window,text="one",value = 44,variable=r,command=updata)
radio1.pack()

radio2 = tkinter.Radiobutton(window,text="two",value = 55,variable=r,command=updata)
radio2.pack()
radio3 = tkinter.Radiobutton(window,text="three",value = 66,variable=r,command=updata)
radio3.pack()

window.mainloop()




