

import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

def updata():
    message = ""
    if hobby1.get() == True:
        message += "money\n"

    if hobby2.get() == True:
        message += "power\n"

    if hobby3.get() == True:
        message += "people\n"
    #清除text中所有的内容
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)

#绑定布尔类型的变量
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()
#创建多选框,选中，没有选中  ----》bool
check1 = tkinter.Checkbutton(window,text="money",variable=hobby1,command=updata)
check1.pack()

check2 = tkinter.Checkbutton(window,text="power",variable=hobby2,command=updata)
check2.pack()

check3 = tkinter.Checkbutton(window,text="people",variable=hobby3,command=updata)
check3.pack()



#创建文本框控件
text = tkinter.Text(window,width = 50,height=5)
text.pack()

window.mainloop()