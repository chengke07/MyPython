'''
@Author: your name
@Date: 2019-12-19 11:32:42
@LastEditTime : 2019-12-25 12:03:32
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\tk3.py
'''
from tkinter import *

def callback():
    var.set("吹吧你，我才不信呢。")



root = Tk()

v = IntVar()
GIRLS = ['西施','貂蝉','王昭君','杨玉环','小美']
LANGS = [('Python',1),('Perl',2),('Ruby',3),('Lua',4)]
v1 = []
v2 = IntVar()
v2.set(1)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
group = LabelFrame(root,text='最好的脚步语言是：',padx=5,pady=5,)


var = StringVar()
var.set('你所下载的影片含有未成年人限制内容，\n请满18周所后再点击浏览！')

textlabel = Label(frame1,
textvariable = var,
justify = LEFT
)
textlabel.pack(side=LEFT) 

photo = PhotoImage(file='1.png')
imglabel = Label(frame1,image=photo)
imglabel.pack(side=RIGHT)

theButton = Button(frame2,text='我已满18周岁',command=callback)
theButton.pack()

c = Checkbutton(frame3,text='测试一下',variable=v)
c.pack()

l = Label(frame3,textvariable=v)
l.pack()

for girl in GIRLS:
    v1.append(IntVar())
    b = Checkbutton(frame3,text=girl,variable=v1[-1])
    c = Label(frame3,textvariable=v1[-1])
    b.pack(anchor=W,side=LEFT)
    c.pack(side=RIGHT)


for lang,num in LANGS:
    b = Radiobutton(group,text=lang,variable=v2,value=num,indicatoron=FALSE)
    b.pack(fill=X)


frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
frame3.pack()
frame4.pack()
group.pack(padx=10,pady=10)



e = Entry(root)
e.pack(padx=20,pady=20)
e.delete(0,END)
#e.insert(0,'默认文本...')
s = StringVar()
s.set('获取输入文本')
txt=Label(root,textvariable=s,)
txt.pack()


def show():
    s.set(e.get())

Button(root,textvariable=s,command=show).pack()


mainloop()