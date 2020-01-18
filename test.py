# -*- coding: utf-8 -*-

'''
import  tkinter  as  tk   #导入Tkinter模块，仅用于Python3

#移动窗口到屏幕中央       
def setCenter(window,w=0,h=0):
    window.update()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    if (w==0 or h==0):
        w = window.winfo_width()   #获取窗口宽度（单位：像素）
        h = window.winfo_height()  #获取窗口高度（单位：像素）
    x = int( (ws/2) - (w/2) )
    y = int( (hs/2) - (h/2) )
    window.geometry('{}x{}+{}+{}'.format(w, h, x, y))

root =tk.Tk()  #建立Tkinter主窗口root
root.title(' Tk窗口')
root.geometry('{}x{}+{}+{}'.format(300, 200, 100, 200)) #改变窗口位置和大小
root.attributes('-topmost',1)  #参数1，设置顶层窗口，覆盖其它窗口。

popWindow=tk.Toplevel(root)
popWindow.title('Toplevel窗口')
popWindow.geometry('{}x{}+{}+{}'.format(300, 200, 450, 200)) #改变窗口位置和大小
popWindow.attributes("-toolwindow", 1)  #参数1，设置工具栏样式窗口。
popWindow.attributes('-topmost',1)  #参数1，设置顶层窗口，覆盖其它窗口。

setCenter(popWindow)  #把popWindow窗口移动到屏幕中央

root.mainloop()  #Tkinter的mainloop()方法

'''


# -*- coding: utf-8 -*-
import  tkinter  as  tk   #导入Tkinter
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
import  tkinter.tix  as  tix   #导入Tkinter.tix
from  tkinter.constants  import  *   #导入Tkinte常量，W和tk.W,tix.W都可用。

root = tix.Tk()   #创建tix.Tk()主窗口

width=300  #把窗口宽度(单位:像素)300赋值给变量width

height=200  #把窗口高度(单位:像素)300赋值给变量height
x,y=150,250  #给屏幕坐标(x,y)赋值(100,200)
root.geometry('{}x{}+{}+{}'.format(width,height, x, y))  #改变窗口位置和大小
root.title("Tix的Form布局演示")
la=tk.Label(root, text='tk_la_form',relief=SUNKEN, bd=1)  #创建tk.Label
la.form(top=50, left=50,right=None,bottom=None)   #用form方法显示

lb=ttk.Label(root, text='ttk_lb_form')  #创建ttk.Label
lb.form(top=100, left=50,right=None,bottom=None)   #用form方法显示

lc=tix.Label(root, text='tix_lc_form',relief=tk.SUNKEN, bd=1)  #创建tix.Label
lc.form(top=150,left=50)    #用form方法显示

ld=tix.Label(root, text='tix_ld_place',relief=tix.SUNKEN, bd=1)   #创建tk.Label
ld.place(x=150,y=100)   #用place方法显示

root.mainloop()   #开启tk主循环
