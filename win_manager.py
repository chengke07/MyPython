'''
@Author: your name
@Date: 2019-12-31 17:20:11
@LastEditTime : 2019-12-31 23:52:08
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\MyTools.py
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import threading,queue
import serial_com
import webbrowser
import time
import pythoncom
import PyHook3


# 主窗
class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.notify_queue = queue.Queue()
        #self.pack() # 若继承 tk.Frame ，此句必须有！
        self.title('窗口管理')
        # 程序参数/数据       
        self.overrideredirect(False)  #参数True，隐藏窗口标题栏。
        
        # 程序界面
        self.setupUI()
    def setupUI(self):
        

        self['bg'] = '#DAA520'
        
        self.attributes("-toolwindow", 1)
        self.option_add('*Font', '微软雅黑 12 bold')
        self.attributes("-topmost", -1)
        self.attributes("-alpha",0)

        self.LB1 = Label(self,text='窗口管理器')
        self.LB1.pack(side=LEFT)
        self.BT1 = Button(self,text='枚举窗口')
        self.BT1.pack(side=LEFT)

       

        



        self.update()
        sw = self.winfo_screenwidth()#得到屏幕宽度
        sh = self.winfo_screenheight()#得到屏幕高度
        ww = self.winfo_width()
        wh = self.winfo_height()
        x=sw-ww
        y=sh-wh
        
        #self.geometry("%dx%d+%d+%d" %(ww,wh,x,y))# 窗口居中放置
        self.geometry("+%d+%d" %(x,0))        
        self.resizable(0,0) #禁止调整窗口大小。
        self.attributes("-alpha",1)
        self.bind('<Alt-End>',self.End)
        self.bind('<Alt-Up>',self.Up)
        self.bind('<Alt-Down>',self.Down)
        self.bind('<Alt-Left>',self.Left)
        self.bind('<Alt-Right>',self.Right)
        
        self.bind('<Enter>',self.show)
        


    def End(self,event):
        self.destroy()
    def Up(self,event):
        x = self.winfo_x()
        y = self.winfo_y()-20
        if y>=0:
            self.geometry('+{}+{}'.format(x,y))  #改变窗口大小
        self.update()
    def Down(self,event):
        sh = self.winfo_screenheight()#得到屏幕高度
        wh = self.winfo_height()
        x = self.winfo_x()
        y = self.winfo_y()+20
        if y<=(sh-wh+20):
            self.geometry('+{}+{}'.format(x,y))  #改变窗口大小
        self.update()
    def Left(self,event):
        x = self.winfo_x()-20
        y = self.winfo_y()
        if x>=-20:
            self.geometry('+{}+{}'.format(x,y))  #改变窗口大小
        self.update()
    def Right(self,event):
        sw = self.winfo_screenwidth()
        ww = self.winfo_width()
        x = self.winfo_x()+20
        y = self.winfo_y()
        if x<=sw-ww:
            self.geometry('+{}+{}'.format(x,y))  #改变窗口大小
        self.update()
    def hide(self,event):
        #self.state('withdrawn')
        sw = self.winfo_screenwidth()
        ww = self.winfo_width()
        h = self.winfo_height()
        x=self.winfo_x()
        y=self.winfo_y()
        
        if(x==(sw-ww)):
            self.geometry('+{}+{}'.format(sw-5,y))
            time.sleep(0.2)
            return
        elif(y==0)and(x<=(sw-ww)):
            self.geometry('+{}+{}'.format(x,-h+5))  #改变窗口大小
            time.sleep(0.2)
            return
    def show(self,event):
        #self.state('withdrawn')
        sw = self.winfo_screenwidth()
        ww = self.winfo_width()
        h = self.winfo_height()
        x=self.winfo_x()
        y = self.winfo_y()
        if(x>(sw-ww)):
            self.geometry('+{}+{}'.format(sw-ww,y))
            time.sleep(0.2)
            return
        elif(y<0):
            self.geometry('+{}+{}'.format(x,y+h-5))  #改变窗口大小
            time.sleep(0.2)
            return
       


        
    def destroy(self):
        super().destroy()
       

def OnMouseEvent(event):
    #print('MessageName:',event.MessageName)
    #print('Message:',event.Message)
    #print('Time:',event.Time)
    #print('Window:',event.Window)
    #print('WindowName:',event.WindowName)
    print('Position:',event.Position)
    #print('Wheel:',event.Wheel)
    #print('Injected:',event.Injected)
    #print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
    return True

def OnKeyboardEvent(event):
    #print('MessageName:',event.MessageName)
    #print('Message:',event.Message)
    #print('Time:',event.Time)
    #print('Window:',event.Window)
    #print('WindowName:',event.WindowName)
    #print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
   #print('KeyID:', event.KeyID)
    #print('ScanCode:', event.ScanCode)
    #print('Extended:', event.Extended)
    #print('Injected:', event.Injected)
    #print('Alt', event.Alt)
    #print('Transition', event.Transition)
    #print('---')

  # return True to pass the event to other handlers
  # return False to stop the event from propagating
    return True

def hook():
    # 创建一个“钩子”管理对象
    # create the hook mananger
    hm = PyHook3.HookManager()
    # register two callbacks
    hm.MouseAllButtonsDown = OnMouseEvent
    hm.KeyDown = OnKeyboardEvent

    # hook into the mouse and keyboard events
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    return True

#def key(event):
#    print(event.char)


if __name__ == '__main__':
      
    app = MyApp()

    th = threading.Thread(target=hook)
    #th.setDaemon(True)
    th.start()
    
    app.mainloop()
    
    