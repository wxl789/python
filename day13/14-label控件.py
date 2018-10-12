"""
label:显示文本信息
"""
import tkinter

#创建窗口，Tk
window = tkinter.Tk()

#设置一个标题
window.title("python1805")

#设置窗口的大小和位置geometry()
"""
widthxheight+x+y

widthxheight:窗口的高度和宽度
x+y:窗口的位置
"""
window.geometry("400x400+200+20")

"""
window:父窗体
text:显示文本的内容
bg:背景色
fg:字体颜色
justify:设置换行后的对齐方式
anchor:位置   n  北   e  东   s   南  w  西  center  居中
"""
#创建label控件
label = tkinter.Label(window,text="杭州很美",bg="blue",fg="red",font=("黑体",20),wraplength=100,justify="left",anchor="center")
#显示出来，pack():
label.pack()#pack为一个布局管理器，弹性的容器
#进入消息循环器
window.mainloop()
