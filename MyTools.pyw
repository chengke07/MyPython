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
import _thread
import serial_com
import webbrowser

# 弹窗
class MyDialog(Toplevel):
  def __init__(self):
    super().__init__()
    self.title('设置用户信息')
    # 弹窗界面

    self.setup_UI()
  def setup_UI(self):
    # 第一行（两列）
    pass

  def close(self):
    self.destroy()

###网址收藏栏 窗口
class Html_Page(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('网址收藏栏')
        # 弹窗界面
        
        self.setup_UI()
    def setup_UI(self):

        # 创建滚动条，置于窗口右侧，y方向填充
        sb = Scrollbar(self)
        sb.pack(side=RIGHT,fill=Y)
        #self.theLB = Listbox(self,selectmode=SINGLE,height=6,yscrollcommand=sb.set)
        self.theTree = ttk.Treeview(self,show='tree',height=20)
        
        style = ttk.Style()     # Create style
        style.configure("Blue.TFrame", foreground="#DAA520",background="#000000",font=('Fira',12,'bold')) # Set bg color
        self.theTree.config(style='Blue.TFrame')    # Apply style to widget
        #ttk.Style().configure('.',font=('宋体',14))
        self.theTree.config(yscrollcommand=sb.set)
        

        treeF1 = self.theTree.insert("", 0, "百度一下", text="百度一下", values=("F1"))
        treeF2 = self.theTree.insert("", 1, "有道翻译", text="有道翻译", values=("F2"))
        treeF3 = self.theTree.insert("", 2, "硬件设计相关", text="硬件设计相关", values=("F3"))    # #创建一级树目录
        treeF4 = self.theTree.insert("", 3, "软件开发相关", text="软件开发相关", values=("F4"))
        treeF5 = self.theTree.insert("", 4, "休闲娱乐网址", text="休闲娱乐网址", values=("F5"))
        #treeF4 = self.theTree.insert("", 4, "百度一下", text="百度一下", values=("F4"))
        # #二级目录
        treeF3_1 = self.theTree.insert(treeF3, 0, "黄浦区", text="黄浦区hp", values=("F3_1"))  # #将目录帮到菜单treeF1
        treeF3_2 = self.theTree.insert(treeF3, 1, "静安区", text="静安区ja", values=("F3_2"))
        treeF3_3 = self.theTree.insert(treeF3, 2, "长宁区", text="长宁区cn", values=("F3_3"))

        treeF4_1 = self.theTree.insert(treeF4, 0, "苏州", text="苏州sz", values=("F4_1"))  # #将目录帮到菜单treeF2
        treeF4_2 = self.theTree.insert(treeF4, 1, "南京", text="南京nj", values=("F4_2"))
        treeF4_3 = self.theTree.insert(treeF4, 2, "无锡", text="无锡wx", values=("F4_3"))

        #treeF5_1 = self.theTree.insert(treeF5, 0, "AV视听纵情", text="AV视听纵情", values=("F5_1"))  # #将目录帮到菜单treeF3
        treeF5_2 = self.theTree.insert(treeF5, 1, "游戏相关", text="游戏相关", values=("F5_2"))
        treeF5_3 = self.theTree.insert(treeF5, 2, "购物网站", text="购物网站", values=("F5_3"))
        # #三级目录
        #treeF5_1_1 = self.theTree.insert(treeF5_1, 0, "MGSFHK", text="MGSFHK", values=("F5_1_1"))
        #treeF5_1_2 = self.theTree.insert(treeF5_1, 0, "xvideos", text="xvideos视频", values=("F5_1_2"))


        self.theTree.pack()

        def treeviewDBClick(event):
            for item in self.theTree.selection():
                item_text = self.theTree.item(item,"values")               
                if item_text[0]=='F1':
                    webbrowser.open('www.baidu.com')
                if item_text[0]=='F2':
                    webbrowser.open('http://fanyi.youdao.com/')
                #if item_text[0]=='F5_1_1':
                    #webbrowser.open('https://www.99fhk.com/')
                #if item_text[0]=='F5_1_2':
                    #webbrowser.open('https://www.xvideos.com')
            
        sb.config(command=self.theTree.yview)
        self.theTree.bind('<Double-1>', treeviewDBClick)#绑定单击离开事件===========
        
        sw = self.winfo_screenwidth()#得到屏幕宽度
        sh = self.winfo_screenheight()#得到屏幕高度
        ww = 200
        wh =  250
        x = (sw-ww)/2
        y = 0

        self.geometry("%dx%d+%d+%d" %(ww,wh,x,y))# 窗口居中放置
        self.resizable(0,0) #禁止调整窗口大小。

    def close(self):
        self.destroy()    



# 主窗
class MyApp(Tk):
    def __init__(self):
        super().__init__()
        #self.pack() # 若继承 tk.Frame ，此句必须有！
        self.title('MyTools')
        # 程序参数/数据

        self.items = ['网址收藏栏','貂蝉','王昭君','杨玉环','串口通信助手','dr']
        self.items_v = []
        self.overrideredirect(True)  #参数True，隐藏窗口标题栏。
        
        # 程序界面
        self.setupUI()
    def setupUI(self):
        
        self['bg'] = '#000000'
        
        self.attributes("-toolwindow", 1)
        self.option_add('*Font', 'Fira 14')
        self.attributes("-topmost", -1)
        self.attributes("-alpha",0)
        group = LabelFrame(self,text='软件工具集合：',padx=5,pady=5,bg='#000000',fg='#00FF00',)
        group.grid(row=0,column=0,sticky=E+W,padx=5,pady=5,)

        #self.sb = Scrollbar(group)
        #self.sb.grid(row=0,column=1,rowspan=5,sticky=N+S)

        self.items_v.append(IntVar())
        b1=Checkbutton(group,text=self.items[0],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB1,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b1.grid(row=0,column=0,sticky=E+W,padx=0,pady=3,)
        self.items_v.append(IntVar())
        b2=Checkbutton(group,text=self.items[1],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB2,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b2.grid(row=1,column=0,sticky=W+E,padx=0,pady=3,)
        self.items_v.append(IntVar())
        b3=Checkbutton(group,text=self.items[2],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB3,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b3.grid(row=2,column=0,sticky=W+E,padx=0,pady=3,)
        self.items_v.append(IntVar())
        b4=Checkbutton(group,text=self.items[3],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB4,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b4.grid(row=3,column=0,sticky=W+E,padx=0,pady=3,)
        self.items_v.append(IntVar())
        b5=Checkbutton(group,text=self.items[4],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB5,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b5.grid(row=4,column=0,sticky=W+E,padx=0,pady=3,)
        self.items_v.append(IntVar())
        b6=Checkbutton(group,text=self.items[5],variable=self.items_v[-1],indicatoron=FALSE,command = self.checkB6,bd=3,padx=35,bg='#32CD32',fg='#FF0000')
        b6.grid(row=5,column=0,sticky=W+E,padx=0,pady=3,)


        #sw = self.winfo_screenwidth()#得到屏幕宽度
        #sh = self.winfo_screenheight()#得到屏幕高度
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
  # 设置参数
  # 弹窗
    def ask_userinfo(self):
        inputDialog = MyDialog()
        self.wait_window(inputDialog) # 这一句很重要！！！
        #return inputDialog.userinfo   
    def checkB1(self):
        if self.items_v[0].get()==1:
            self.B1 = Html_Page()
            self.wait_window(self.B1) # 这一句很重要！！！
                        
        elif self.items_v[0].get()==0:
            self.B1.close()
    def key(self,event):
        print(event.keysym)
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


    def checkB2(self):
        pass

    def checkB3(self):
        pass
    def checkB4(self):
        pass
    def checkB5(self):
        if self.items_v[4].get()==1:
            self.B5 = serial_com.ComWin()
        elif self.items_v[4].get()==0:
            self.B5.close()
    def checkB6(self):
        pass

    def destroy(self):
        super().destroy()
        self.B5.close()
        


#def key(event):
#    print(event.char)


if __name__ == '__main__':
      
    app = MyApp()
    #app.bind('<Key>',key)
    a=messagebox.showinfo('提示', '请用组合键控制程序，ALT+END是退出，ALT+方向键可以移动窗口位置！！')
    
    app.mainloop()
    
    