
"""
text:显示文本信息

"""
import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

#创建Text控件
text = tkinter.Text(window,width = 30,height = 10)
text.pack()
str = "window = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometry"

#insert():插入
text.insert(tkinter.INSERT,str)



window.mainloop()







