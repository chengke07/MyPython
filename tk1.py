import tkinter as tk

app = tk.Tk()   #TOP顶层窗口,root窗口
app.title('chengke07')

theLabel = tk.Label(app,text='我的第一个窗口程序！')
theLabel.pack() #用于自动调整组件的尺寸位置

app.mainloop()  #窗口的主事件循环