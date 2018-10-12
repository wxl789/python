
import tkinter
window = tkinter.Tk()
window.title("python1805")
window.geometry("400x400+200+20")

#文本控件
text = tkinter.Text(window,width = 30,height = 10)

#创建滚动条   ScrollBar
scroll = tkinter.Scrollbar()

scroll.pack(side= tkinter.RIGHT,fill = tkinter.Y)
text.pack(side=tkinter.LEFT,fill = tkinter.Y)

#设置两个关联config
scroll.config(command = text.yview)
text.config(yscrollcommand=scroll.set)
str = "window = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window.title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window..title(python1805)window.geometrywindow = tkinter.Tk()window."

text.insert(tkinter.INSERT,str)

window.mainloop()



