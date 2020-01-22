from tkinter import *
from tkinter import ttk
from DragWindow import DragWindow
import pyautogui
import threading
import time
import win32gui
import win32con


root = DragWindow()
#root.set_window_size(200, 200)
#root.set_display_postion(500, 400)
frame = Frame(root,)
frame1=Frame(root,)
frame2=Frame(root,)
frame.pack(fill=X)
frame1.pack(fill=X)
frame2.pack(fill=X)

str1=StringVar()
str1.set('键盘扫描：')
LB1 = Label(frame1,textvariable=str1,width=20,anchor=W)
LB1.pack(fill=X)

str2=StringVar()
str2.set('鼠标X:1920 鼠标Y:1080')
LB2 = Label(frame1,textvariable=str2,width=20)
LB2.pack(side=LEFT)
BT1 = Button(frame1,text='枚举窗口',width=10,)
BT1.pack(side=LEFT)
list1=ttk.Treeview(frame2,height=9,columns=('col1','col2'),show='headings')
list1.column('col1',width=60,anchor='center')
list1.column('col2',width=220,anchor='center')
list1.heading('col1',text='PID')
list1.heading('col2',text='窗口标题')

sb = Scrollbar(frame2)
list1.config(yscrollcommand=sb.set)
sb.config(command=list1.yview)


def treeviewDBClick(event):
    item_text = list1.item(list1.selection(),"values")
    #win32gui.ShowWindow(int(item_text[0]),win32con.SW_SHOW)
    if win32gui.IsIconic(int(item_text[0])):
        win32gui.SendMessage(int(item_text[0]), win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
        win32gui.SetForegroundWindow(int(item_text[0]))
    else:
        win32gui.SendMessage(int(item_text[0]), win32con.WM_SYSCOMMAND, win32con.SC_ICON, 0)
    #win32gui.BringWindowToTop(int(item_text[0]))
    #print(item_text[0])
    #win32gui.SetActiveWindow(int(item_text[0]))
    

def hide():
    #root.state('withdrawn')
    sw = root.winfo_screenwidth()
    ww = root.winfo_width()
    h = root.winfo_height()
    x=root.winfo_x()
    y=root.winfo_y()
    
    if(x==(sw-ww)):
        root.geometry('+{}+{}'.format(sw-10,y))
        time.sleep(0.2)
        return
       
def show():
    #root.state('withdrawn')
    sw = root.winfo_screenwidth()
    ww = root.winfo_width()
    h = root.winfo_height()
    x=root.winfo_x()
    y = root.winfo_y()
    if(x>(sw-ww)):
        root.geometry('+{}+{}'.format(sw-ww,y))
        time.sleep(0.2)
        return







list1.bind('<Double-1>', treeviewDBClick)#绑定单击离开事件===========






def closelist():
    list1.forget()
    frame2.forget()
    BT1['text']='枚举窗口'
    BT1['command']=showlist


def showlist():
    frame2.pack(fill=X)
    sb.pack(side=RIGHT,fill=Y)
    list1.pack()
    root.update()
    BT1['text']='刷新'
    BT1['command']=get_allwin
    get_allwin()
    
BT1['command']=showlist

BT2 = Button(frame1,text='关闭枚举',width=10,command=closelist)
BT2.pack(side=LEFT)

root.resizable(0,0) #禁止调整窗口大小。
#Button(root, text="Exit",command=root.quit).pack(side=BOTTOM,anchor=E)
#保护措施，避免失控
#pyautogui.FAILSAFE = True
#为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
#pyautogui.PAUSE = 0.5

root.update()
sw = root.winfo_screenwidth()#得到屏幕宽度
sh = root.winfo_screenheight()#得到屏幕高度
ww = root.winfo_width()
wh = root.winfo_height()
x=sw-ww
y=sh-wh


def OnMouseEvent():
    while True:
        time.sleep(0.02)
        currentMouseX, currentMouseY = pyautogui.position()
        str2.set('鼠标X:%d 鼠标Y:%d' % (currentMouseX,currentMouseY))
        ww = root.winfo_width()
        wh = root.winfo_height()
        x= root.winfo_x()
        y = root.winfo_y()
        #print(x,y,ww,wh)
        if (x==sw-ww)and((currentMouseX<x)or(currentMouseY>(wh+y+30))or(currentMouseY<y)):
            hide()
        elif (x>=sw-10)and(currentMouseX>sw-10)and(currentMouseY<wh+y+30)and(currentMouseY>y):
            show()



s='窗口管理器------>屏幕大小：%d X %d' %(sw,sh)
root.title(s)
#geometry("%dx%d+%d+%d" %(ww,wh,x,y))# 窗口居中放置
root.geometry("+%d+%d" %(x,0))        

 


def get_allwin():
    hwnd_title = dict()
    def get_all_hwnd(hwnd,mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)
    i=0
    x=list1.get_children()
    for item in x:
        list1.delete(item)
    for h,t in hwnd_title.items():
        if (t is not "") and (t !="Program Manager") and (t != "dummyLayeredWnd")and(t!='SCM')and(t!='Microsoft Edge')\
        and(t!='Microsoft Text Input Application')and(t!=s):
            list1.insert('',i,values=(h,t))
            i+=i
    list1.update()


              
        

th=threading.Thread(target=OnMouseEvent)
th.setDaemon(True)
th.start()



root.mainloop()
