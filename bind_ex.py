'''
@Author: your name
@Date: 2019-12-29 19:03:13
@LastEditTime : 2019-12-30 14:45:44
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\bind_ex.py
'''

from tkinter import *

root = Tk()

def callback1(event):
    print('点击位置:',event.x,event.y)

frame1 = Frame(root,width=200,height=200,bg='green')
frame1.bind('<Button-1>',callback1)
frame1.pack()

def callback2(event):
    print('按下的是:',event.keysym)

frame2 = Frame(root,width=200,height=200,bg='blue')
frame2.bind('<Key>',callback2)
frame2.focus_set()
frame2.pack()


def callback3(event):
    print('当前位置是:',event.x,event.y)

frame3 = Frame(root,width=200,height=200,bg='red')
frame3.bind('<Motion>',callback3)
frame3.pack()



mainloop()