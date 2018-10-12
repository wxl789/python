

"""
SpinBox
数值范围控件
"""
import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

def updata():
    print(v.get())

#绑定数据
v = tkinter.StringVar()
#increment:步长
#创建SpinBox,
sp = tkinter.Spinbox(window,from_=0,to=100,
                increment=1,textvariable=v,command=updata)

#设置默认值
# set

sp.pack()
v.set(20)
window.mainloop()



