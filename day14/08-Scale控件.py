
"""
供用户通过拖拽指示器改变变量的值
水平
垂直
"""
import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")
#开始值0，结束值100，方向
scale = tkinter.Scale(window,from_=0,to=100,
              orient= tkinter.HORIZONTAL,tickinterval=100,length=200)

scale.pack()

#设置初始化值set
scale.set(20)

window.mainloop()

