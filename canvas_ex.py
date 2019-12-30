'''
@Author: your name
@Date: 2019-12-25 16:34:25
@LastEditTime : 2019-12-25 16:41:22
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\canvas_ex.py
'''
from tkinter import *

root = Tk()

w = Canvas(root,width=400,height=200)
w.pack()

def paint(event):
    x1,y1 = (event.x - 1),(event.y - 1)
    x2,y2 = (event.x + 1),(event.y + 1)
    w.create_oval(x1,y1,x2,y2,fill='red')

w.bind("<B1-Motion>",paint)

Label(root,text='按住鼠标左键，开始绘制你的图形').pack(side=BOTTOM)

mainloop()

